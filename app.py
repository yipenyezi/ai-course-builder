from pathlib import Path
from copy import deepcopy
import json

import streamlit as st
import streamlit.components.v1 as components

from src.mock_generation import generate_current_mock
from src.html_generator import generate_interactive_html
from src.source_files import extract_source
import hashlib
from src.storyboard_review import new_project, save_revision, approve, approved_content, persist

ROOT = Path(__file__).resolve().parent
STORE = ROOT / '.local_projects'
st.set_page_config(page_title='AI Course Builder', page_icon='🧠', layout='wide')
st.title('AI Course Builder')
st.caption('Draft a storyboard, review and revise it, then explicitly approve a saved version.')
st.info('Deterministic mock generator. No model is connected and project skills are not yet automatically executed. This isolated review prototype does not replace upstream diagnosis and design approval.')

if 'review_project' not in st.session_state:
    st.session_state.review_project = new_project()
project = st.session_state.review_project

def commit(candidate):
    # Persist before updating session state, so failed writes cannot imply a saved decision.
    persist(candidate, STORE)
    st.session_state.review_project = candidate

with st.sidebar:
    st.header('Local projects')
    st.caption('Snapshots stay on this computer in .local_projects, excluded from Git. Reviewer names are audit labels, not authenticated identities.')
    files = sorted(STORE.glob('*.json')) if STORE.exists() else []
    selected = st.selectbox('Saved project', files, format_func=lambda p: p.stem, index=None)
    if st.button('Open saved project', disabled=selected is None):
        try:
            candidate = json.loads(selected.read_text())
            from src.storyboard_review import validate_storyboard
            if candidate.get('schema_version') != '0.1' or not isinstance(candidate.get('revisions'), list):
                raise ValueError('Unsupported project format.')
            for revision in candidate['revisions']:
                validate_storyboard(revision['content'])
            st.session_state.review_project = candidate
            if candidate['revisions']:
                saved_source = candidate['revisions'][-1]['source']
                st.session_state.source_text = saved_source.get('text', '')
                st.session_state.source_audience = saved_source.get('audience', 'Adult learners')
                st.session_state.source_upload = saved_source.get('uploaded_file') or {}
            st.rerun()
        except (ValueError, KeyError, OSError) as exc:
            st.error(str(exc))
    if st.button('Start new project'):
        st.session_state.review_project = new_project()
        for key in ('source_text', 'source_audience', 'source_upload'):
            st.session_state.pop(key, None)
        st.rerun()

sample = (ROOT / 'data/sample_source.md').read_text(encoding='utf-8')
st.caption('Refreshing does not regenerate saved storyboards. To see updated example content, create a new draft with the latest built-in example below.')
if st.button('Generate latest built-in example'):
    try:
        candidate = deepcopy(project)
        save_revision(candidate, generate_current_mock(sample, 'Learning-content reviewers', require_latest_example=True),
                      source={'text': sample, 'audience': 'Learning-content reviewers', 'provider': 'deterministic_mock',
                              'example_revision': 'concrete-review-cases-v1'},
                      feedback='Generated the latest built-in example; earlier versions are preserved.')
        commit(candidate)
        st.session_state.source_text = sample
        st.session_state.source_audience = 'Learning-content reviewers'
        st.session_state.pop('source_upload', None)
        st.rerun()
    except (ValueError, OSError) as exc:
        st.error(str(exc))
with st.expander('Source and mock generation', expanded=not project['revisions']):
    audience = st.text_input('Target audience', value='Adult learners', key='source_audience')
    upload = st.file_uploader('Upload source material', type=['txt', 'md', 'pdf', 'docx'], key=f'upload_{project["project_id"]}', help='One file, up to 10 MB. Text extraction only; OCR is not supported.')
    st.caption('PDFs become page-referenced Markdown, without reconstructing tables or images; reading order may need correction. DOCX extraction includes body/table text, not images, headers, comments, or tracked-change interpretation. Review before generating.')
    if st.button('Load uploaded text', disabled=upload is None):
        try:
            data = upload.getvalue()
            extracted = extract_source(upload.name, data)
            st.session_state.source_text = extracted
            st.session_state.source_upload = {'project_id': project['project_id'], 'filename': upload.name, 'sha256': hashlib.sha256(data).hexdigest(),
                                              'format': 'markdown' if Path(upload.name).suffix.lower() == '.pdf' else 'text',
                                              'original_extraction': extracted,
                                              'method': 'pypdf_page_text_v1' if Path(upload.name).suffix.lower() == '.pdf' else 'text_extraction_v1'}
            st.success('Text loaded below. Review and edit it before generating a draft.')
        except ValueError as exc:
            st.error(str(exc))
    source = st.text_area('Source material', value=sample, height=220, key='source_text')
    provenance = st.session_state.get('source_upload', {})
    if provenance.get('project_id') == project['project_id']:
        st.caption(f'Loaded source: {provenance["filename"]}. Edits below are saved with each generated version; the original binary file is not saved.')
        if provenance.get('format') == 'markdown':
            st.download_button('Download reviewed source Markdown', source,
                               file_name='reviewed_source.md', mime='text/markdown')
            with st.expander('Original PDF extraction (before edits)'):
                st.code(provenance['original_extraction'], language='markdown')
    if st.button('Generate new mock draft', type='primary'):
        if not source.strip():
            st.error('Provide source material first.')
        else:
            try:
                candidate = deepcopy(project)
                save_revision(candidate, generate_current_mock(source, audience),
                              source={'text': source, 'audience': audience, 'provider': 'deterministic_mock',
                                      'uploaded_file': provenance if provenance.get('project_id') == project['project_id'] else None})
                commit(candidate)
                st.rerun()
            except (ValueError, OSError) as exc:
                st.error(str(exc))

