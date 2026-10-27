"""Original, fully authored mock example for the bundled AI-review source only."""

SECTIONS = [
    {
        "title": "A polished draft is not an approved draft",
        "purpose": "Establish why reviewers must check accuracy and record corrections before approval (objectives 1 and 2).",
        "key_points": [
            'On-screen heading: "Would you release these drafts?"\nLearner copy: "Review three fictional situations. A: an AI-written policy lesson includes an approval limit, but its reference document does not confirm the number. B: a lesson aims to teach documenting corrections, but its quiz only asks for a definition. C: a lesson gives an essential instruction only in an image, with no equivalent text. For each situation, state what you would check or request before approval."\nThese are synthetic review cases, not real policies or claims about uploaded material.',
            'Learner copy: "AI can draft content, but a person remains responsible for checking facts, alignment to learning objectives, terminology, tone, accessibility, and whether the assessment measures the intended skill."\nVisual brief: show a draft document beside an empty review checklist; keep the document marked Draft, not Approved.',
        ],
        "interaction": 'Type: opening guided reflection, not scored.\nSituations: use cases A, B, and C written above, each with its own labeled response field.\nPrompt: "For each draft, identify the issue and the next review action. Do not approve on appearance alone."\nLearner action: write a response for each case, then select Compare with review notes.\nSystem response: retain responses and reveal case-specific notes. A: "The limit is unverified. Ask the source owner or SME to confirm it; do not invent a replacement number." B: "The quiz checks recall rather than documenting corrections. Request a draft-review task that elicits a written correction." C: "Essential information lacks an accessible text equivalent. Request equivalent text and verify the built output."\nFeedback: ask learners to compare each response with the relevant issue and action, then revise. Alternative wording is acceptable. No automatic grading is implemented.\nEvidence limit: this opening identifies review concerns; it does not establish ability to complete a full review or implement fixes.\nCompletion: Continue after opening the comparison; retain edit/retry access.\nAccessibility: separate labeled fields for A/B/C, keyboard-operable buttons, and text feedback in reading order.',
    },
    {
        "title": "Use the objective to review the assessment",
        "purpose": "Model identification of an objective–assessment mismatch (objective 1).",
        "key_points": [
            'On-screen example, labeled Synthetic: "Objective: document required corrections in an AI-generated draft before approval. Draft quiz: What does human-in-the-loop mean?"\nLearner copy: "The definition question can check recall. It does not show whether the learner can inspect a draft and document a correction."',
            'Worked-example reasoning: "First identify the action in the objective: document corrections. Next inspect the evidence the quiz produces: a definition. The evidence does not demonstrate the action. Request a task that asks the learner to review a draft and record a specific correction."\nVisual brief: place the objective and quiz side by side; highlight the action and evidence only when the explanation reaches them. Provide the same distinctions in text.',
        ],
        "interaction": 'Type: learner-paced worked example.\nInitial state: show the objective and quiz, with the reasoning hidden.\nPrompt: "What evidence would this quiz give you?"\nLearner action: consider the question, then select Show review reasoning.\nSystem response: reveal the worked-example reasoning above. No scoring or learner-response evaluation is implied.\nNext action: select Continue to practice after reading; allow reopening the explanation.\nAccessibility: buttons work with keyboard; use explicit Objective and Draft quiz labels, not color alone. Motion is optional, with an equivalent static explanation.',
    },
    {
        "title": "Write a correction the designer can act on",
        "purpose": "Practice identifying a review issue and documenting an actionable correction (objectives 1 and 2).",
        "key_points": [
            'Practice draft, labeled Synthetic: "A review exercise asks learners to approve an AI-generated lesson because its wording is clear. It provides no opportunity to check facts or record errors."\nLearner copy: "Inspect this review process. Describe what is missing and the change you would request before approval."',
            'Review-note model: "Location: practice instruction. Issue: approval is based on writing clarity alone. Required change: add checks for factual accuracy and objective alignment, and provide a way to document errors and required corrections before approval."\nLearner copy: "A useful review note identifies where the issue occurs, what is wrong, and what needs to change. The model is one valid response, not required wording."',
        ],
        "interaction": 'Type: open written practice with self-comparison; not live AI role-play.\nInputs: three labeled fields — Location, Issue, Required correction.\nLearner action: write the review note and select Compare with model.\nSystem response: retain the input; reveal the review-note model and checklist: "Did you identify the location? Explain the missing review step? Specify a change before approval?"\nFeedback: invite the learner to revise the note using the checklist. Do not claim the system has graded the text.\nRetry: allow editing and comparing again without penalty.\nCompletion: Continue after comparison; completion is not evidence of mastery. Independent response assessment still needs an ID-approved rubric and reviewer/model implementation.\nAccessibility: explicit labels, logical focus order, text feedback; no drag-only actions.',
    },
]

