# Integration Map for Parallel Agents

## Overview

This map defines how sk-parallel-agents-pro integrates with other skills in this repository.

## Skill Dependencies

### Upstream Skills (Use Before sk-parallel-agents-pro)

**planning-pro**
- **When to call:** Before parallel execution
- **Purpose:** Create detailed plan with dependency mapping
- **Handoff:** Task list with dependencies and parallelization strategy
- **Integration:** sk-parallel-agents-pro uses planning-pro output for agent dispatch
- **When to call:** Before parallel execution
- **Purpose:** High-level coordination and milestone tracking
- **Handoff:** Milestone structure and high-level dependencies
- **Integration:** sk-parallel-agents-pro coordinates with planning-pro milestones

### Downstream Skills (Use After or During sk-parallel-agents-pro)

**sk-executing-pro**
- **When to call:** For sequential coordination of dependent tasks
- **Purpose:** Execute dependent tasks sequentially
- **Handoff:** Dependent tasks for sequential execution
- **Integration:** sk-parallel-agents-pro dispatches independent tasks, sk-executing-pro handles dependent

**Domain *-pro skills**
- **When to call:** During execution for agent task execution
- **Purpose:** Execute technical tasks within each agent
- **Handoff:** Task assignment and technical guidance
- **Integration:** sk-parallel-agents-pro coordinates domain skill execution across agents

**sk-systematic-debugging-pro**
- **When to call:** When agents encounter issues or blockers
- **Purpose:** Debug and resolve agent issues
- **Handoff:** Agent issue details and context
- **Integration:** sk-parallel-agents-pro uses sk-systematic-debugging-pro for agent issue resolution

**sk-feedback-pro**
- **When to call:** After execution for review
- **Purpose:** Review execution quality and outcomes
- **Handoff:** Execution results and aggregated output
- **Integration:** sk-parallel-agents-pro uses sk-feedback-pro for quality review

## Integration Scenarios

### Scenario 1: Parallel Task Execution

**Flow:**
1. **planning-pro** creates detailed plan with dependency mapping
2. **sk-parallel-agents-pro** dispatches independent tasks
3. Domain ***-pro skills** execute each agent task
4. **sk-parallel-agents-pro** aggregates results
5. **sk-executing-pro** executes dependent tasks sequentially

**Key Integration Points:**
- Dependency mapping (planning-pro → sk-parallel-agents-pro)
- Agent dispatch (sk-parallel-agents-pro)
- Task execution (sk-parallel-agents-pro → domain skills)
- Result aggregation (sk-parallel-agents-pro)
- Sequential coordination (sk-parallel-agents-pro → sk-executing-pro)

### Scenario 2: Parallel with Dependencies

**Flow:**
1. **planning-pro** maps dependencies
2. **sk-parallel-agents-pro** executes wave 1 (independent tasks)
3. Domain ***-pro skills** execute wave 1 tasks
4. **sk-parallel-agents-pro** aggregates wave 1 results
5. **sk-parallel-agents-pro** executes wave 2 (now-available tasks)
6. Continue until all waves complete

**Key Integration Points:**
- Dependency mapping (planning-pro)
- Wave execution (sk-parallel-agents-pro)
- Task execution (sk-parallel-agents-pro → domain skills)
- Wave coordination (sk-parallel-agents-pro)

### Scenario 3: Agent Failure Handling

**Flow:**
1. **sk-parallel-agents-pro** detects agent failure
2. **sk-systematic-debugging-pro** diagnoses issue
3. **sk-parallel-agents-pro** retries or reassigns task
4. Domain ***-pro skills** execute recovered task
5. **sk-parallel-agents-pro** continues with aggregation

**Key Integration Points:**
- Failure detection (sk-parallel-agents-pro)
- Debugging (sk-parallel-agents-pro → sk-systematic-debugging-pro)
- Recovery (sk-parallel-agents-pro)
- Task execution (sk-parallel-agents-pro → domain skills)

## Handoff Protocols

### From planning-pro

**When:** Plan ready for parallel execution
**Input:** Task list with dependencies, parallelization strategy
**Output:** Aggregated execution results
**Protocol:**
- Receive task list
- Receive dependency map
- Receive parallelization strategy
- Dispatch agents
- Aggregate results

### To sk-executing-pro

**When:** Dependent tasks need sequential execution
**Input:** Dependent tasks with dependencies
**Output:** Execution status
**Protocol:**
- Provide dependent tasks
- Provide dependency information
- Receive execution status
- Continue with next wave

### To Domain Skills

**When:** Agent task execution needed
**Input:** Task with technical requirements
**Output:** Task completion
**Protocol:**
- Provide task description
- Provide acceptance criteria
- Receive task completion
- Verify acceptance criteria

### To sk-systematic-debugging-pro

**When:** Agent issue occurs
**Input:** Agent issue details and context
**Output:** Root cause and resolution
**Protocol:**
- Provide issue description
- Provide context and logs
- Receive diagnosis
- Implement resolution

### To sk-feedback-pro

**When:** Execution review needed
**Input:** Execution results and aggregated output
**Output:** Quality assessment
**Protocol:**
- Provide execution results
- Provide aggregated output
- Request quality review
- Receive assessment

## Conflict Resolution

### Conflicts with planning-pro

**Scenario:** Dependency mapping issues during execution

**Resolution:**
- Pause execution
- Communicate dependency issues to planning-pro
- Adjust dependency map
- Resume execution

### Conflicts with sk-executing-pro

**Scenario:** Sequential coordination conflicts

**Resolution:**
- Review sequential execution plan
- Adjust wave structure
- Ensure consistency
- Continue execution

### Conflicts with Domain Skills

**Scenario:** Technical approach issues in agents

**Resolution:**
- Consult with domain skill
- Adjust technical approach
- Re-validate
- Continue execution

## Quality Gates

### Before sk-parallel-agents-pro

- [ ] Plan received from planning-pro
- [ ] Dependencies understood
- [ ] Parallelization strategy defined
- [ ] Resources available

### During sk-parallel-agents-pro

- [ ] Dependencies respected
- [ ] Agents dispatched appropriately
- [ ] Failures handled
- [ ] Results aggregated correctly

### After sk-parallel-agents-pro

- [ ] Results aggregated
- [ ] Dependent tasks handed to sk-executing-pro
- [ ] Execution reviewed with sk-feedback-pro
- [ ] Lessons learned documented
