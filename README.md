# AI Course Builder

An AI-assisted course design prototype that turns source material into a structured storyboard and a lightweight interactive learning experience.

> **Portfolio disclaimer:** This is an independently built portfolio project inspired by common instructional-design workflow challenges. It does not contain or reproduce proprietary employer code, data, prompts, internal systems, business rules, or confidential information.

## Why this project

Instructional designers often spend substantial time converting raw source material into:
- learning objectives,
- a coherent course structure,
- storyboard content,
- knowledge checks,
- and interactive experiences.

This project explores how AI can reduce that manual effort while keeping the instructional designer in control of the final learning experience.

## MVP workflow

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
├── data/
│   └── sample_source.md
└── src/
    ├── __init__.py
    ├── storyboard.py
    └── html_generator.py
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
streamlit run app.py
```

## Current MVP

The mock generator creates:
- course title,
- audience,
- learning objectives,
- section sequence,
- key teaching points,
- a knowledge check,
- and a simple interactive HTML experience.

## Next iterations

- Add a real LLM provider
- Support file upload and document chunking
- Add editable storyboard fields
- Add reusable interaction templates
- Add content QA checks
- Add evaluation rubric for generated learning content
- Track time saved and revision effort
- Export storyboard to JSON / Markdown

## Evaluation questions

This project is not only about whether AI can generate content. The more important questions are:

- Does the output reduce design time?
- How much human revision is still required?
- Does the storyboard preserve instructional coherence?
- Are objectives, content, and assessment aligned?
- Which tasks should remain human-owned?
- What quality guardrails are needed before scaling?

## Author

Wei He  
Instructional Design • AI Enablement • Learning Program Management