KNOWLEDGE_CHECK = {
    "objective_index": 0,
    "question": "A draft lesson aims to teach reviewers to document corrections, but its quiz only asks for the definition of human-in-the-loop. Which review note best addresses the assessment mismatch?",
    "options": [
        "Replace the definition question with a more detailed glossary question.",
        "Request a draft-review task that requires a documented correction.",
        "Add a longer explanation of the definition before the existing quiz.",
    ],
    "answer_index": 1,
    "feedback_mode": "per_option",
    "option_feedback": [
        "A more detailed glossary question still checks definition recall. It does not ask the learner to document a correction in a draft.",
        "A draft-review task elicits the target action: documenting a correction. This choice identifies an appropriate assessment, but does not itself demonstrate review-note writing.",
        "Additional explanation may support learning, but it does not change the evidence produced by the existing definition quiz. Revise the assessment task as well.",
    ],
    "feedback": "A documented correction provides evidence of the target action. More definition content still checks recall. This decision item checks recognition of an aligned task; it does not itself demonstrate the ability to write a review note.",
}

ADDITIONAL_ASSESSMENTS = [
    {
        "objective_index": 0,
        "question": "An AI draft states an approval limit that is not confirmed in its reference document. What should the reviewer do before release?",
        "options": ["Use a familiar limit from another process.", "Remove the reference and retain the limit.", "Ask the source owner to verify the limit."],
        "answer_index": 2,
        "feedback": "An unsupported rule needs verification, not a plausible replacement.",
        "feedback_mode": "per_option",
        "option_feedback": ["Another process does not establish this rule. Request verification rather than substitute a familiar value.", "Removing the reference hides the evidence gap without resolving it. The claim remains unsupported.", "Verification addresses the accuracy issue without inventing a rule. Keep the claim pending until confirmed."],
    },
    {
        "type": "written", "objective_index": 1,
        "question": "Synthetic draft, practice instruction: 'Approve the AI-generated lesson when its writing is clear.' Write a review note specifying the location, issue, and required correction before approval.",
        "rubric": "The note identifies the practice instruction; explains that writing clarity alone omits accuracy/alignment review; requests specific checks and documentation of required corrections before approval. Accept equivalent wording. A vague request to improve quality is insufficient.",
        "model_response": "Location: practice instruction. Issue: clarity alone does not establish accuracy or objective alignment. Required correction: add source and objective-alignment checks and a way to record required corrections before approving the draft.",
    },
    {
        "type": "written", "objective_index": 1,
        "question": "Synthetic draft, assessment block: the objective asks learners to document review corrections, but the assessment asks only for a definition. Write a review note identifying the issue and requesting an assessment change that produces evidence of the target behavior.",
        "rubric": "Identify the assessment block, explain recall versus documenting corrections, and request a draft-review task with a written correction assessed against explicit criteria. Accept other defensible performance tasks. Do not award evidence of performance merely for selecting a task type.",
        "model_response": "Location: assessment block. Issue: the definition item does not elicit a documented correction. Required correction: provide a draft to inspect and ask learners to record the issue and required change, with an ID-approved review rubric.",
    },
]
