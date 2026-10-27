import unittest

from src.project import Project, STAGES


class ProjectTests(unittest.TestCase):
    def approve(self, project, stage, content=None):
        project.revise(stage, content or {})
        project.submit(stage)
        project.review(stage, reviewer="Synthetic test reviewer", decision="approve")

    def test_cannot_skip_review_or_training_decision(self):
        project = Project("test", "Test")
        project.revise("diagnosis", {"intervention": "non_training"})
        with self.assertRaises(ValueError):
            project.revise("sme_scope", {})
        project.submit("diagnosis")
        project.review("diagnosis", reviewer="Reviewer", decision="approve")
        with self.assertRaises(ValueError):
            project.revise("sme_scope", {})

    def test_upstream_change_blocks_build_even_after_reapproval(self):
        project = Project("test", "Test")
        for stage in STAGES:
            self.approve(project, stage, {"intervention": "training"})
        self.assertEqual(project.build_inputs()["storyboard"], 1)
        self.approve(project, "design", {"new_objective": True})
        self.assertEqual(project.current("storyboard").status, "needs_review")
        with self.assertRaises(ValueError):
            project.build_inputs()
        for stage in ("storyboard", "interaction_spec"):
            self.approve(project, stage)
        self.assertEqual(project.build_inputs()["design"], 2)
        self.assertEqual(project.artifacts["design"][0].version, 1)

    def test_feedback_requires_revision_and_content_is_snapshotted(self):
        project = Project("test", "Test")
        content = {"intervention": "training", "notes": []}
        project.revise("diagnosis", content)
        content["notes"].append("later mutation")
        self.assertEqual(project.current("diagnosis").content["notes"], [])
        project.submit("diagnosis")
        project.review("diagnosis", reviewer="Reviewer", decision="request_changes", feedback="Add evidence")
        with self.assertRaises(ValueError):
            project.submit("diagnosis")
        self.approve(project, "diagnosis", {"intervention": "combined"})
        self.assertEqual(project.artifacts["diagnosis"][0].reviews[0]["feedback"], "Add evidence")


if __name__ == "__main__":
    unittest.main()
