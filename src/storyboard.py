from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import List
from pathlib import Path
from copy import deepcopy
from src.sample_storyboard import SECTIONS, KNOWLEDGE_CHECK, ADDITIONAL_ASSESSMENTS


@dataclass
class StoryboardSection:
    title: str
    purpose: str
    key_points: List[str]
    interaction: str


@dataclass
class Storyboard:
    course_title: str
    audience: str
    learning_objectives: List[str]
    sections: List[StoryboardSection]
    knowledge_check: dict
    additional_assessments: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def generate_storyboard(source_text: str, audience: str = "Adult learners") -> Storyboard:
    """Create a deterministic mock storyboard from source text.

    This deliberately avoids calling an external AI provider so the MVP
    can run without API keys. Replace this function later with a provider-
    backed implementation while preserving the same return shape.
    """
    cleaned = " ".join(source_text.split())
    if not cleaned:
        cleaned = "No source content was provided."

    preview = cleaned[:220].rstrip()
    title_seed = preview.split(".")[0][:70].strip() or "AI-Assisted Learning Module"

    sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_source.md"
    is_review_sample = sample_path.exists() and cleaned == " ".join(sample_path.read_text(encoding="utf-8").split())
    objectives = [
        "By the end of the lesson, learning-content reviewers will be able to identify issues in AI-generated learning content using the review criteria.",
        "By the end of the lesson, learning-content reviewers will be able to document required corrections before approving AI-generated content.",
    ] if is_review_sample else [
        "Draft objective pending ID input: specify the observable work behavior this material supports, linked to the confirmed performance gap."
    ]

    sections = [
        StoryboardSection(
            title="Why this matters",
            purpose="Establish relevance and connect the topic to the learner's work.",
            key_points=[
                "Introduce the core problem or opportunity.",
                "Clarify when the learner will use this knowledge.",
            ],
            interaction="Pending source-specific scenario design: the mock cannot infer a validated work situation from this upload. Before approval, the ID must supply or confirm the exact situation, learner-visible facts, task, expected evidence, and feedback. This placeholder is not a ready-to-use assessment.",
        ),
        StoryboardSection(
            title="Core concepts",
            purpose="Explain the essential ideas in a concise, structured sequence.",
            key_points=[
                preview or "Summarize the source material into 2–3 core ideas.",
                "Distinguish must-know concepts from supporting detail.",
            ],
            interaction="Clickable cards that reveal concise explanations and examples.",
        ),
        StoryboardSection(
            title="Apply the learning",
            purpose="Move from recognition to practical application.",
            key_points=[
                "Pending ID/SME input: specify a source-supported incident or explicitly synthetic case, including role, trigger, constraints, and decision cues.",
                "Pending design: write the exact prompt, valid response evidence, plausible mistakes, consequences, and feedback before treating this section as ready to build.",
            ],
            interaction="Incomplete mock specification: no source-specific test situation or answer key has been established. Confirm the target behavior and concrete case before drafting choices or open-response criteria; do not infer learner competence from this outline.",
        ),
    ]

    if is_review_sample:
        sections = [StoryboardSection(**deepcopy(section)) for section in SECTIONS]

    return Storyboard(
        course_title=f"{title_seed}",
        audience=audience,
        learning_objectives=objectives,
        sections=sections,
        additional_assessments=deepcopy(ADDITIONAL_ASSESSMENTS) if is_review_sample else [],
        knowledge_check=deepcopy(KNOWLEDGE_CHECK) if is_review_sample else {
            "question": "Which response best demonstrates application of the key concept?",
            "options": [
                "Repeat the definition without applying it.",
                "Use the concept to select an action in context.",
                "Ignore the source material and rely on preference.",
            ],
            "answer_index": 1,
            "feedback": "Application requires using the concept in context, not only recalling it.",
        },
    )
