# Evaluation, tracking, and delivery

Status: planned specification. No LRS integration, telemetry pipeline, or LMS package export is claimed as implemented.

## Storyboard-first delivery

1. Generate a Storyline slide storyboard or Rise linear lesson/block storyboard from the approved design brief.
2. Let the ID review and comment against stable slide/block IDs; preserve feedback and revision history.
3. Revise and record the ID's explicit approval against a specific storyboard version.
4. Generate scene specifications and embeddable interactions from that approved version. Unapproved drafts may have clearly labeled previews, not approved build artifacts.
5. Deliver HTML/assets, any separately verified host adapter, installation instructions, and QA evidence. Record the source storyboard version for every artifact.

If objectives, facts, rubric, or interactions change, flag the affected storyboard and artifacts for review; never silently replace approved outputs. The ID assembles the surrounding course in the chosen authoring tool in the first release.

A complete course package would instead include the assembled course structure, lessons, navigation, assets, assessments, completion rules, and a tested LMS launch/tracking package. This is a possible later scope, not the first-release deliverable. xAPI statements alone do not provide that launch/package contract.

## Kirkpatrick evaluation plan

Use [Kirkpatrick's four levels](https://www.kirkpatrickpartners.com/the-kirkpatrick-model/), planning backward from Level 4 to required workplace behavior, learning, and learner experience. Do not defer evaluation design until after production.

| Level | Question | Evidence candidates | Limits |
|---|---|---|---|
| 1: Reaction | Is the experience relevant, engaging, and useful to learners? | Relevance questions, perceived applicability, learner comments | Click counts and time spent do not establish positive reaction |
| 2: Learning | Can learners demonstrate the intended knowledge and skills? | Aligned assessment, scenario decisions, criterion-level role-play evidence; baseline comparison where appropriate | Simulation performance is not workplace transfer; validate AI judgment with ID/SME-labeled examples |
| 3: Behavior | Are learners applying the critical behaviors at work? | Planned observations, work samples, manager follow-up, appropriate operational workflow evidence | Requires post-training workplace evidence and opportunities/support to apply learning |
| 4: Results | Are the intended organizational outcomes changing? | Original performance measures, baseline and follow-up, business data and contextual changes | Improvement alone does not prove training caused it |

For each selected measure, confirm with the ID/stakeholders: linked gap/objective, definition, source, baseline, target if appropriate, collection timing, owner, access, and analysis limitations. Leave unsupported fields pending. All four levels belong in the plan; missing external Level 3/4 data is reported as unavailable, never inferred from course completion.

## xAPI instrumentation

Use xAPI as the learning-event transport to a Learning Record Store (LRS). See [ADL's xAPI resources](https://adlnet.github.io/) and [statement data specification](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md). Select and document the supported xAPI version/profile during implementation.

Maintain an internal event vocabulary mapped to validated xAPI statements. Candidate events: activity started, decision submitted, hint requested, attempt retried, simulation ended, debrief viewed, and criterion evaluated. These are design labels, not yet approved verb IRIs. Finalize stable activity/verb identifiers and extensions before integration.

Record meaningful events rather than every click. Include event ID, learner identifier, activity and session/registration, event timestamp, attempt, course/scenario/storyboard/rubric versions, objective/criterion references, and applicable result data. Distinguish learner-submitted actions from system-generated criterion evaluations. Record simulation ending reason separately from criterion attainment: an early exit or a viewed debrief is not mastery. Avoid a default success=true for activity completion.

Background evaluation may send private records while practice continues, but learner-facing evaluation remains hidden until the final debrief. Never expose hidden rubric or counterpart information through learner-accessible telemetry endpoints.

## Integration and data decisions

- Confirm LRS endpoint, deployment/identity model, authentication, and host adapter behavior. Do not embed reusable LRS or model-service secrets in downloaded HTML; use a backend relay or appropriately scoped short-lived authorization.
- Define who can see individual records versus aggregates, retention/deletion rules, and what learners are told. Raw role-play transcripts are not sent by default; decide their storage separately from event summaries and references.
- Queue eligible unsent events, retry with stable IDs to avoid duplicate records, and surface delivery failure rather than claiming successful tracking. Scope local persistence to the learner/session and deployment policy.
- Test event validation, identity mapping, resume/retry, duplicate handling, and actual LRS receipt in the intended host. Standalone success does not establish Rise/LMS integration.
- Keep a mock recording mode for local demonstrations. Static offline activities can queue records under the approved persistence policy; live AI conversation still requires connectivity.

Reports should distinguish telemetry delivery, learner experience, demonstrated learning, workplace behavior, and business outcomes. xAPI supports collecting and connecting records; it does not supply an evaluation dashboard, permissions model, or causal analysis by itself.
