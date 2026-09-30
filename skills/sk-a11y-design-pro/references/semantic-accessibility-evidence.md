# Semantic accessibility evidence matrix

| Area | Expected evidence |
|---|---|
| Semantics | Native element or justified ARIA role/name/value/state mapping |
| Keyboard | Tab order, activation keys, escape behavior, focus entry/return, no trap |
| Screen reader | Landmark/heading structure, labels, status/live-region announcements, meaningful order |
| Contrast | Text, controls, focus indicator, disabled/state colors checked against target level |
| Zoom/reflow | 200% zoom and narrow reflow preserve task completion without hidden content |
| Forms | Label, instruction, required/error association, autocomplete and recovery |
| Dynamic widgets | Dialog, menu, tabs, accordion, carousel and combobox follow APG behavior |
| Preferences | Reduced motion, high contrast, forced colors, RTL and text scaling are respected |
| Automation | axe/Lighthouse findings triaged; critical violations block release |

Record assistive technology/browser versions, violation severity, reproduction steps, affected users, remediation owner, and manual-test evidence. Automated scans supplement, not replace, keyboard and screen-reader review.
