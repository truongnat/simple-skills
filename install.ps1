param(
    [ValidateSet("install", "uninstall", "doctor")]
    [string]$Command = "install",

    [ValidateSet("prompt", "replace", "skip")]
    [string]$AgentsMode,

    [ValidateSet("prompt", "replace", "skip", "rename")]
    [string]$ConflictMode,

    [string]$Profile,

    [switch]$Yes,
    [switch]$KeepSettings,
    [switch]$PurgeWork,
    [switch]$PurgeUnselected
)

$ErrorActionPreference = "Stop"

# GitHub requires TLS 1.2; older Windows PowerShell may default to TLS 1.0/1.1.
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$Owner = if ($env:SIMPLE_SKILLS_OWNER) { $env:SIMPLE_SKILLS_OWNER } else { "truongnat" }
$Repo = if ($env:SIMPLE_SKILLS_REPO) { $env:SIMPLE_SKILLS_REPO } else { "simple-skills" }
$Branch = if ($env:SIMPLE_SKILLS_BRANCH) { $env:SIMPLE_SKILLS_BRANCH } else { "main" }
$Github = "$Owner/$Repo"
if (-not $AgentsMode) {
    $AgentsMode = if ($env:SIMPLE_SKILLS_AGENTS_MODE) {
        $env:SIMPLE_SKILLS_AGENTS_MODE.ToLowerInvariant()
    } else {
        "prompt"
    }
}
if ($AgentsMode -notin @("prompt", "replace", "skip")) {
    throw "AgentsMode must be prompt, replace, or skip."
}
if (-not $ConflictMode) {
    $ConflictMode = if ($env:SIMPLE_SKILLS_CONFLICT_MODE) {
        $env:SIMPLE_SKILLS_CONFLICT_MODE.ToLowerInvariant()
    } else {
        "prompt"
    }
}
if ($ConflictMode -notin @("prompt", "replace", "skip", "rename")) {
    throw "ConflictMode must be prompt, replace, skip, or rename."
}
if (-not $Profile) {
    $Profile = if ($env:SIMPLE_SKILLS_PROFILE) {
        $env:SIMPLE_SKILLS_PROFILE
    } else {
        "core"
    }
}

$Target = Get-Location
$Source = $null
$Tmp = $null

function Remove-Tmp {
    if ($Tmp -and (Test-Path $Tmp)) {
        Remove-Item -Path $Tmp -Recurse -Force
    }
}

function Get-UniqueSkillName {
    param([string]$BaseName, [string]$SkillsDir)
    $name = $BaseName
    $counter = 1
    while (Test-Path (Join-Path $SkillsDir $name)) {
        $name = "${BaseName}${counter}"
        $counter++
    }
    return $name
}

function Resolve-ConflictAction {
    param([string]$SkillName, [string]$Mode)
    if ($Mode -eq "replace") { return "replace" }
    if ($Mode -eq "skip") { return "skip" }
    if ($Mode -eq "rename") { return "rename" }
    
    # prompt mode
    Write-Host ""
    Write-Host "Skill '$SkillName' already exists." -ForegroundColor Yellow
    $answer = Read-Host "[R]eplace / [S]kip / [C]opy to new name (skill-A1) / [A]bort? (R/S/C/A)"
    switch -Regex ($answer.ToLower()) {
        "^(r|replace|y|yes)$" { return "replace" }
        "^(s|skip|n|no)$" { return "skip" }
        "^(c|copy|rename)$" { return "rename" }
        default { return "abort" }
    }
}

function Resolve-InstallSkills {
    param(
        [string]$SourceRoot,
        [string]$ProfileName
    )
    $resolver = Join-Path $SourceRoot "scripts/resolve_install_profile.py"
    $python = Get-Command python3 -ErrorAction SilentlyContinue
    if (-not $python) {
        $python = Get-Command python -ErrorAction SilentlyContinue
    }
    if ($python) {
        $output = & $python.Source $resolver --source $SourceRoot --profile $ProfileName --check
        if ($LASTEXITCODE -ne 0) {
            throw "Failed to resolve install profile '$ProfileName'."
        }
        return @($output | Where-Object { $_ -and $_.Trim() })
    }
    if ($ProfileName -ne "all") {
        throw "Python is required to resolve install profile '$ProfileName'. Use -Profile all."
    }
    return @(Get-ChildItem -Path (Join-Path $SourceRoot "skills") -Directory |
        Sort-Object Name |
        ForEach-Object { $_.Name })
}

