---
name: course-quality-review
description: Review alignment and production readiness across needs analysis, SME scope, learning design, assessments, storyboards, and interactive outputs. Use at review gates or after material changes to identify evidence-backed blockers and affected artifacts, without granting human approval.
---

# Cross-stage course quality review

Review supplied artifacts and exact versions against approved decisions. Use the [review contract](references/review-contract.md) for severity, evidence, and reporting. This is a project-local reviewer skill, not an automatically enforced application gate.

## Establish scope

Identify the requested gate: analysis readiness, design/storyboard review, production readiness, or built-output verification. Inventory artifacts, approval records, source access, and tests available. Say what was inspected, executed, and unavailable. Never infer missing evidence from polished wording or a previous approval.

## Review checks

1. **Diagnosis:** confirm evidence supports a training/combined intervention before course production. Distinguish hypotheses, reports, observations, and measured gaps; check comparable units/conditions. Do not reinterpret a mandated content request as proof of training effectiveness.
2. **SME scope:** trace workflow, decision cues, mistakes, exceptions, content selection, and job aids to validated sources. Flag conflicts, invented facts, excluded requirements without owner decisions, and missing non-training dependencies.
3. **Design:** trace gap → task → SMART objective → course-map practice → appropriate assessment evidence. Check prerequisites, time/resources, scaffolding, and actual task demands. One MCQ cannot establish a full conversation or tool-operation skill.

   Inspect theory application in the storyboard against the learning/visual principle references: identify actual retrieval, meaningful variation, reflection, purposeful signaling/contiguity, and any planned spaced follow-up where selected. Theory labels without a learner action or presentation decision are not implementation evidence. Require objective-linked content and flag missing practice/assessment or off-scope content; do not mandate every theory or treat orientation/access controls as needing invented learning objectives.
4. **Assessment:** use `skills/course-assessment-design/SKILL.md` for item/set checks. Verify approved aspects/counts/formats, defensible keys/rubrics, plausible errors, answer clues/leakage, release timing, and opportunity to demonstrate each criterion. Do not treat automated scoring or completion as independent evidence of mastery.
5. **Storyboard:** verify the Rise lesson/block or Storyline slide contract, exact copy, source/asset references, branch destinations, feedback per authored choice, navigation/recovery, and accessibility instructions. Identify unsupported implementation assumptions.
6. **Role-play:** check free learner input, contextual counterpart behavior, no unsolicited suggested replies, learner-requested hints only, private evaluation, and final evidence-based debrief. Completion requires learner exit or sufficient evidence for all criteria; no-opportunity and uncertain judgments do not count as met. Do not expose private rubric content to the counterpart or learner through visible notes/telemetry.
7. **Visual/media:** use `skills/course-visual-design/SKILL.md` for purpose, hierarchy, consistency, readable cues, optional audio, and reduced-motion/access alternatives. Source review alone cannot confirm contrast, keyboard flow, or rendered usability.
8. **Build/tracking, when in scope:** verify version-pinned approved inputs, schema/component validity, assets, runtime errors, branches/retry, keyboard/focus/mobile/reduced motion, actual host behavior, and LRS receipt when test access exists. Missing implementation tests remain not-run. Document static/offline versus live-service dependencies; never expose reusable secrets in course output.
9. **Evaluation and change impact:** confirm Kirkpatrick plan, baseline/source/owner/timing and limits; flag L2 results presented as L3/4 evidence. Identify stale versions and all affected downstream artifacts after changes. Approval of one version does not transfer silently to another.

## Report, do not silently fix

Return an evidence-backed issue log, coverage table, tests/results, unresolved decisions, and readiness recommendation. Propose concrete edits and route facts to the SME, scope/design to the ID, and runtime problems to implementation. Editing is a separate action when requested; do not silently change a policy, key, threshold, or approved artifact while reviewing it.

Use **blocked**, **ready for human review**, or **verification incomplete** as recommendations, never a fabricated human sign-off. Optional improvements do not block progression. Where evidence is insufficient to decide, identify the exact check needed rather than guessing a pass. Learner pilots, expert calibration, and runtime tests provide different evidence; none alone certifies effectiveness or accessibility.
