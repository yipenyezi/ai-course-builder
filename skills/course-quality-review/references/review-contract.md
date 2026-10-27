# Review contract

## Severity and gate outcome

- **Blocker:** a demonstrated issue prevents the requested next step, such as unapproved training diagnosis before production, a materially ambiguous key, missing evidence for a claimed complete skill, stale approval, inaccessible essential task cues, or exposed service credentials. Link the issue to the relevant requirement.
- **Required correction:** a concrete defect needs repair before the affected artifact is accepted, but may not prevent unrelated draft work. State exactly what is gated.
- **Advisory:** an optional improvement or preference. Do not create a new requirement from reviewer taste.
- **Unknown/not verified:** insufficient access or execution evidence. Describe the missing check and whether it is required at this gate; do not count all future runtime checks as blockers during early storyboarding.

Overall: **blocked** when required evidence or defects prevent the requested gate; **verification incomplete** when outstanding in-scope checks prevent a recommendation; **ready for human review** when available checks support review with no unresolved gate blockers. Report advisory and deferred checks separately. This is not ID/SME approval.

## Issue log

| Issue ID | Gate / artifact and version | Location / linked IDs | Observed evidence | Requirement and consequence | Severity / affected step | Proposed fix or verification | Owner / disposition |
|---|---|---|---|---|---|---|---|
| [ID] | [version] | [source, block, item, criterion] | [excerpt, mismatch, or test result] | [specific basis] | [not mere aesthetic preference] | [action] | [ID/SME/developer; pending/verified fix] |

Separate observed defect, interpretation, and suggested remedy. For a source claim that cannot be verified, say so rather than alleging the claim is false. Group duplicate issues without hiding affected locations.

## Alignment coverage

| Gap / task | Objective and version | Practice / support | Assessment evidence / limitation | Storyboard location | Missing / stale link |
|---|---|---|---|---|---|
| [IDs] | [reference] | [reference] | [what it establishes] | [slide or lesson/block] | [specific issue] |

## Verification record

| Check | Scope / environment / artifact version | Method | Result | Evidence / limitation |
|---|---|---|---|---|
| [source, static, browser, host, LRS, learner pilot] | [actual environment] | [what was run or inspected] | [pass / fail / not-run / inconclusive] | [reference] |

Structural skill validation is not instructional validation. A standalone browser pass is not Rise/LMS validation. An AI judge preference is not a measured gain in learning. Keep independent human judgment and actual learner evidence visible.

## Examples

- **Storyboard gate:** an objective requires eliciting and confirming needs, but only a question about the first action exists. Flag missing evidence for confirmation/full conversation; propose an open performance opportunity or narrow the approved claim through ID review.
- **Storyboard gate:** no live LMS test yet. Record it as a deferred built-output check, not proof that the storyboard is unusable.
- **Production gate:** current sources changed but the storyboard approval refers to the old version. Block affected production until revision and approval; preserve prior records.
- **Role-play test:** a guidance panel appears before the learner requests help. Report the observed hint-policy violation, identify its UI/state location, and retest after repair.

## Summary

State reviewed versions and gate; blockers/required fixes; unknowns and deferred checks; optional improvements; proposed owners and affected artifacts; readiness recommendation. Do not manufacture percentages or claim a complete review when only a subset was inspected.