$KitFlatDocs = @(
    "conventions/DESIGN_SYSTEM.md",
    "conventions/CODE_COMMENTS.md",
    "conventions/THIRD_PARTY_SKILLS.md",
    "policy/SKILL_PREAMBLE.md",
    "policy/AGENT_POLICY.md",
    "policy/AGENT_WORK.md",
    "guides/START_HERE.md",
    "guides/WHAT_NEXT.md",
    "guides/MIGRATION.md",
    "guides/BA_SKILLS.md"
)

$ThinkingDocs = @(
    "outcome-first.md",
    "input-process-output.md",
    "make-implicit-explicit.md",
    "single-source-of-truth.md",
    "small-batch.md",
    "feedback-loop.md",
    "default-path-first.md",
    "reversible-decisions.md",
    "standardize-before-automate.md",
    "design-for-handoff.md",
    "evidence-over-confidence.md",
    "optimize-bottleneck.md",
    "README.md"
)

function Test-DoctorFile {
    param([string]$Label, [string]$Path)
    if (Test-Path $Path -PathType Leaf) {
        Write-Host "${Label}=yes"
        return $true
    }
    Write-Host "${Label}=missing"
    return $false
}

function Invoke-Doctor {
    $ok = $true
    Write-Host "DOCTOR project=$($Target.Path)"

    if (Test-Path (Join-Path $Target.Path ".agents") -PathType Container) {
        Write-Host "agents_dir=yes"
    } else {
        Write-Host "agents_dir=MISSING — run install.ps1"
        $ok = $false
    }

    foreach ($f in @(
            "START_HERE.md", "WHAT_NEXT.md", "SKILL_PREAMBLE.md",
            "AGENT_POLICY.md", "settings.yaml", "BA_SKILLS.md"
        )) {
        if (-not (Test-DoctorFile "kit_${f}" (Join-Path $Target.Path ".agents/$f"))) {
            $ok = $false
        }
    }

    foreach ($f in $ThinkingDocs) {
        if (-not (Test-DoctorFile "kit_thinking/${f}" (Join-Path $Target.Path ".agents/thinking/$f"))) {
            $ok = $false
        }
    }

    if (-not (Test-DoctorFile "root_AGENTS.md" (Join-Path $Target.Path "AGENTS.md"))) {
        $ok = $false
    }

    $gi = Join-Path $Target.Path ".gitignore"
    if ((Test-Path $gi -PathType Leaf) -and
        (Select-String -Path $gi -Pattern '^\.agent-work/$' -Quiet)) {
        Write-Host "gitignore_agent_work=yes"
    } else {
        Write-Host "gitignore_agent_work=MISSING"
        $ok = $false
    }

    $work = Join-Path $Target.Path ".agent-work"
    if (Test-Path $work -PathType Container) {
        Write-Host "work_dir=yes"
        if (Test-Path (Join-Path $work ".git") -PathType Container) {
            Write-Host "work_nested_git=yes"
        } else {
            Write-Host "work_nested_git=no"
        }
    } else {
        Write-Host "work_dir=(none yet)"
    }

    $sess = Join-Path $Target.Path ".agents/tools/session/session.sh"
    if (Test-Path $sess -PathType Leaf) {
        Write-Host "session_tool=yes"
        try {
            $out = & bash $sess doctor 2>$null
            if ($LASTEXITCODE -eq 0) {
                foreach ($line in $out) { Write-Host "session_$line" }
            } else {
                Write-Host "session_doctor=warn (could not run)"
            }
        } catch {
            Write-Host "session_doctor=warn (could not run)"
        }
    } else {
        Write-Host "session_tool=missing"
        $ok = $false
    }

    foreach ($t in @("validate_artifacts.py", "lint_artifacts.py", "build_context.py")) {
        if (Test-Path (Join-Path $Target.Path ".agents/tools/session/$t") -PathType Leaf) {
            Write-Host "tool_${t}=yes"
        } else {
            Write-Host "tool_${t}=missing"
            $ok = $false
        }
    }

    if ($ok) {
        Write-Host "DOCTOR_OK"
        exit 0
    }
    Write-Host "DOCTOR_FAIL"
    exit 1
}

