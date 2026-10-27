# AI Course Builder

An AI-assisted instructional design prototype. The current MVP turns source material into a structured storyboard and a lightweight interactive learning experience. The planned workflow starts with evidence of a performance problem and determines whether training is an appropriate intervention before designing a course.

> **Portfolio disclaimer:** This is an independently built portfolio project inspired by common instructional-design workflow challenges. It does not contain or reproduce proprietary employer code, data, prompts, internal systems, business rules, or confidential information.

## Why this project

Instructional designers often spend substantial time converting raw source material into:
- learning objectives,
- a coherent course structure,
- storyboard content,
- knowledge checks,
- and interactive experiences.

This project explores how AI can reduce that manual effort while keeping the instructional designer in control of diagnosis, design decisions, and the final learning experience.

## Design direction

Start with the project-local [needs analysis skill](skills/course-needs-analysis/SKILL.md) and its [guided input and decision brief](skills/course-needs-analysis/references/analysis-template.md). They consolidate the learner brief, five analysis lenses, evidence/cause investigation, and training/non-training decision before downstream design. Skill execution and these inputs are not yet integrated into the app.

The guiding workflow is:

**Business problem → Data evidence → Performance gaps → Root causes → Intervention decision → SME workflow interview → Content selection → SMART learning objectives → Scenario and assessment design → Storyboard → Build and evaluation**

- Define expected performance and compare it with actual performance using evidence in comparable units and contexts.
- Identify gaps at the task level. Record the source, scope, and limitations of the evidence; missing data remains unknown.
- Investigate possible causes, including knowledge and skills, information, tools, processes, resources, and incentives. Distinguish supported causes from hypotheses that still need validation.
- Recommend training, non-training changes, a combination, or further investigation. A performance gap does not automatically justify a course.
- When training content is needed, interview the SME about incidents, workflow, decision points, common mistakes, and exceptions. Capture scenario seeds and validate any assumptions against the source material.
- Select content before finalizing objectives: classify it as must-do, must-know, look-up, or cut, identify job aid candidates, and record reasons for exclusions. The ID and SME confirm scope.
- Derive SMART learning objectives only from the knowledge or skill gaps that training can address and the confirmed workflow and scope. Make them specific, measurable, achievable, relevant, and time-bound, with realistic conditions and approved standards. Trace each objective to its gap, task, and supporting evidence; do not invent thresholds or deadlines.
- Align practice and assessment with those objectives, and plan how to check workplace performance against the original gap. Improved results alone do not establish that training caused the change.

Data analysis and cause investigation may run together and lead to revisions. AI assists with analysis and drafts; the designer and relevant stakeholders validate the evidence and approve decisions.

This diagnostic workflow is **planned, not implemented in the current MVP**. The current source-to-course workflow below remains available as a prototype.

See the [course design template](docs/course-design-template.md) for the SME interview, content selection, SMART checks, scenario planning, tool-specific storyboard, and assessment confirmation requirements.

## Planned interactive learning framework

### Skills organized by ADDIE

Use the [ADDIE-ordered skill index](skills/README.md) as the workflow entry point:

| ADDIE phase | Skills / work |
|---|---|
| Analysis | Optional PDF source preparation → needs analysis → SME workflow and content selection |
| Design | Learning objectives/course map → assessment design → visual/media design → detailed storyboard, with iteration |
| Development | Approved specifications, component rendering, visual/runtime QA (production renderer planned) |
| Implementation | Packaging, embedding, host validation, learner access and tracking (planned) |
| Evaluation | Cross-stage quality review plus Kirkpatrick evaluation planning and evidence collection |

QA and evaluation planning run throughout the process. Folder names stay stable; this navigation order does not imply automated skill execution. The earlier enhanced visual direction was rejected, and the guided-practice prototype remains unapproved for visual design.

The intended differentiator is executable work practice: learners perform an action, receive a realistic response, make decisions, and see consequences. Interaction choices must serve the learning objective.

The planned architecture has three reusable layers:

