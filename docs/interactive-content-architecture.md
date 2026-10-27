# Interactive content architecture

Status: planned design, not an implemented renderer or tested Rise integration.

## Responsibility split

The orchestration agent reads the approved storyboard, objectives, assets, and brand guidance. It selects interaction patterns and registered components, and writes a structured scene specification. A deterministic renderer validates the specification and assembles versioned templates. New behavior is added to the component library with review and tests, not arbitrary generated JavaScript in scene properties.

Keep three content layers: shared engine, abstract interaction patterns, and environment context packs. A separate platform adapter handles host integration; it is not another environment skin. Course facts, task rules, and assessment criteria remain scenario configuration.

## Teaching decision before rendering

Record the objective served, learner action, and reason for each interaction. Distinguish orientation/atmosphere from practice that provides evidence of learning. An animated badge or phone notification becomes practice only if the learner meaningfully acts and receives feedback.

Choose opening mode: none, title card, static scene, or immersive sequence. Consider learner experience, task relevance, refresher versus onboarding purpose, and whether the series already used an immersive opening. Proposed default: immersive opening at most 15 seconds; any exception requires an explicit ID decision. Provide skip and stay/manual-continue controls. Animation and automatic navigation are optional, not indicators of course quality.

## Component contracts

Initial candidates: title card, hotspot tag, work-action feedback, interruption notification, decision with consequences, and countdown toast. The cue engine schedules them; context packs supply environment-specific presentation and props.

Each registered component declares:

- Stable name, version, purpose, when to use/avoid, and allowed platform scopes.
- Typed properties, required fields, defaults, bounds, and asset references.
- Events, state changes, keyboard behavior, focus management, and cleanup/reset behavior.
- Reduced-motion alternative, accessible labels/text, and responsive behavior.
- Required adapter capabilities and a functional fallback when unavailable.
- Component tests and supported runtime/adapter versions.

Reject unknown components/properties, unresolved assets, invalid timing, arbitrary executable properties, and unsupported navigation targets before rendering. Render copy as text or sanitized approved markup. The agent cannot modify library source through a specification.

## Illustrative scene specification

This is a proposed shape, not yet a JSON Schema implementation. Component property names must be finalized with their implementations.

```json
{
  "schema_version": "0.1",
  "scene_id": "intro",
  "objective_ids": ["LO-1"],
  "context_pack": "warehouse",
  "target": {"platform": "rise", "scope": "block"},
  "opening": {"mode": "static_scene", "rationale": "Orient learners to the task environment", "duration_seconds": 10},
  "background": {"type": "image", "asset_id": "warehouse_entry", "motion": "optional_zoom"},
  "controls": {"allow_skip": true, "allow_pause": true, "reduced_motion": "static"},
  "cues": [
    {"id": "title", "at": 4.5, "component": "title_card", "version": "1", "props": {"title": "Before the First Truck", "duration_label": "About 12 minutes"}},
    {"id": "badge_label", "at": 5.5, "component": "hotspot_tag", "version": "1", "props": {"text": "Badge in", "x_percent": 62, "y_percent": 55}}
  ],
  "on_end": {"component": "countdown_toast", "version": "1", "props": {"message": "Continue to the shift briefing", "seconds": 10, "allow_stay": true, "auto_advance": false}},
  "navigation": {"next_scene_id": "briefing", "fallback": "manual_continue"},
  "host_requests": {"full_bleed": false, "hide_lesson_header": false}
}
```

Host requests express desired capabilities, not permission to manipulate the host. A block cannot enable page-wide changes merely by setting a flag. Automatic navigation, if selected by the ID, must use a supported adapter, warn the learner, and offer cancel/stay and manual continue. Do not equate a scene finishing with a learning objective being achieved.

## Pipeline and delivery

Production rendering follows ID approval of a specific storyboard version. Feedback/revisions precede approval; affected outputs return to review after material changes. The first release delivers embeddable components, not a complete assembled LMS course. See [evaluation and tracking](evaluation-and-tracking.md) for planned xAPI events, access, and integration checks.

1. Confirm storyboard, authoring target, available host capabilities, assets, brand, objectives, and opening decision.
2. Generate the scene specification against a JSON Schema and component registry; validate semantic constraints and produce an ID-readable preview.
3. Resolve assets. Supply image/video briefs and prompts when assets are missing; offer a static-image alternative. Do not imply a video has been generated. Confirm media licensing and availability.
4. Render local HTML/CSS/JS from templates. Produce block output separately from any required page adapter. No guessed host selectors, DOM traversal, or navigation routes.
5. Run component and assembled-page browser checks. Actual Rise/export/LMS checks require that environment and must be reported separately.
6. Package the specification, block entry point, assets, runtime/component versions, optional verified page adapter, installation instructions, and test report. Report unresolved dependencies and untested checks explicitly.

Static activities should package fonts, scripts, and media locally and be tested without external network requests. Live AI role-play requires a service connection; offer an authored/static alternative when offline delivery is required. Never ship model API credentials in course assets.

## Rise integration boundary

Rise's official Code Block documentation describes an index.html running in an iframe. Treat block-local rendering and page-level layout/navigation as different capabilities. See [Rise 360: How to Use Code Block](https://www.articulatesupport.com/article/Rise-360-How-to-Use-Code-Block).

Full-screen host layout, hiding lesson headers, and navigating between host lessons require a separately verified integration path. Mighty and export modification are candidate paths from the design proposal, not verified guarantees. Record tool/version, actual selectors or supported APIs, integration method, and verification status. When verification is needed, label it **Needs host/console verification** and provide a block-contained/manual-navigation fallback. Never assume preview hash routes match Rise routes.

## Browser QA plan

Use Playwright or equivalent automation for meaningful runtime behavior:

- Cue visibility and state before/after timestamps, seek backward, pause/resume, replay, and navigation; no duplicated animation loops or stale timers.
- Skip, cancel/stay, manual continue, and any verified automatic navigation.
- No console errors or missing assets; no external requests in the offline static package.
- Tab order, Enter/Space operation, visible focus, hidden elements excluded from focus, and focus after navigation.
- Reduced motion disables programmatic camera/zoom motion as well as CSS transitions; meaningful content remains available.
- Mobile widths, zoom, text overflow, and image/hotspot alignment across aspect ratios.

Automated checks do not establish complete accessibility conformance. Include manual assistive-technology review and host/LMS validation as separate checks, with pass/fail/not-run and evidence in the report.

## Reference prototype observations

The supplied “Rise full-screen intro prototype.html” was inspected as source code, not executed or validated inside Rise. Its comments and labels are reference material, not proof of platform support. It illustrates a timed SVG scene with zoom, title overlay, automatic badge animation, countdown/stay controls, a second view, and a phone notification.

Before adapting the idea into library components:

- Add a direct skip-intro control; the supplied version has playback and timeline controls but no dedicated skip button.
- Replace or locally package its Google Fonts dependency for offline delivery.
- Its reduced-motion CSS shortens transitions but does not stop the JavaScript-driven zoom; provide a static alternative.
- Opacity-hidden controls need visibility/focus handling, not just pointer-event changes.
- Its FakeVideo and hash router are local simulation mechanisms; real media and host navigation need separate implementations and verification.
- Treat the prototype as inspiration. Keep its environment-specific details out of engine logic and do not copy it into the public repository without confirming reuse rights.
