# Mobile interaction and platform matrix

| Concern | Expected evidence |
|---|---|
| Touch target | Primary controls meet platform target guidance with adequate spacing |
| Safe area | Notches, home indicators, cutouts, keyboard, and landscape are handled |
| Navigation | Back behavior, deep link, modal/sheet dismissal, and restoration are explicit |
| Input | Keyboard type, focus, scroll-to-field, validation, and submit behavior work |
| Permission | Rationale, denial, retry/settings path, and degraded mode are clear |
| Offline/error | Connectivity loss, retry, stale data, and unsaved work are recoverable |
| Dynamic type | Text scales without clipping or hiding essential actions |
| Reduce motion/RTL | Preferences and direction preserve comprehension and task completion |
| Tablet/foldable | Width changes, split panes, posture/orientation, and pointer input are considered |

Test at least one small phone, large phone, tablet, landscape, keyboard-visible, and screen-reader configuration. Hand implementation details to React Native/Flutter/native skills while preserving this UX contract.