1. **Core engine:** cue timelines, title cards, optional transitions and countdowns, navigation, shared CSS/JS, accessibility, and learner controls.
2. **Interaction patterns:** enter a work environment, perform an action and receive feedback, respond to an interruption, make a decision, and reveal consequences.
3. **Context packs:** environment-specific interfaces and props, selected with a field such as `context_pack: contact_center`. Spatial, screen, and dialogue interactions can be combined. Course-specific facts and business rules remain separate from the environment pack.

The designer decides whether an immersive opening or animation supports the task. Brief refreshers may open directly with a title card; a course series need not repeat its immersive introduction. Support skipping introductions and reduced motion.

The orchestration agent produces a structured scene specification; a versioned component library validates it and renders the code. The agent selects registered components and supplies parameters rather than rewriting their implementation. Platform adapters keep block-contained behavior separate from page-level integration. See the [interactive content architecture](docs/interactive-content-architecture.md) for the planned pipeline, component contracts, testing, and packaging.

### Configurable AI role-play

Role-play is a planned interaction mode configured by instructional designers (IDs), rather than a fixed sales application. IDs supply materials through guided templates; AI proposes a scenario and rubric, asks about missing information, and the ID reviews the result before use.

- The AI counterpart stays in character throughout the simulation.
- Earlier sales practice may use fixed-choice scenarios. Later AI role-play is fully free-form: no answer choices or suggested replies; the counterpart responds to actual learner input, and the final feedback cites it.
- Assessment runs privately in the background; learners see formal evaluation only in the final debrief.
- Learners may explicitly request hints through a separate coach interface. Hints do not appear as statements from the counterpart.
- A session ends when the learner chooses to finish, or when all configured criteria are met with sufficient evidence. Automatic completion follows a coherent closing response from the counterpart.
- Unobserved criteria do not count as met. The scenario must provide an opportunity to demonstrate every criterion used for automatic completion.
- The debrief uses the complete interaction record and cites evidence for its judgments. Hint use is recorded without an automatic penalty.

The first planned example is a synthetic sales discovery conversation for ClearLake, a fictional data platform. Its product facts, customer information, and rubric are configuration, not engine logic. A second, different scenario should work through configuration alone to check reusability.

See the [ID scenario template](docs/role-play-id-template.md) and [criteria template](docs/role-play-criteria-template.md). These are design specifications; AI role-play and the layered engine are not implemented in the current MVP.

### Scenario-based learning and authoring outputs

Courses also support authored scenarios without a live AI counterpart: a problem-based opening hook, a case threaded through the course, decision practice, and scenario-based assessment. Use SME-validated mistakes, meaningful branches and consequences, and explanatory feedback per choice. Keep these feedback rules separate from AI role-play, whose formal debrief remains at the end.

Confirm the authoring tool before generating the storyboard. For Storyline, deliver slide-by-slide text, actionable visual/image descriptions, interaction behavior, narration, and accessibility notes. For Rise, use a linear lesson-and-block storyboard in reading order, with content, media descriptions, interactions, and accessibility notes; slide-by-slide formatting is not required. Confirm objective aspects, question counts, scenario use, and feedback timing with the ID before writing assessment items. Avoid answer-length and position patterns that reveal the correct choice.

## Current source-to-course workflow

### Planned first-release delivery

Deliver the tool-specific storyboard first. The ID reviews it, submits feedback, and revises it with AI assistance. Generate embeddable interactions only from an explicitly approved storyboard version; material later changes require review of affected outputs. Deliver component assets, installation instructions, and QA evidence. A complete LMS-ready course package is outside this first-release scope.

Evaluation planning uses Kirkpatrick's four levels, working backward from intended results. Planned xAPI instrumentation sends meaningful learning events to an LRS; it does not by itself measure workplace transfer or business impact. See the [evaluation and tracking plan](docs/evaluation-and-tracking.md). These capabilities are planned, not implemented.

### Existing prototype

1. Paste or load source material.
2. Generate a structured storyboard.
3. Review and edit the storyboard.
4. Generate a lightweight HTML learning interaction.
5. Preview the result locally.

The first version includes a **mock AI mode**, so it runs without any API key. A model-backed provider can be added later without changing the user workflow.

