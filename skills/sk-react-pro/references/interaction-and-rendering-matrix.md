# React interaction and rendering verification matrix

| Scenario | Expected evidence |
|---|---|
| Initial/loading/error/success | State transitions are deterministic and recoverable |
| Form input/submit | Labels, validation, pending state, duplicate-submit prevention, and focus are correct |
| Modal/menu/popover | Portal/stacking, focus entry/return, Escape, outside click, and keyboard behavior work |
| Async race/unmount | Abort or sequence guard prevents stale results and state updates after unmount |
| Strict Mode | Effects are idempotent; no duplicate subscription, fetch, or side effect |
| SSR/hydration | Server/client markup and locale/time-dependent values do not mismatch |
| Large list | Keys are stable; virtualization/memoization is justified by measurement |
| Responsive/a11y | Semantic HTML, keyboard flow, reduced motion, and narrow viewport remain usable |

Evidence may combine component tests, interaction tests, browser checks, and profiler traces. Do not use memoization or client state to mask an unclear ownership boundary; hand Next-specific RSC/cache concerns to `sk-nextjs-pro`.
