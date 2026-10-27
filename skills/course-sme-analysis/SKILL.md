---
name: course-sme-analysis
description: Prepare and synthesize SME workflow interviews into decision maps, common mistakes, exceptions, scenario seeds, content selection, and job aid candidates. Use after a training or combined intervention is confirmed and before finalizing learning objectives.
---

# SME workflow and content analysis

Turn expert knowledge into a reviewable account of what performers do, notice, decide, and need at work. Use the [interview and synthesis template](references/interview-template.md). Repository paths below are project-relative. Outputs are English unless explicitly requested otherwise; this skill is not yet automatically executed by the app.

## Inputs and boundary

Read the approved diagnosis, gap/task/source IDs, learner brief, environment constraints, and non-training dependencies. Reuse known answers. If intervention approval is missing, return the missing decision to `skills/course-needs-analysis/SKILL.md`; an exploratory interview outline may be drafted, but do not call downstream content approved.

Accept ID notes, transcripts, source documents, and work samples. Plan interviews for a human to conduct or ask the ID questions in chat; do not contact an SME, schedule a meeting, or record anyone without authorization. Identify facts the SME can validate and the person who resolves policy conflicts. Never reproduce confidential employer material in this portfolio repository.

## Interview method

1. Prepare a short gap-specific agenda and focused questions from the template. Start with one representative task or incident rather than requesting everything the SME knows. Adapt depth to available time and risk; do not require every question when evidence is already sufficient.
2. Reconstruct the workflow from trigger through successful completion, including inputs, tools, handoffs, conditions, permissions, and observable outputs. Distinguish prescribed workflow from observed workarounds.
3. Revisit a concrete incident chronologically. Ask what information was available at each decision, what the performer noticed, which options were plausible then, and why. Do not insert hindsight knowledge into the learner's later scenario.
4. Probe common errors, tempting shortcuts, exceptions, escalation, recovery, and consequences. Ask for an example or observation supporting each “common” mistake; label unverified proposals. Request expert think-aloud or a demonstration when tacit reasoning remains unclear.
5. Separate recall, opinion, approved rules, observed practice, and analyst inference. Seek performer/process-owner corroboration when feasible; an expert's account alone may miss novice difficulties or local conditions. Record disagreements rather than merging them into a fabricated consensus.

## Synthesize and select

Produce a task/decision map and a source-linked claims register before proposing content. Include frequency, difficulty, and consequence evidence where available; do not invent priority scores. Flag rare but high-consequence actions for stakeholder review.

Classify at an actionable granularity:

- **Must-do:** behaviors/decisions needing practice; identify conditions and evidence of good execution.
- **Must-know:** information essential to those actions and not adequately served by available reference support.
- **Look-up:** details best accessed at the point of work. Include locating and using the aid as practice when needed.
- **Cut:** out-of-scope, duplicate, unsupported, or obsolete material, with an explicit reason. Cutting from this course does not authorize deletion of the source or removal of a required record.

A task can require practice and a reference; split its action and supporting detail rather than forcing one label onto both. Do not classify everything as must-know because the SME requests inclusion. Explain the task/gap linkage and ask the ID/SME to resolve scope disagreements. Preserve mandatory requirements and ask the designated owner before excluding them; do not invent compliance obligations.

Identify job aid candidates with point of use, format, access constraints, source/version, maintenance owner, and validation needs. Suggest scenario seeds for a hook, recurring case, decision practice, or later open role-play. Seeds contain a setup, cues, decision, plausible mistakes, consequences, and unresolved facts; they are not automatically approved questions or finalized branches. Fictionalize safely and label synthetic details.

## Failure handling and review

| Trigger | Next action | If unresolved |
|---|---|---|
| SME gives only topic lists | Ask for a recent task/incident and an observable success example | Mark workflow incomplete; do not manufacture task steps |
| Experts or documents conflict | Record both claims with location/version; refer to the designated owner | Keep affected content and scenario facts pending |
| Error or consequence is speculative | Label it proposed and request an example/source | Exclude it from approved assessment keys and factual claims |
| A process/tool barrier emerges | Return the evidence to needs analysis and reconsider dependencies/intervention | Do not assume more instruction will fix it |
| Time or source access is insufficient | Prioritize consequential uncertainties and deliver a bounded draft | List follow-up questions, owners, and blocked outputs |

Return the synthesis to the SME for factual validation and the ID for scope decisions, tied to a version and actual review record. No fabricated sign-off. Final SMART objectives follow confirmed workflow/content scope using `skills/course-learning-design/SKILL.md`; questions follow `skills/course-assessment-design/SKILL.md`. Scope or fact revisions flag affected downstream designs for review.

## Completion

The handoff includes the workflow/decision map, claim/source register, prioritized task rationale, four-category content table, job aid candidates, cut list with reasons, scenario seeds, and unresolved questions. Each included item links to an approved gap/task or a separately confirmed requirement. Unknowns remain visible. A polished summary is not proof the SME agreed with it.
