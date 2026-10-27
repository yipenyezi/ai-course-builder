"""Local prototype review records; no authentication or AI approval is implied."""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import uuid


def validate_storyboard(value):
    if not isinstance(value, dict):
        raise ValueError("Storyboard must be a JSON object.")
    def text(v):
        return isinstance(v, str) and bool(v.strip())
    for key in ("course_title", "audience"):
        if not text(value.get(key)):
            raise ValueError(f"{key} must contain text.")
    objectives = value.get("learning_objectives")
    if not isinstance(objectives, list) or not objectives or not all(map(text, objectives)):
        raise ValueError("Provide at least one nonempty learning objective.")
    sections = value.get("sections")
    if not isinstance(sections, list) or not sections:
        raise ValueError("Provide at least one section.")
    for section in sections:
        if not isinstance(section, dict) or not all(text(section.get(k)) for k in ("title", "purpose", "interaction")):
            raise ValueError("Every section needs a title, purpose, and interaction.")
        points = section.get("key_points")
        if not isinstance(points, list) or not points or not all(map(text, points)):
            raise ValueError("Every section needs nonempty key points.")
    check = value.get("knowledge_check")
    if not isinstance(check, dict) or not all(text(check.get(k)) for k in ("question", "feedback")):
        raise ValueError("The knowledge check needs a question and feedback.")
    options = check.get("options")
    if not isinstance(options, list) or len(options) < 2 or not all(map(text, options)):
        raise ValueError("The knowledge check needs at least two nonempty options.")
    answer = check.get("answer_index")
    if type(answer) is not int or not 0 <= answer < len(options):
        raise ValueError("answer_index must identify an existing option (starting at zero).")
    mode = check.get('feedback_mode', 'shared')
    if mode not in {'shared', 'per_option'}:
        raise ValueError('Choose a supported feedback mode.')
    if mode == 'per_option':
        feedback = check.get('option_feedback')
        if not isinstance(feedback, list) or len(feedback) != len(options) or not all(map(text, feedback)):
            raise ValueError('Provide nonempty feedback for every option before saving.')
    for item in value.get('additional_assessments', []):
        if item.get('type') == 'written':
            if not all(text(item.get(k)) for k in ('question', 'rubric', 'model_response')):
                raise ValueError('Written tasks require a prompt, rubric, and illustrative response.')
        else:
            nested = {**value, 'knowledge_check': item, 'additional_assessments': []}
            validate_storyboard(nested)
    for item in [check] + value.get('additional_assessments', []):
        index = item.get('objective_index', 0)
        if type(index) is not int or not 0 <= index < len(objectives):
            raise ValueError('Every assessment item must link to an existing objective.')


def new_project():
    return {"schema_version": "0.1", "project_id": str(uuid.uuid4()), "revisions": []}


def save_revision(project, content, *, source, feedback=""):
    validate_storyboard(content)
    project["revisions"].append({
        "version": len(project["revisions"]) + 1, "status": "draft",
        "content": deepcopy(content), "source": deepcopy(source),
        "feedback": feedback, "created_at": datetime.now(timezone.utc).isoformat(),
        "approval": None,
    })


def digest(content):
    return hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()


def approve(project, reviewer):
    if not reviewer.strip():
        raise ValueError("Enter the ID reviewer name.")
    revision = project["revisions"][-1]
    if revision["status"] != "draft":
        raise ValueError("Only the current draft can be approved.")
    validate_storyboard(revision["content"])
    revision["status"] = "approved"
    revision["approval"] = {"reviewer": reviewer.strip(), "version": revision["version"],
                            "content_digest": digest(revision["content"]),
                            "at": datetime.now(timezone.utc).isoformat()}


def approved_content(project):
    revision = project["revisions"][-1]
    approval = revision.get("approval")
    if revision["status"] != "approved" or not approval or approval["content_digest"] != digest(revision["content"]):
        raise ValueError("Approve the current saved storyboard before generating HTML.")
    return deepcopy(revision["content"])


def persist(project, directory):
    """Write a local snapshot atomically; caller owns access to the directory."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    identifier = str(uuid.UUID(project["project_id"]))
    target = directory / f"{identifier}.json"
    temporary = directory / f"{identifier}.tmp"
    temporary.write_text(json.dumps(project, indent=2), encoding="utf-8")
    temporary.replace(target)
    return target