if not project['revisions']:
    st.write('Generate a draft to begin review.')
    st.stop()

revision = project['revisions'][-1]
version = revision['version']
st.subheader(f'Storyboard · Version {version} · {revision["status"]}')
st.caption('Editing creates a new draft. Previous approved versions remain in the history. The current mock uses a generic section structure, not full Rise/Storyline output yet.')
editor_key = f'editor_{project["project_id"]}_{version}'
edited_content = deepcopy(revision['content'])

def edit_text(label, value, field, *, multiline=False, help=None):
    widget = st.text_area if multiline else st.text_input
    if multiline and field.endswith('_interaction'):
        return widget(label, value=value, key=f'{editor_key}_{field}', help=help, height=300)
    if multiline and '_point_' in field:
        return widget(label, value=value, key=f'{editor_key}_{field}', help=help, height=190)
    return widget(label, value=value, key=f'{editor_key}_{field}', help=help)

st.caption('Review and edit the fields below. Save changes as a new draft before approval.')
st.subheader('Course overview')
edited_content['course_title'] = edit_text('Course title', edited_content['course_title'], 'title')
edited_content['audience'] = edit_text('Learner audience', edited_content['audience'], 'audience')
st.subheader('Learning objectives')
for i, objective in enumerate(edited_content['learning_objectives']):
    edited_content['learning_objectives'][i] = edit_text(f'Objective {i + 1}', objective, f'objective_{i}', multiline=True)

st.subheader('Storyboard content')
st.caption('The bundled source has a detailed authored mock. Other sources still generate a generic outline pending AI integration. Described activities are specifications; the existing HTML preview does not implement every activity.')
for i, section in enumerate(edited_content['sections']):
    with st.expander(f"Section {i + 1}: {revision['content']['sections'][i]['title']}", expanded=True):
        section['title'] = edit_text('Section title', section['title'], f'section_{i}_title')
        section['purpose'] = edit_text('Teaching purpose', section['purpose'], f'section_{i}_purpose', multiline=True)
        st.write('Teaching content and learner-facing copy')
        st.caption('Review exact copy, examples, explanations, and visual descriptions—not just topic labels.')
        for j, point in enumerate(section['key_points']):
            section['key_points'][j] = edit_text(f'Point {j + 1}', point, f'section_{i}_point_{j}', multiline=True)
        section['interaction'] = edit_text('Learner activity and interaction', section['interaction'], f'section_{i}_interaction', multiline=True, help='Specify the prompt, learner actions, system responses, feedback, retries, completion, and accessibility. These are build specifications, not necessarily implemented in the HTML preview.')

st.subheader('Knowledge check')
checks = [edited_content['knowledge_check']] + edited_content.get('additional_assessments', [])
st.caption('Proposed assessment set. Counts and formats need ID confirmation; section count alone does not determine assessment coverage.')
for objective_index, objective in enumerate(edited_content['learning_objectives']):
    linked = [item for item in checks if item.get('objective_index', 0) == objective_index]
    written = sum(item.get('type') == 'written' for item in linked)
    st.write(f'LO {objective_index + 1}: {len(linked)} proposed items ({written} written tasks).')
    if not linked:
        st.warning(f'LO {objective_index + 1} has no linked assessment evidence. Resolve coverage before approving.')
