---
name: course-storyboard
description: Generate or revise ID-reviewable Rise lesson/block or Storyline slide storyboards from approved course design. Use for exact learner copy, media briefs, interactions, accessibility notes, traceability, and versioned feedback before production.
---

# Tool-specific course storyboard

Use the repository's `docs/course-design-template.md`, section 7, as the format contract; do not duplicate or replace it with a generic slide deck. Use `docs/project-workflow.md` for review/version rules. Paths are repository-relative. This skill guides work; it is not yet invoked by the app.

## Confirm inputs

Read the approved diagnosis, SME scope, SMART objectives, course map, scenario plan, assessment brief/items, learner/environment constraints, and source versions. Confirm authoring tool, output format, target duration, narration, accessibility, and any approved visual direction. Reuse confirmed decisions.

Missing inputs may support an explicitly conditional draft with blocked fields, not a production-ready storyboard. Resolve factual conflicts with the SME/source owner. New objectives, unapproved assessment counts, or unsupported policy must not be silently introduced to fill gaps.

## Compose

Read `skills/course-learning-design/references/principles.md` and `skills/course-visual-design/references/principles.md` before drafting. Apply the supplied action-mapping, retrieval, spacing, variation/interleaving, generation, reflection, and multimedia principles where justified by the approved learner/task analysis. Record their concrete implementation, not just theory names. Do not force every principle into every lesson or invent a reinforcement schedule without ID confirmation.

For each slide/block, identify its approved objective/aspect and explain how the content or learner action supports it. Orientation and navigation may instead have an explicit access/orientation purpose. Flag content that supports neither; propose cutting it, moving it to a job aid, or seeking a scope decision rather than adding a new objective to justify it. Maintain a coverage table linking objective → essential explanation/model → practice → assessment → slide/block IDs, including evidence limits and missing coverage.

Translate theory into observable storyboard decisions: practice the actual work action; retain only supporting information; invite recall or an attempt before revealing a model when appropriate; vary relevant cases and revisit learning across approved intervals; elicit reasoning/reflection; place labels next to their visuals, signal essential cues, remove extraneous media, and segment complex demonstrations. Preserve captions/transcripts and justified text access rather than treating redundancy as an absolute ban. Keep solutions hidden until the approved feedback point. A click-to-reveal, attractive animation, or rewritten definition alone is not evidence of application.

1. Preserve the approved learning sequence and stable objective/task/content/assessment IDs. Assign stable slide or lesson/block IDs, including branch/layer IDs where necessary. Map orientation/navigation to an explicit purpose rather than inventing a learning objective for every control.
2. For **Storyline**, write slide-by-slide exact copy and media descriptions, narration when used, learner actions, triggers/conditions, state/layer/variable changes, feedback, destinations, retries, and accessibility notes.
3. For **Rise**, write a linear course → lesson → ordered-block script. Include exact headings/text/instructions, media briefs, proposed block purpose/type, interactions and local scenario paths, feedback, progression, and accessibility. Do not force slide timing or Storyline implementation concepts onto Rise.
4. Make image briefs actionable: subject, setting, action, composition, important cues, style/continuity, placement/aspect ratio. Separate the generation brief from alt text. Keep facts and decision cues faithful to approved sources; mark proposed fictional details. A prompt is not a delivered asset.
5. Apply `skills/course-visual-design/SKILL.md` for hierarchy, multimedia, and purposeful motion. Include a reason and accessible/static equivalent for motion. Use the approved theme consistently. Preview representative layouts without treating an unapproved visual exploration as approval to build the entire course.
6. Preserve authored choice consequences and explanations with agreed release timing. Open AI role-play has no answer choices or suggested responses; hints are requested through a separate coach, evaluation is private, and personalized debrief follows completion. Storyboard role-play screens and configuration references without scripting the learner's answers or promising deterministic AI dialogue.
7. Distinguish native-tool proposals, embedded components, and host/page integration. Flag unverified capabilities and assets; do not invent selectors, APIs, routes, or export support. Provide a feasible fallback for ID review.

## Review and revisions

Teaching content must include the actual learner-facing explanation, relevant example, and visual/media brief, not only topic names or directions such as “introduce the concept.” Interaction descriptions must identify initial state, exact prompt/instructions, input/actions, system response and state/branch changes, feedback for each authored choice or the open-response review mechanism, retry/recovery, completion, and accessibility. Mark unknowns for ID/SME resolution; never imply an open response is automatically graded when only a model comparison exists. Describe what the learner experiences separately from implementation notes. Draft specifications do not prove the HTML renderer implements those interactions.

For every planned scenario/reflection/test situation, write out the actual case: role, trigger, available information, constraints, exact question/task, objective aspect, expected response evidence or acceptable alternatives, and feedback/consequence. List each distinct case separately so the ID can judge coverage and difficulty. “Identify a situation in your work” alone is not a specified test case. An optional learner-generated transfer reflection may supplement authored cases but does not replace planned assessment evidence. Missing source facts must be requested or clearly labeled synthetic proposals, not silently invented.

Deliver the storyboard, coverage/branch map, asset list, unresolved-facts/dependencies list, and versioned review log. Separate learner text from build instructions and hidden keys/rubrics. Estimate time including responses, feedback, and retries; report a mismatch with the design budget instead of compressing the promised skill unrealistically.

Bind ID comments to artifact version and slide/block IDs. Create a new draft for changes; show what changed and which sources/objectives/items are affected. Preserve prior approved output. Return changes in objectives, facts, criteria, or scope to the relevant upstream reviewer; do not disguise them as copy edits. Record the actual ID approval before formal interaction production. Downloading feedback, silence, or an AI recommendation is not approval.

Use `skills/course-quality-review/SKILL.md` for a cross-stage review before handing off an approved version to component-specification work. A storyboard does not establish accessibility conformance, working branches, or LMS integration; those require built-output checks.
