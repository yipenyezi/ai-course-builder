# Project data and review workflow

The first workflow module is `src/project.py`. It is independent of the existing Streamlit prototype; the UI does not yet use these gates. Content is currently an extensible dictionary, not a fully validated instructional schema.

One controller can use skills to prepare five versioned artifacts:

| Stage | Content | Human decision |
|---|---|---|
| diagnosis | Learner brief, evidence, gaps, causes, intervention and evaluation baseline | Confirm evidence and intervention |
| sme_scope | Interview notes, workflow, content selection and job aids | Confirm facts and scope |
| design | SMART objectives, course map, scenarios, assessment brief, rubric, Kirkpatrick plan | Confirm alignment and feasible standards |
| storyboard | Rise lesson/blocks or Storyline slides and build details | ID feedback, revision and explicit approval |
| interaction_spec | Component specification and asset/adapter requirements | Approve build inputs |

States: `draft → in_review → approved` or `changes_requested`. Revisions produce new drafts while preserving content snapshots and review records. Upstream revision marks downstream current artifacts `needs_review`; they need a new revision based on current approved inputs. Build eligibility requires approved current inputs through the interaction specification.

Only `training` and `combined` intervention decisions allow downstream course design. `non_training` and `insufficient_evidence` remain valid diagnostic outcomes. Content completeness, SMART checks, source validation, identity/authorization, persistence and schema migrations still need implementation. A supplied reviewer string is an audit field, not authentication; this module is not a production authorization boundary. No agent may invent a human approval.

The [ClearLake example](../data/clearlake_design_example.json) is deliberately unapproved. It demonstrates references from evidence through a draft storyboard without claiming diagnosis is proven. Conditional downstream drafts are illustrative reference material, not artifacts admitted past the runtime approval gates. Missing evidence, design blocks, and confirmation requirements remain visible. Correct next step: review the example and validate diagnosis, not build it as an approved course.

Run the workflow checks with `.venv/bin/python -m unittest discover -s tests`.

## ID feedback and revision previews

Feedback is associated with the artifact version and relevant slide/block/component IDs. A future **Generate revision preview** action should propose changes and create a new draft, preserving the approved source version. The ID compares, revises, and explicitly approves the new version. Changes to objectives, criteria, or scenario facts require renewed review of affected artifacts. Downloading feedback is not approval, and collecting feedback does not imply automatic changes.

The standalone guided-practice preview currently collects and exports feedback only; it has no AI revision service or project-state connection. The enhanced variant was rejected and removed; the remaining visual direction is unapproved. Discovery guidance is hidden by default and appears only when the learner requests a hint. Retrying hides it again; selecting an answer never reveals it automatically. All preview controls are unapproved design settings.
