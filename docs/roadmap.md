# Roadmap and iteration record

Last updated: 2026-10-27. This is the maintained next-steps list. Milestones describe intended work, not implemented capabilities or release dates. Update status and evidence as each small increment is completed.

## V1 baseline accepted for further iteration

The ID-facing review slice is accepted as a working V1 baseline, not a production release or endorsement of the current visual theme.

- Source text and TXT/Markdown/PDF/DOCX upload; page-referenced PDF Markdown with extraction limitations.
- Readable editable course, objective, teaching-content, interaction, and assessment fields; advanced read-only JSON.
- Detailed authored built-in example with concrete situations and proposed objective-linked assessment items.
- Shared or per-option feedback; written tasks with criteria and model comparison, not automatic grading.
- New draft versions, feedback notes, local persistence/reopening, explicit named approval, and approved-version HTML prototype.
- Project-local design skills and templates. Generation is still deterministic mock; custom sources do not yet receive a full AI-authored storyboard.

Existing limitations remain visible: skills are not automatically orchestrated, review identity is not authenticated, detailed storyboard activities are not all executable in the HTML renderer, and host/LMS/LRS behavior is not verified. The earlier enhanced UI direction was rejected. Preserve its lessons, not its styling as a requirement.

## Ordered increments

| ID | Status | Increment | Done when |
|---|---|---|---|
| N1 | In progress | Publish the V1 checkpoint to GitHub | Review the full diff, keep public content English, exclude uploads/local records/credentials, reconcile README claims, run relevant checks, then commit and push. Record the resulting commit; do not claim release before it exists. |
| N2 | Planned | Build one complete guided interaction | Select one approved objective and concrete case. Implement learner action → response → consequence → explanatory feedback → retry using a structured specification and reusable component. Validate keyboard, mobile, reduced motion, and actual behavior; obtain ID review of the representative screen before expansion. |
| N3 | Planned | Formalize structured design contracts | Validate objective links, assessment types/counts/coverage, source references, and versioned artifact schemas. Report missing evidence without equating item count with full skill coverage; provide migration/legacy handling. |
| N4 | Planned | Connect AI-assisted storyboard generation | Load relevant skills/references and approved inputs, generate schema-validated output, retain source provenance and unknowns, and support Rise lesson/block versus Storyline slide specifications. Test custom synthetic sources. Keep mock mode explicit. |
| N5 | Planned | Connect ID-feedback revision | Target version and slide/block/item references, propose a changed draft, show differences, preserve approved history, and require renewed approval for material changes. Feedback must not silently overwrite content. |
| N6 | Planned | Connect upstream analysis and design | Provide needs-analysis/learner-brief inputs, SME synthesis and content selection, SMART objectives, and course-map review in the UI. Enforce training/combined approval before production; support non-training and insufficient-evidence outcomes. |
| N7 | Planned | Add open AI role-play | Use configurable synthetic facts, counterpart/private evaluator/separate hint roles, free learner input, end-only personalized debrief, and the agreed learner-exit/all-criteria-met endings. Calibrate with ID/SME-labeled conversations and validate a second context without core-code changes. |
| N8 | Planned | Validate embedding and tracking | Verify one actual Rise or Storyline integration path, package local static assets, define xAPI profile/events and LRS authorization, test receipt/retry/identity, and preserve private assessment data. Document live-service/offline boundaries. |
| N9 | Planned | Pilot and evaluate | Collect relevant learner usability and Level 2 evidence, plan/collect available Kirkpatrick Level 3/4 data with owners, compare with the original gap, and turn findings into focused revisions. Do not infer workplace impact from completion or visual preference. |

Dependencies: N4 depends on validated contracts from N3; N6 supplies the full upstream approvals for eventual production use. N2 and N4 may use explicitly reviewed synthetic design fixtures before upstream UI integration; this does not constitute real diagnostic approval. N7 requires model/service and rubric validation; N8 requires actual host/LRS access. Reorder increments only with the reason recorded here; do not expand all tracks simultaneously.

## Deferred decisions and guardrails

- Revisit Darwin-inspired paired output tests when an actual skill failure warrants iteration. Do not install it or automatically rewrite skills now. Use fixed cases, held-out variants, recorded evidence, and human judgment rather than an absolute score alone.
- Reassess huashu-design animation components when a specific teaching animation needs timelines/seeking. Current dependency-free prototype is original; no upstream engine is installed. Preserve license notices if code is later reused.
- Keep series navigation/themes consistent; animation/audio are optional and purposeful. Hints remain hidden until requested.
- Full assembled LMS-ready course packages, voice/multiple-character simulation, OCR/layout-aware PDF conversion, and authenticated multi-user review are outside the accepted V1 slice; prioritize only after a concrete need is established.

## Update protocol

For each increment, record the implemented behavior, verification performed, material limitations, ID feedback, and the next smallest action. Mark complete only when its done criteria are met. Preserve approved content versions and keep planning separate from implementation claims.

| Date | Milestone | Decision / evidence | Next action |
|---|---|---|---|
| 2026-10-27 | V1 | User accepted the review slice as a V1 baseline; mock/renderer limitations remain. | Prepare GitHub checkpoint (N1). |
| 2026-10-27 | Planning | Record gradual next steps before further interaction expansion. | Maintain this roadmap alongside each implementation increment. |

V1 checkpoint preparation: 11 unit tests, 8 skill validations, relative documentation links, English-only checks, and credential-pattern checks passed. Local project records and machine-specific VS Code settings are excluded. Commit/push completion must be confirmed from Git before marking N1 complete.