for q, check in enumerate(checks, 1):
    st.markdown(f'#### Item {q}')
    check['objective_index'] = st.selectbox('Assessed learning objective', range(len(edited_content['learning_objectives'])),
        index=check.get('objective_index', 0), format_func=lambda i: f"LO {i + 1}: {edited_content['learning_objectives'][i]}", key=f'{editor_key}_q{q}_objective')
    if check.get('type') == 'written':
        check['question'] = edit_text('Performance task', check['question'], f'q{q}_task', multiline=True)
        check['rubric'] = edit_text('Evidence and review criteria', check['rubric'], f'q{q}_rubric', multiline=True)
        check['model_response'] = edit_text('Illustrative response', check['model_response'], f'q{q}_model', multiline=True)
        st.caption('Written responses require reviewer assessment; no automatic grading is implemented.')
        continue
    check['question'] = edit_text('Question', check['question'], f'q{q}_question', multiline=True)
    for i, option in enumerate(check['options']):
        check['options'][i] = edit_text(f'Option {i + 1}', option, f'q{q}_option_{i}')
    check['answer_index'] = st.selectbox('Correct answer', range(len(check['options'])), index=check['answer_index'], format_func=lambda i: f"Option {i + 1}: {check['options'][i]}", key=f'{editor_key}_q{q}_answer')
    check['feedback'] = edit_text('Answer explanation', check['feedback'], f'q{q}_explanation', multiline=True)
    feedback_modes = ['shared', 'per_option']
    feedback_mode = st.radio('Feedback mode', feedback_modes,
                            index=feedback_modes.index(check.get('feedback_mode', 'shared')),
                            format_func=lambda mode: 'Feedback for each option' if mode == 'per_option' else 'Shared answer explanation',
                            key=f'{editor_key}_q{q}_feedback_mode',
                            help='This prototype displays feedback immediately after a choice. Delayed assessment feedback is not implemented yet.')
    # Preserve legacy records unchanged when the existing shared mode is retained.
    if feedback_mode != 'shared' or 'feedback_mode' in check:
        check['feedback_mode'] = feedback_mode
    if feedback_mode == 'per_option':
        saved_feedback = check.get('option_feedback', [''] * len(check['options']))
        check['option_feedback'] = [
            edit_text(f'Feedback for option {i + 1}', saved_feedback[i] if i < len(saved_feedback) else '',
                      f'q{q}_option_feedback_{i}', multiline=True,
                      help='Explain why this specific choice is appropriate or mistaken and what to do next.')
            for i in range(len(check['options']))
        ]
feedback = st.text_area('ID feedback / revision notes', key=f'feedback_{project["project_id"]}_{version}', help='Saved with a new draft; feedback does not trigger automatic AI changes.')
unchanged = edited_content == revision['content']
with st.expander('Advanced: structured data'):
    st.caption('Read-only data reflecting the fields above. No JSON editing is required.')
    st.json(edited_content)

if st.button('Save as new draft'):
    try:
        candidate = deepcopy(project)
        save_revision(candidate, edited_content, source=revision['source'], feedback=feedback)
        commit(candidate)
        st.rerun()
    except (ValueError, OSError) as exc:
        st.error(str(exc))

reviewer = st.text_input('ID reviewer name', key=f'reviewer_{project["project_id"]}_{version}')
confirmed = st.checkbox('I have reviewed the saved content and approve this version.', key=f'confirm_{project["project_id"]}_{version}')
if not unchanged:
    st.warning('Unsaved edits cannot be approved or used to generate HTML. Save them as a new draft first.')
if feedback.strip():
    st.caption('Revision notes are not saved until you select Save as new draft.')
if st.button('Approve saved version', disabled=not (unchanged and confirmed and reviewer.strip() and revision['status'] == 'draft') or bool(feedback.strip())):
    try:
        candidate = deepcopy(project)
        approve(candidate, reviewer)
        commit(candidate)
        st.rerun()
    except (ValueError, OSError) as exc:
        st.error(str(exc))

st.download_button('Download project and review history', json.dumps(project, indent=2), file_name=f'{project["project_id"]}.json', mime='application/json')
with st.expander('Version history'):
    for previous in reversed(project['revisions']):
        st.write(f'Version {previous["version"]} · {previous["status"]}')
        if previous['feedback']:
            st.write(previous['feedback'])
        if previous['approval']:
            st.json(previous['approval'])
        st.write(previous['content']['course_title'])
        for objective in previous['content']['learning_objectives']:
            st.write(f'- {objective}')
        for section in previous['content']['sections']:
            st.write(f"**{section['title']}**")
            st.write(section['purpose'])
            for point in section['key_points']:
                st.write(f'- {point}')
            st.write(section['interaction'])

if revision['status'] == 'approved' and unchanged:
    st.success(f'Version {version} approved by {revision["approval"]["reviewer"]}.')
    st.subheader('Approved-version HTML prototype')
    html_output = generate_interactive_html(approved_content(project))
    components.html(html_output, height=650, scrolling=True)
    st.download_button('Download approved-version HTML', html_output, file_name=f'learning_interaction_v{version}.html', mime='text/html')
else:
    st.info('HTML generation is available after explicit approval of the current saved version.')
