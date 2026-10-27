import unittest
from pathlib import Path
from unittest.mock import patch

from src.mock_generation import generate_current_mock


class MockGenerationTests(unittest.TestCase):
    def test_generation_replaces_stale_imported_fixture(self):
        import src.sample_storyboard as fixture
        import src.storyboard as generator
        sample = (Path(__file__).resolve().parent.parent / 'data/sample_source.md').read_text()
        with patch.object(fixture, 'SECTIONS', []), patch.object(generator, 'SECTIONS', []):
            content = generate_current_mock(sample, 'Reviewers', require_latest_example=True)
            self.assertIn('Situations: use cases A, B, and C', content['sections'][0]['interaction'])
