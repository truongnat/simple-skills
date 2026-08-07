param (
    [Parameter(Position = 0)]
    [ValidateSet("install", "update", "doctor")]
    [string]$Command = "install",

    [string]$AgentName = "agents"
)

$ErrorActionPreference = "Stop"

$Owner = if ($env:SIMPLE_SKILLS_OWNER) { $env:SIMPLE_SKILLS_OWNER } else { "truongnat" }
$Repo = if ($env:SIMPLE_SKILLS_REPO) { $env:SIMPLE_SKILLS_REPO } else { "simple-skills" }
$Branch = if ($env:SIMPLE_SKILLS_BRANCH) { $env:SIMPLE_SKILLS_BRANCH } else { "main" }
$Github = "$Owner/$Repo"

$Target = (Get-Location).Path
$Source = $null
$Tmp = $null

$AgentDirName = ".$AgentName"
$AgentDir = Join-Path $Target $AgentDirName

function Cleanup {
    if ($null -ne $Tmp -and (Test-Path $Tmp)) {
        Remove-Item -Path $Tmp -Recurse -Force -ErrorAction SilentlyContinue
    }
}
$ExecutionContext.SessionState.Module.OnRemove = [scriptblock]::Create("Cleanup")

function Fetch-Source {
    Write-Host "Downloading $Github@$Branch ..."
    $global:Tmp = New-TemporaryFile | Rename-Item -NewName { [IO.Path]::ChangeExtension($_, ".zip") } -PassThru
    $url = "https://github.com/$Github/archive/refs/heads/$Branch.zip"
    
    Invoke-WebRequest -Uri $url -OutFile $global:Tmp.FullName
    $extractPath = Join-Path ([System.IO.Path]::GetTempPath()) "simple-skills-$(New-Guid)"
    Expand-Archive -Path $global:Tmp.FullName -DestinationPath $extractPath -Force
    Remove-Item $global:Tmp.FullName -Force

    # Find the extracted folder (e.g., simple-skills-main)
    $extractedDir = Get-ChildItem -Path $extractPath -Directory | Select-Object -First 1
    $global:Source = $extractedDir.FullName
    $global:Tmp = $extractPath
}

function Is-SimpleSkillsSource([string]$Root) {
    return (Test-Path (Join-Path $Root "docs\AGENTS.md")) -and
           (Test-Path (Join-Path $Root "skills\planning\SKILL.md")) -and
           (Test-Path (Join-Path $Root "skills\execution\SKILL.md"))
}

