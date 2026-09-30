# Meta-review evidence and heuristic triage

| Finding class | Evidence | Treatment |
|---|---|---|
| Deterministic failure | Validator/test/link/fence output with file and line | Fix or block merge |
| Structural gap | Missing contract section, metadata or resource path | Create actionable issue with owner |
| Heuristic concern | Generic/vague/redundant content signal | Label as hypothesis; sample and review manually |
| Staleness | Version/date mismatch against official source | Verify via `sk-web-research-pro` before changing |
| Duplicate boundary | Two skills claim the same artifact/trigger | Compare canonical ownership and add routing note |
| Automation limit | Tool cannot judge domain correctness or visual quality | State limitation; require focused human/domain review |

Review output should separate facts from interpretation, map each finding to a file/section, include severity and confidence, and avoid turning a heuristic score into a hard failure.
