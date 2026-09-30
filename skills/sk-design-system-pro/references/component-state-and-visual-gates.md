# Design-system component state and visual gates

Every reusable component should specify semantic tokens, supported states, content limits, platform scope, and ownership before implementation.

| State/variant | Expected evidence |
|---|---|
| Default/hover/focus/pressed | State is distinguishable without color alone; focus remains visible |
| Disabled/loading | Input is blocked appropriately and progress/status is understandable |
| Error/validation | Message is associated with field/control and recovery is clear |
| Empty/partial data | Layout communicates absence without dead-end interaction |
| Dark/high contrast | Tokens preserve contrast and semantic meaning |
| Long text/localization | Wrapping, truncation, RTL, and translated labels are intentional |
| Dense/compact mode | Target size and readability remain acceptable |
| Responsive/native variant | Differences are documented instead of copied blindly |

Visual regression evidence should compare stable viewport/font/data fixtures, while semantic/a11y checks verify roles, names, keyboard behavior, contrast, and announcements. Review token changes for blast radius across themes and components.