function Copy-DocsAndTools {
    $kitFlatDocs = @(
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

    $flatThinkingDocs = Join-Path $AgentDir "THINKING_OUTCOME_FIRST.md"
    if (Test-Path $flatThinkingDocs) { Remove-Item $flatThinkingDocs -Force }

    foreach ($rel in $kitFlatDocs) {
        $relWin = $rel -replace "/", "\"
        $srcFile = Join-Path $Source "docs\$relWin"
        if (-not (Test-Path $srcFile)) {
            $flat = Join-Path $Source "docs\$([System.IO.Path]::GetFileName($relWin))"
            if (Test-Path $flat) { $srcFile = $flat }
        }
        if (Test-Path $srcFile) {
            $destFile = Join-Path $AgentDir ([System.IO.Path]::GetFileName($relWin))
            Copy-Item -Path $srcFile -Destination $destFile -Force
        }
    }

    $thinkingDir = Join-Path $AgentDir "thinking"
    if (Test-Path $thinkingDir) { Remove-Item $thinkingDir -Recurse -Force }
    $srcThinking = Join-Path $Source "docs\thinking"
    if (Test-Path $srcThinking) {
        Copy-Item -Path $srcThinking -Destination $thinkingDir -Recurse -Force
    }

    $examplesDir = Join-Path $AgentDir "examples"
    if (Test-Path $examplesDir) { Remove-Item $examplesDir -Recurse -Force }
    $srcExamples = Join-Path $Source "docs\examples"
    if (Test-Path $srcExamples) {
        Copy-Item -Path $srcExamples -Destination $examplesDir -Recurse -Force
    }

    $settingsYaml = Join-Path $AgentDir "settings.yaml"
    if (-not (Test-Path $settingsYaml)) {
        $srcSettings = Join-Path $Source "docs\config\settings.yaml"
        if (Test-Path $srcSettings) {
            Copy-Item -Path $srcSettings -Destination $settingsYaml -Force
        }
    }

    $workLoc = ".agent-work"
    if (Test-Path $settingsYaml) {
        $content = Get-Content $settingsYaml -Raw
        if ($content -match 'agent_work:\s*\n\s*location:\s*(.+)($|\n)') {
            $workLoc = $matches[1].Trim(" '`"")
        }
    }

    $gi = Join-Path $Target ".gitignore"
    $marker = "$workLoc/"
    $needsMarker = $true
    if (Test-Path $gi) {
        $lines = Get-Content $gi
        foreach ($line in $lines) {
            if ($line.Trim() -eq $marker) {
                $needsMarker = $false
                break
            }
        }
    }
    
    if ($needsMarker) {
        $append = "`n# Simple Skills — Work layer`n$marker`n"
        Add-Content -Path $gi -Value $append -Encoding utf8
    }

    $srcTools = Join-Path $Source "tools"
    if (Test-Path $srcTools) {
        $destTools = Join-Path $AgentDir "tools"
        if (-not (Test-Path $destTools)) { New-Item -ItemType Directory -Path $destTools | Out-Null }
        
        $existingItems = Get-ChildItem -Path $destTools
        foreach ($item in $existingItems) {
            if ($item.Name -ne "decision-logs") {
                Remove-Item $item.FullName -Recurse -Force
            }
        }
        
        $newItems = Get-ChildItem -Path $srcTools
        foreach ($item in $newItems) {
            if ($item.Name -ne "decision-logs") {
                Copy-Item -Path $item.FullName -Destination $destTools -Recurse -Force
            }
        }
    }

    $sessionDir = Join-Path $AgentDir "tools\session"
    if (-not (Test-Path $sessionDir)) { New-Item -ItemType Directory -Path $sessionDir -Force | Out-Null }
    $srcSchemas = Join-Path $Source "docs\config\artifact-schemas.json"
    if (Test-Path $srcSchemas) {
        Copy-Item -Path $srcSchemas -Destination (Join-Path $sessionDir "artifact-schemas.json") -Force
    }

    $srcAgentsMd = Join-Path $Source "docs\AGENTS.md"
    if (Test-Path $srcAgentsMd) {
        Copy-Item -Path $srcAgentsMd -Destination (Join-Path $Target "AGENTS.md") -Force
    }
    
    $nestedAgentsMd = Join-Path $AgentDir "AGENTS.md"
    if (Test-Path $nestedAgentsMd) { Remove-Item $nestedAgentsMd -Force }
}

function Cmd-Install {
    if (Is-SimpleSkillsSource $Target) {
        $global:Source = $Target
    } else {
        Fetch-Source
    }

    Write-Host "Installing all skills into $AgentDir ..."

    if (Test-Path $AgentDir) {
        Write-Host "Removing existing $AgentDirName directory for a fresh install..."
        Remove-Item $AgentDir -Recurse -Force
    }
    
    $skillsDir = Join-Path $AgentDir "skills"
    New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null

    $srcSkills = Join-Path $Source "skills"
    if (Test-Path $srcSkills) {
        $skillDirs = Get-ChildItem -Path $srcSkills -Directory
        foreach ($sDir in $skillDirs) {
            $destSkill = Join-Path $skillsDir $sDir.Name
            New-Item -ItemType Directory -Path $destSkill -Force | Out-Null
            
            $items = Get-ChildItem -Path $sDir.FullName
            foreach ($item in $items) {
                if ($item.Name -ne ".venv") {
                    Copy-Item -Path $item.FullName -Destination $destSkill -Recurse -Force
                }
            }
        }
    }

    Copy-DocsAndTools
    Write-Host "Installation complete."
}

function Cmd-Update {
    if (Is-SimpleSkillsSource $Target) {
        $global:Source = $Target
    } else {
        Fetch-Source
    }

    Write-Host "Updating own skills in $AgentDir ..."

    $skillsDir = Join-Path $AgentDir "skills"
    if (-not (Test-Path $skillsDir)) {
        New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null
    }

    $srcSkills = Join-Path $Source "skills"
    if (Test-Path $srcSkills) {
        $skillDirs = Get-ChildItem -Path $srcSkills -Directory
        foreach ($sDir in $skillDirs) {
            $destSkill = Join-Path $skillsDir $sDir.Name
            
            if (Test-Path $destSkill) {
                $items = Get-ChildItem -Path $destSkill
                foreach ($item in $items) {
                    if ($item.Name -ne ".venv") {
                        Remove-Item $item.FullName -Recurse -Force
                    }
                }
            } else {
                New-Item -ItemType Directory -Path $destSkill -Force | Out-Null
            }
            
            $items = Get-ChildItem -Path $sDir.FullName
            foreach ($item in $items) {
                if ($item.Name -ne ".venv") {
                    Copy-Item -Path $item.FullName -Destination $destSkill -Recurse -Force
                }
            }
        }
    }

    Copy-DocsAndTools
    Write-Host "Update complete."
}

function Cmd-Doctor {
    $ok = $true
    Write-Host "DOCTOR check for project in $Target with agent directory $AgentDirName"
    
    if (-not (Test-Path $AgentDir)) {
        Write-Host "ERROR: Directory $AgentDirName is missing. Run install command."
        return
    }

    $checkFiles = @("START_HERE.md", "WHAT_NEXT.md", "SKILL_PREAMBLE.md", "AGENT_POLICY.md", "settings.yaml", "BA_SKILLS.md")
    foreach ($f in $checkFiles) {
        if (-not (Test-Path (Join-Path $AgentDir $f))) {
            Write-Host "Missing: kit_$f"
            $ok = $false
        }
    }

    if (-not (Test-Path (Join-Path $Target "AGENTS.md"))) {
        Write-Host "Missing: root_AGENTS.md"
        $ok = $false
    }

    if ($ok) {
        Write-Host "DOCTOR: Everything looks good!"
    } else {
        Write-Host "DOCTOR: Found some missing files or issues. Consider running update or install."
    }
}

try {
    switch ($Command) {
        "install" { Cmd-Install }
        "update"  { Cmd-Update }
        "doctor"  { Cmd-Doctor }
    }
} finally {
    Cleanup
}