## What this demonstrates

- Instructional design and curriculum architecture
- AI-enabled workflow design
- Human-in-the-loop review
- Structured content generation
- HTML/CSS/JavaScript learning interaction generation
- Product thinking: problem → prototype → evaluation → iteration

## Project structure

```
ai-course-builder/
├── app.py
├── requirements.txt
├── data/                # Public/synthetic examples
├── docs/                # Design specifications and roadmap
├── skills/              # ADDIE-ordered skill index and references
├── prototypes/          # Unapproved interaction explorations
├── src/                 # Generation, extraction, review, rendering
└── tests/               # Workflow, extraction, and review checks
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/yipenyezi/ai-course-builder.git
cd ai-course-builder
```

### 2. Create a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the app

```bash
.venv/bin/python -m streamlit run app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Current MVP

The latest built-in example proposes four assessment items across two objectives: two decision items for issue identification and two written tasks for documenting corrections. IDs can edit each item and its objective link; written tasks include criteria and model responses for self-comparison, not automatic grading. This proposed count is example-specific and still needs ID confirmation. Legacy single-item drafts remain readable.

The knowledge-check editor supports shared explanation or per-option feedback. Per-option mode requires an explanation for every choice and the HTML prototype displays the selected option's feedback immediately. Existing shared-feedback records remain supported; delayed-release assessment behavior is not implemented yet.

Source inputs support pasted text or one uploaded TXT/Markdown, text-based PDF, or DOCX (10 MB maximum). Select **Load uploaded text**, review the extracted text, then generate. OCR is not supported; PDF reading order and DOCX non-body content may require manual correction. Saved revisions retain the reviewed text and upload filename/hash, not the original binary file.

PDF extraction now produces downloadable page-referenced Markdown, retaining the original extraction separately from ID edits. The [PDF source skill](skills/course-pdf-source/SKILL.md) specifies conversion limits and source handoff; this is text extraction with Markdown page wrappers, not layout-aware table/image reconstruction.

The Streamlit review prototype now supports readable, editable course/objective/section/assessment fields, a read-only advanced JSON view, validated new draft versions, ID feedback notes, explicit named approval, local project snapshots/reopening, and project-history download. HTML is generated only for the current saved approved version; unsaved edits and newer drafts block it. Earlier approvals remain in history. Local snapshots live in Git-ignored `.local_projects/` and can include source material and reviewer names; this is local prototype storage, not authenticated multi-user review.

Generation remains deterministic mock output with generic sections. Project-skill orchestration, upstream workflow gates, full Rise/Storyline formats, AI-assisted feedback revision, and production component renderer are not yet wired into this review slice.

The bundled human-in-the-loop source now has a detailed authored mock with learner copy, worked examples, and activity/build specifications. Custom source material still uses the generic mock outline. The HTML renderer does not implement every described activity; specifications and runtime behavior must be reviewed separately.

The mock generator creates:
- course title,
- audience,
- learning objectives,
- section sequence,
- key teaching points,
- a knowledge check,
- and a simple interactive HTML experience.

## Next steps

The ID review slice is accepted as the V1 baseline. See the maintained [roadmap and iteration record](docs/roadmap.md) for priorities, dependencies, completion criteria, and deferred decisions.

The immediate sequence is to prepare a clean GitHub checkpoint, then implement and review one complete objective-aligned interaction. AI generation, feedback-driven revision, upstream workflow integration, open role-play, and xAPI/LRS validation follow as separate increments. These are planned capabilities, not current features.

## Evaluation questions

This project is not only about whether AI can generate content. The more important questions are:

- Does the output reduce design time?
- Does the diagnosis distinguish training needs from problems requiring other interventions?
- Can each learning objective be traced to a supported performance gap that training can address?
- How much human revision is still required?
- Does the storyboard preserve instructional coherence?
- Are objectives, content, and assessment aligned?
- Which tasks should remain human-owned?
- What quality guardrails are needed before scaling?

## Author

Wei He  
Instructional Design • AI Enablement • Learning Program Management
