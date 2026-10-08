from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List


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

    sections = [
        StoryboardSection(
            title="Why this matters",
            purpose="Establish relevance and connect the topic to the learner's work.",
            key_points=[
                "Introduce the core problem or opportunity.",
                "Clarify when the learner will use this knowledge.",
            ],
            interaction="Reflection prompt: identify one situation where this topic appears in your work.",
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
                "Provide a realistic scenario.",
                "Ask the learner to choose or construct an appropriate response.",
            ],
            interaction="Scenario-based decision activity with feedback.",
        ),
    ]

    return Storyboard(
        course_title=f"{title_seed}",
        audience=audience,
        learning_objectives=[
            "Explain the core concepts presented in the source material.",
            "Apply the concepts to a realistic work scenario.",
            "Identify an appropriate next action using the provided guidance.",
        ],
        sections=sections,
        knowledge_check={
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
