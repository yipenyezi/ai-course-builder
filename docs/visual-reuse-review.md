# Visual component reuse: first source review

Reviewed upstream `assets/animations.jsx` from alchaincyf/huashu-design (master, retrieved 2026-10-27). This is a source review, not a benchmark or browser test of the upstream implementation.

The Stage/Sprite separation, normalized local progress, interpolation, and externally seekable rendering are useful patterns. Direct reuse would bring a React/JSX dependency and assumptions that do not match our initial embedded activity:

- Stage uses fixed viewport positioning and a 1920×1080 default canvas, scaling against the browser window rather than a component container.
- Its scrubber is a mouse-driven div without a keyboard slider contract.
- The animation loop has no built-in reduced-motion policy. Non-loop playback holds the final frame but continues requesting frames.
- Recording globals and fixed controls are oriented toward animation/video preview, not multiple independently embedded learning activities.

Decision: do not vendor this engine yet. Use its separation-of-concerns ideas while validating our own small, dependency-free interaction. Reassess timeline reuse when we actually need seeking and synchronized media. No upstream code or assets were copied into the prototype; any future substantial reuse must retain the MIT notice.

References: [animation source](https://github.com/alchaincyf/huashu-design/blob/master/assets/animations.jsx), [license](https://github.com/alchaincyf/huashu-design/blob/master/LICENSE).

## Comparison preview

Update: the user rejected the enhanced direction. Its variant controls and enhanced layouts have been removed. The existing filename is retained for link compatibility; the file now contains only unapproved guided practice. The historical comparison description below records the earlier experiment, not current functionality. Do not use this styling as the approved course theme. Apply the project-local visual design skill to the next representative layout and purposeful-animation exploration.

Open `prototypes/clearlake-comparison.html` locally in a browser. The same authored choices and feedback appear in both variants. Enhanced mode adds a customer-workspace presentation and optional short entry motion. It adds no new learning decisions. Audio and external assets are absent; reduced-motion CSS overrides animation.

ID controls change presentation only. Settings and feedback can be downloaded as JSON for later project integration; no browser preference is treated as an approved project artifact. The preview does not use an AI service, LRS, or the production review gates.

Review task clarity, consequence/feedback comprehension, distraction, keyboard flow, narrow-screen layout, and ease of ID modification. Do not infer retention or workplace transfer from visual preference.

Verification status: source reviewed; browser interaction, screenshots, accessibility, and Rise/LMS integration have not yet been verified. This is an isolated unapproved preview, not production output from the conditional ClearLake design.
