# Integration Map for Executing Plans

## Overview

This map defines how sk-executing-pro integrates with other skills in this repository.

## Skill Dependencies

### Upstream Skills (Use Before sk-executing-pro)

**planning-pro**
- **When to call:** Before execution
- **Purpose:** Create detailed execution plan
- **Handoff:** Task list with dependencies, acceptance criteria, estimates
- **Integration:** sk-executing-pro uses planning-pro output for execution

**planning-pro**
- **When to call:** Before execution
- **Purpose:** High-level coordination and milestone tracking
- **Handoff:** Milestone structure and high-level dependencies
- **Integration:** sk-executing-pro coordinates with planning-pro milestones

### Downstream Skills (Use After or During sk-executing-pro)

**Domain *-pro skills**
- **When to call:** During execution for technical task execution
- **Purpose:** Execute technical tasks within their stack
- **Handoff:** Task assignment and technical guidance
- **Integration:** sk-executing-pro coordinates domain skill execution

**sk-systematic-debugging-pro**
- **When to call:** When issues or blockers occur during execution
- **Purpose:** Debug and resolve execution issues
- **Handoff:** Issue details and context
- **Integration:** sk-executing-pro uses sk-systematic-debugging-pro for issue resolution

**sk-testing-pro**
- **When to call:** During execution for verification
- **Purpose:** Verify work meets acceptance criteria
- **Handoff:** Tasks to verify
- **Integration:** sk-executing-pro uses sk-testing-pro for verification

**sk-feedback-pro**
- **When to call:** After execution for review
- **Purpose:** Review execution quality and outcomes
- **Handoff:** Execution results
- **Integration:** sk-executing-pro uses sk-feedback-pro for quality review

**sk-git-operations-pro**
- **When to call:** During execution for version control
- **Purpose:** Manage code changes during execution
- **Handoff:** Changes to commit
- **Integration:** sk-executing-pro uses sk-git-operations-pro for version control

## Integration Scenarios

### Scenario 1: Standard Feature Execution

**Flow:**
1. **planning-pro** creates detailed plan
2. **sk-executing-pro** executes plan
3. Domain ***-pro skills** execute technical tasks
4. **sk-testing-pro** verifies work
5. **sk-executing-pro** coordinates checkpoints
6. **sk-feedback-pro** reviews execution

**Key Integration Points:**
- Plan to execution (planning-pro → sk-executing-pro)
- Task execution (sk-executing-pro → domain skills)
- Verification (sk-executing-pro → sk-testing-pro)
- Review (sk-executing-pro → sk-feedback-pro)

### Scenario 2: Debugging During Execution

**Flow:**
1. **sk-executing-pro** encounters blocker
2. **sk-systematic-debugging-pro** diagnoses issue
3. Domain ***-pro skills** implement fix
4. **sk-executing-pro** resumes execution
5. **sk-testing-pro** verifies fix

**Key Integration Points:**
- Issue detection (sk-executing-pro)
- Debugging (sk-executing-pro → sk-systematic-debugging-pro)
- Fix implementation (sk-executing-pro → domain skills)
- Fix verification (sk-executing-pro → sk-testing-pro)

### Scenario 3: Adaptive Replanning

**Flow:**
1. **sk-executing-pro** identifies need to replan
2. **planning-pro** assists with replanning
3. **planning-pro** updates detailed plan
4. **sk-executing-pro** continues with new plan

**Key Integration Points:**
- Replan trigger (sk-executing-pro)
- Replan assistance (sk-executing-pro → planning-pro)
- Plan update (sk-executing-pro → planning-pro)

## Handoff Protocols

### From planning-pro

**When:** Plan ready for execution
**Input:** Detailed task list with dependencies, criteria, estimates
**Output:** Execution status and completion
**Protocol:**
- Receive complete task list
- Receive dependency map
- Receive acceptance criteria
- Receive estimates and risks
- Execute and report status

### To Domain Skills

**When:** Technical task execution needed
**Input:** Task with technical requirements
**Output:** Task completion
**Protocol:**
- Provide task description
- Provide acceptance criteria
- Receive task completion
- Verify acceptance criteria

### To sk-systematic-debugging-pro

**When:** Blocker or issue occurs
**Input:** Issue details and context
**Output:** Root cause and resolution
**Protocol:**
- Provide issue description
- Provide context and logs
- Receive diagnosis
- Implement resolution

### To sk-testing-pro

**When:** Verification needed
**Input:** Tasks to verify
**Output:** Verification results
**Protocol:**
- Provide tasks and acceptance criteria
- Receive verification results
- Address failures
- Mark tasks complete

### To sk-feedback-pro

**When:** Execution review needed
**Input:** Execution results
**Output:** Quality assessment
**Protocol:**
- Provide execution results
- Request quality review
- Receive assessment
- Incorporate feedback

### To sk-git-operations-pro

**When:** Version control needed
**Input:** Changes to commit
**Output:** Commit status
**Protocol:**
- Provide changes
- Request commit
- Receive commit status
- Track version

## Conflict Resolution

### Conflicts with planning-pro

**Scenario:** Execution reveals plan issues
**Resolution:**
- Pause execution
- Communicate plan issues to planning-pro
- Adjust plan
- Resume execution

### Conflicts with Domain Skills

**Scenario:** Technical approach issues
**Resolution:**
- Consult with domain skill
- Adjust technical approach
- Re-validate
- Continue execution

### Conflicts with sk-systematic-debugging-pro

**Scenario:** Debugging reveals deeper issues
**Resolution:**
- Accept diagnosis
- Implement recommended fix
- Verify fix
- Resume execution

### Conflicts with planning-pro

**Scenario:** Milestone conflicts with detailed execution
**Resolution:**
- Review milestone structure
- Adjust execution or milestone
- Ensure consistency
- Update both

## Quality Gates

### Before sk-executing-pro

- [ ] Plan received from planning-pro
- [ ] Dependencies understood
- [ ] Resources available
- [ ] Checkpoints defined

### During sk-executing-pro

- [ ] Domain skills consulted for technical execution
- [ ] Blockers handled with sk-systematic-debugging-pro
- [ ] Verification done with sk-testing-pro
- [ ] Version control with sk-git-operations-pro

### After sk-executing-pro

- [ ] Execution reviewed with sk-feedback-pro
- [ ] Lessons learned documented
- [ ] Stakeholders informed
- [ ] Plan updated if needed