function Invoke-Uninstall {
    if (-not $Yes) {
        $answer = Read-Host "Uninstall Simple Skills kit from $($Target.Path)? [y/N]"
        if ($answer -notmatch "^(?i:y|yes)$") {
            Write-Host "Aborted."
            return
        }
    }

    $settingsBackup = $null
    $settingsSrc = Join-Path $Target.Path ".agents/settings.yaml"
    if ($KeepSettings -and (Test-Path $settingsSrc -PathType Leaf)) {
        $settingsBackup = Join-Path ([System.IO.Path]::GetTempPath()) ("ss-settings-" + [guid]::NewGuid().ToString())
        Copy-Item -Path $settingsSrc -Destination $settingsBackup -Force
        Write-Host "Backing up settings.yaml ..."
    }

    $agents = Join-Path $Target.Path ".agents"
    if (Test-Path $agents) {
        Write-Host "Removing $agents ..."
        Remove-Item -Path $agents -Recurse -Force
    } else {
        Write-Host "No .agents/ directory to remove."
    }

    $agentsMd = Join-Path $Target.Path "AGENTS.md"
    if (Test-Path $agentsMd -PathType Leaf) {
        Write-Host "Removing $agentsMd ..."
        Remove-Item -Path $agentsMd -Force
    }

    if ($settingsBackup) {
        New-Item -ItemType Directory -Force -Path (Join-Path $Target.Path ".agents") | Out-Null
        Copy-Item -Path $settingsBackup -Destination (Join-Path $Target.Path ".agents/settings.yaml") -Force
        Remove-Item -Path $settingsBackup -Force
        Write-Host "Restored .agents/settings.yaml (-KeepSettings)."
    }

    if ($PurgeWork) {
        $work = Join-Path $Target.Path ".agent-work"
        if (Test-Path $work) {
            Write-Host "Removing $work (-PurgeWork) ..."
            Remove-Item -Path $work -Recurse -Force
        }
    } else {
        Write-Host "Keeping .agent-work/ (sessions/memory). Use -PurgeWork to delete."
    }

    Write-Host "Uninstall complete. (.gitignore .agent-work/ entry left in place if present.)"
}

