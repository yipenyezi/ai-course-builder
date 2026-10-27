import tempfile
import unittest
import json

from src.storyboard import generate_storyboard
from src.storyboard_review import new_project, save_revision, approve, approved_content, persist


class ReviewTests(unittest.TestCase):
    def test_option_feedback_requires_coverage_and_safe_rendering(self):
        from src.html_generator import generate_interactive_html
        from src.storyboard_review import validate_storyboard
        content = generate_storyboard('Synthetic material.').to_dict()
        check = content['knowledge_check']
        check['feedback_mode'] = 'per_option'
        check['option_feedback'] = ['Only one explanation']
        with self.assertRaises(ValueError):
            validate_storyboard(content)
        check['option_feedback'] = ['First explanation', '</script><script>bad()</script>', 'Third explanation']
        validate_storyboard(content)
        output = generate_interactive_html(content)
        self.assertIn('First explanation', output)
        self.assertIn('Third explanation', output)
        self.assertNotIn('</script><script>bad()', output)
        self.assertIn('messages[index]', output)

    def test_approval_is_version_specific_and_history_is_preserved(self):
        project = new_project()
        content = generate_storyboard('Synthetic product discovery.').to_dict()
        save_revision(project, content, source={'provider': 'mock'})
        with self.assertRaises(ValueError):
            approved_content(project)
        approve(project, 'Test ID')
        self.assertEqual(approved_content(project), content)
        content['course_title'] = 'Revised title'
        save_revision(project, content, source={'provider': 'mock'}, feedback='Clarify title')
        self.assertEqual(project['revisions'][0]['status'], 'approved')
        with self.assertRaises(ValueError):
            approved_content(project)
        approve(project, 'Test ID')
        project['revisions'][-1]['content']['course_title'] = 'Unsaved mutation'
        with self.assertRaises(ValueError):
            approved_content(project)

    def test_invalid_key_does_not_create_revision_and_records_persist(self):
        project = new_project()
        content = generate_storyboard('Synthetic material.').to_dict()
        content['knowledge_check']['answer_index'] = 999
        with self.assertRaises(ValueError):
            save_revision(project, content, source={})
        self.assertEqual(project['revisions'], [])
        content['knowledge_check']['answer_index'] = 1
        save_revision(project, content, source={})
        approve(project, 'Test ID')
        with tempfile.TemporaryDirectory() as directory:
            path = persist(project, directory)
            restored = json.loads(path.read_text())
            self.assertEqual(approved_content(restored), content)
