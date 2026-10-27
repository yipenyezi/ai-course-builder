"""Versioned design artifacts and review gates, independent of the Streamlit UI."""
from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


STAGES = (
    "diagnosis", "sme_scope", "design", "storyboard", "interaction_spec",
)


@dataclass
class Revision:
    version: int
    content: dict[str, Any]
    status: str = "draft"
    # Exact upstream versions used to produce this revision.
    dependencies: dict[str, int] = field(default_factory=dict)
    reviews: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class Project:
    project_id: str
    title: str
    schema_version: str = "0.1"
    artifacts: dict[str, list[Revision]] = field(default_factory=dict)

    def current(self, stage: str) -> Revision:
        if stage not in STAGES:
            raise ValueError(f"Unknown stage: {stage}")
        if not self.artifacts.get(stage):
            raise ValueError(f"No artifact for {stage}")
        return self.artifacts[stage][-1]

    def _dependencies(self, stage: str) -> dict[str, int]:
        index = STAGES.index(stage)
        dependencies = {}
        for upstream in STAGES[:index]:
            revision = self.current(upstream)
            if revision.status != "approved":
                raise ValueError(f"{upstream} must be approved first")
            dependencies[upstream] = revision.version
        if index > 0:
            decision = self.current("diagnosis").content.get("intervention")
            if decision not in {"training", "combined"}:
                raise ValueError("Course design requires a confirmed training need")
        return dependencies

    def revise(self, stage: str, content: dict[str, Any]) -> Revision:
        """Create a draft snapshot; invalidate downstream approvals without deleting history."""
        if stage not in STAGES:
            raise ValueError(f"Unknown stage: {stage}")
        dependencies = self._dependencies(stage)
        history = self.artifacts.setdefault(stage, [])
        revision = Revision(len(history) + 1, deepcopy(content), dependencies=dependencies)
        history.append(revision)
        for downstream in STAGES[STAGES.index(stage) + 1:]:
            if self.artifacts.get(downstream):
                self.current(downstream).status = "needs_review"
        return revision

    def submit(self, stage: str) -> None:
        revision = self.current(stage)
        if revision.status != "draft":
            raise ValueError("Only a draft can be submitted")
        if revision.dependencies != self._dependencies(stage):
            raise ValueError("Rebase the artifact on current approved inputs")
        revision.status = "in_review"

    def review(self, stage: str, *, reviewer: str, decision: str, feedback: str = "") -> None:
        revision = self.current(stage)
        if revision.status != "in_review":
            raise ValueError("Submit the artifact before review")
        if not reviewer.strip() or decision not in {"approve", "request_changes"}:
            raise ValueError("A reviewer and valid decision are required")
        if decision == "approve" and revision.dependencies != self._dependencies(stage):
            raise ValueError("Upstream inputs have changed")
        revision.reviews.append({
            "reviewer": reviewer, "decision": decision, "feedback": feedback,
            "at": datetime.now(timezone.utc).isoformat(), "version": revision.version,
        })
        revision.status = "approved" if decision == "approve" else "changes_requested"

    def build_inputs(self) -> dict[str, int]:
        """Gate for a future production renderer; does not render or publish anything."""
        dependencies = self._dependencies("interaction_spec")
        specification = self.current("interaction_spec")
        if specification.status != "approved" or specification.dependencies != dependencies:
            raise ValueError("Interaction specification requires current approval")
        return {**dependencies, "interaction_spec": specification.version}

    def to_dict(self) -> dict[str, Any]:
        return deepcopy(asdict(self))