function Invoke-Install {
    function Test-SimpleSkillsSource {
        param([string]$Root)
        return (Test-Path (Join-Path $Root "docs/AGENTS.md") -PathType Leaf) `
            -and (Test-Path (Join-Path $Root "skills/planning/SKILL.md") -PathType Leaf) `
            -and (Test-Path (Join-Path $Root "skills/execution/SKILL.md") -PathType Leaf)
    }

    if (Test-SimpleSkillsSource -Root $Target.Path) {
        $script:Source = $Target.Path
    } else {
        Write-Host "Downloading ${Github}@${Branch} ..."
        $script:Tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("simple-skills-" + [guid]::NewGuid().ToString())
        New-Item -ItemType Directory -Force -Path $script:Tmp | Out-Null

        $Archive = Join-Path $script:Tmp "repo.zip"
        $Extract = Join-Path $script:Tmp "extract"
        $ZipUrl = "https://github.com/$Github/archive/refs/heads/$Branch.zip"

        Invoke-WebRequest -Uri $ZipUrl -OutFile $Archive -UseBasicParsing
        Expand-Archive -Path $Archive -DestinationPath $Extract -Force

        $script:Source = Get-ChildItem -Path $Extract -Directory |
            Select-Object -First 1 -ExpandProperty FullName
    }

    Write-Host "Installing skills into $((Get-Location).Path)\.agents (profile: $Profile) ..."

    New-Item -ItemType Directory -Force -Path ".agents" | Out-Null
    New-Item -ItemType Directory -Force -Path ".agents/skills" | Out-Null

    $selected = Resolve-InstallSkills -SourceRoot $Source -ProfileName $Profile
    if ($selected.Count -eq 0) {
        throw "Profile '$Profile' resolved to zero skills."
    }
    Write-Host "Installing $($selected.Count) skills."

    $skillsDir = Join-Path ".agents/skills" ""
    $abortInstall = $false

    foreach ($skillName in $selected) {
        if ($abortInstall) { break }
        
        $skillPath = Join-Path $Source "skills/$skillName"
        if (-not (Test-Path $skillPath -PathType Container)) {
            throw "Missing skill source: $skillName"
        }
        
        $dest = Join-Path ".agents/skills" $skillName
        $skillExists = Test-Path $dest -PathType Container
        
        # Handle conflict if skill already exists
        if ($skillExists) {
            $action = Resolve-ConflictAction -SkillName $skillName -Mode $ConflictMode
            
            switch ($action) {
                "skip" {
                    Write-Host "Skipping skill $skillName (keeping existing)."
                    continue
                }
                "rename" {
                    $newName = Get-UniqueSkillName -BaseName $skillName -SkillsDir $skillsDir
                    $dest = Join-Path ".agents/skills" $newName
                    Write-Host "Installing skill $skillName as $newName ..."
                }
                "replace" {
                    Write-Host "Replacing skill $skillName ..."
                }
                "abort" {
                    Write-Host "Aborting install."
                    $abortInstall = $true
                    continue
                }
            }
        } else {
            Write-Host "Installing skill $skillName ..."
        }
        
        if ($abortInstall) { continue }
        
        New-Item -ItemType Directory -Force -Path $dest | Out-Null
        
        # Only remove existing content if we're replacing
        if ($skillExists -and $dest -eq (Join-Path ".agents/skills" $skillName)) {
            Get-ChildItem -Path $dest -Force |
                Where-Object { $_.Name -ne ".venv" } |
                Remove-Item -Recurse -Force
        }
        
        Get-ChildItem -Path $skillPath -Force |
            Where-Object { $_.Name -ne ".venv" } |
            Copy-Item -Destination $dest -Recurse -Force
    }
    
    if ($abortInstall) {
        throw "Installation aborted by user."
    }

    if ($PurgeUnselected) {
        $selectedSet = [System.Collections.Generic.HashSet[string]]::new(
            [string[]]$selected,
            [System.StringComparer]::OrdinalIgnoreCase
        )
        Get-ChildItem -Path ".agents/skills" -Directory | ForEach-Object {
            if (-not $selectedSet.Contains($_.Name)) {
                Write-Host "Removing skill not in profile: $($_.Name) ..."
                Remove-Item -Path $_.FullName -Recurse -Force
            }
        }
    } else {
        Write-Host "Keeping existing skills not in profile (use -PurgeUnselected to remove)."
    }

    $obsoleteOfficeMcp = Join-Path ".agents/skills" "office-mcp"
    if (Test-Path $obsoleteOfficeMcp) {
        Write-Host "Removing obsolete skill office-mcp ..."
        Remove-Item -Path $obsoleteOfficeMcp -Recurse -Force
    }

    $obsoleteThinking = Join-Path ".agents" "THINKING_OUTCOME_FIRST.md"
    if (Test-Path $obsoleteThinking -PathType Leaf) {
        Remove-Item -Path $obsoleteThinking -Force
    }

    foreach ($rel in $KitFlatDocs) {
        $name = Split-Path $rel -Leaf
        Copy-Item -Path (Join-Path $Source "docs/$rel") -Destination ".agents/$name" -Force
    }

    $thinkingDest = ".agents/thinking"
    if (Test-Path $thinkingDest) {
        Remove-Item -Path $thinkingDest -Recurse -Force
    }
    New-Item -ItemType Directory -Force -Path $thinkingDest | Out-Null
    Copy-Item -Path (Join-Path $Source "docs/thinking/*") -Destination $thinkingDest -Force
    foreach ($f in $ThinkingDocs) {
        if (-not (Test-Path (Join-Path $thinkingDest $f) -PathType Leaf)) {
            throw "Missing thinking doc after copy: $f"
        }
    }

    $examplesSource = Join-Path $Source "docs/examples"
    if (Test-Path $examplesSource -PathType Container) {
        $examplesDest = Join-Path ".agents" "examples"
        if (Test-Path $examplesDest) { Remove-Item -Path $examplesDest -Recurse -Force }
        Copy-Item -Path $examplesSource -Destination $examplesDest -Recurse -Force
    }

    $gitignorePath = Join-Path $Target.Path ".gitignore"
    $marker = ".agent-work/"
    if ((Test-Path $gitignorePath -PathType Leaf) -and
        (Select-String -Path $gitignorePath -Pattern '^\.agent-work/$' -Quiet)) {
        Write-Host "Keeping existing .gitignore entry for .agent-work/."
    } elseif (Test-Path $gitignorePath -PathType Leaf) {
        Add-Content -Path $gitignorePath -Value "`n# Simple Skills — Work layer (sessions + memory; nested git)`n$marker"
        Write-Host "Appended .agent-work/ to existing .gitignore."
    } else {
        Copy-Item -Path (Join-Path $Source "docs/config/gitignore.agent-work.snippet") `
            -Destination $gitignorePath -Force
        Write-Host "Created .gitignore with .agent-work/ ignore rule."
    }

    $toolsSource = Join-Path $Source "tools"
    if (Test-Path $toolsSource -PathType Container) {
        Write-Host "Installing tools into .agents/tools ..."
        $toolsDest = Join-Path ".agents" "tools"
        New-Item -ItemType Directory -Force -Path $toolsDest | Out-Null
        Get-ChildItem -Path $toolsDest -Force |
            Where-Object { $_.Name -ne "decision-logs" } |
            Remove-Item -Recurse -Force
        Get-ChildItem -Path $toolsSource -Force |
            Where-Object { $_.Name -ne "decision-logs" } |
            Copy-Item -Destination $toolsDest -Recurse -Force
    }

    New-Item -ItemType Directory -Force -Path ".agents/tools/session" | Out-Null
    Copy-Item -Path (Join-Path $Source "docs/config/artifact-schemas.json") `
        -Destination ".agents/tools/session/artifact-schemas.json" -Force

    $settingsDest = Join-Path ".agents" "settings.yaml"
    if (Test-Path $settingsDest -PathType Leaf) {
        Write-Host "Keeping existing .agents/settings.yaml."
    } else {
        Copy-Item -Path (Join-Path $Source "docs/config/settings.yaml") -Destination $settingsDest -Force
    }

    $installAgentsFile = $true
    $agentsPath = Join-Path $Target.Path "AGENTS.md"
    if (Test-Path $agentsPath -PathType Leaf) {
        switch ($AgentsMode) {
            "replace" {
                Write-Host "Replacing existing $agentsPath ..."
            }
            "skip" {
                Write-Host "Keeping existing $agentsPath."
                $installAgentsFile = $false
            }
            "prompt" {
                try {
                    $answer = Read-Host "AGENTS.md already exists. Replace it? [y/N]"
                }
                catch {
                    $answer = ""
                    Write-Warning "No interactive prompt is available."
                }
                if ($answer -match "^(?i:y|yes)$") {
                    Write-Host "Replacing existing $agentsPath ..."
                } else {
                    Write-Host "Keeping existing $agentsPath."
                    Write-Host "Use -AgentsMode replace or SIMPLE_SKILLS_AGENTS_MODE=replace to replace it."
                    $installAgentsFile = $false
                }
            }
        }
    }
    if ($installAgentsFile) {
        Copy-Item -Path (Join-Path $Source "docs/AGENTS.md") -Destination $agentsPath -Force
    }

    $obsoleteAgentsPath = Join-Path ".agents" "AGENTS.md"
    if (Test-Path $obsoleteAgentsPath) {
        Remove-Item -Path $obsoleteAgentsPath -Force
    }

    Write-Host "Skills installed successfully (profile: $Profile)."
    Write-Host "Next: bash .agents/tools/session/session.sh doctor   # or: .\install.ps1 -Command doctor"
}

try {
    switch ($Command) {
        "doctor" { Invoke-Doctor }
        "uninstall" { Invoke-Uninstall }
        default { Invoke-Install }
    }
}
finally {
    Remove-Tmp
}
