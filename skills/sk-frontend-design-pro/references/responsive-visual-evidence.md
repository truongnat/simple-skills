# Responsive visual evidence matrix

Treat visual direction as a system that must survive content, viewport, and preference changes. Record target widths, content priority, typography scale, density, motion policy, and known trade-offs.

| Scenario | Expected evidence |
|---|---|
| Narrow mobile viewport | No horizontal overflow; hierarchy and primary action remain clear |
| Wide desktop viewport | Content measure, whitespace, and focal point remain intentional |
| Long/wrapped content | Labels, cards, tables, and buttons do not clip or overlap |
| Large text/zoom | Layout remains usable at 200% zoom or declared limitation is addressed |
| Dark/high-contrast theme | Semantic colors preserve contrast and state distinction |
| Reduced motion | Non-essential transitions are removed or shortened without losing state feedback |
| Loading/empty/error state | State has visual hierarchy, actionable recovery, and accessible announcement |
| RTL/localization | Direction, text expansion, icons, and alignment remain correct |

Verify representative screenshots or review captures at mobile, tablet, desktop, long-content, and preference variants. Aesthetic quality is evidence-based when hierarchy, contrast, interaction state, and content resilience are all reviewed.
