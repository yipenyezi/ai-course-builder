"""Reload editable mock fixtures on explicit generation, not on every UI rerun."""
import importlib


def generate_current_mock(source, audience, *, require_latest_example=False):
    # Streamlit may rerun app.py while imported modules retain old definitions.
    # This development-only mock reloads the fixture before its dependent generator.
    import src.sample_storyboard as fixture
    import src.storyboard as generator
    importlib.invalidate_caches()
    importlib.reload(fixture)
    importlib.reload(generator)
    content = generator.generate_storyboard(source, audience).to_dict()
    if require_latest_example:
        if not content['sections'] or 'Situations: use cases A, B, and C' not in content['sections'][0]['interaction']:
            raise ValueError('The latest example did not load. No revision was saved. Restart the Streamlit server and try again.')
    return content
