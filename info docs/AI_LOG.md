# AI PROMPT-and-Diff Log


## M1 — Project Concept and Setup

### Prompt
Develop the initial concept for AutoScroll, a PDF reader that automatically scrolls through documents for hands-free reading, and establish the project's development tools.

### Changes Made
- No AI input was needed for this part of the project


## M2 — Requirements and AI Elicitation Audit

### Prompt
Develop user stories, acceptance criteria, and measurable non-functional requirements for AutoScroll. I have my own and will compare with yours afterwards.

### Changes Made
- Documented user stories covering PDF upload and viewing, automatic scrolling, starting and stopping, scroll speed, remembering reading position, and reaching the end of a document.
- Added measurable non-functional requirements for scrolling performance, document loading, and PDF validation.
- Compared the AI-generated requirements against the planned application.
- Recorded missing requirements, unsupported assumptions, and useful suggestions from the AI draft.

### Review and Verification
Reviewed the generated requirements rather than accepting them automatically. Identified questions about hands-free interaction, scrolling behavior, speed settings, and document storage that needed consideration.


## M3 — Domain Model and AI Audit

### Prompt
Create a domain model for AutoScroll. I will compare my model with an AI-generated draft based on the M2 requirements.

### Changes Made
- Created a domain model representing the main concepts involved in uploading, storing, and reading PDF documents.
- Produced an AI-generated draft for comparison.
- Documented differences between the two models and evaluated which elements were necessary for the application.

### Review and Verification
Compared the models against the requirements and considered whether the proposed entities and relationships were useful for the current application scope. Avoided adding unnecessary complexity just because the AI suggested it.


## M4 — Architecture Decision Record

### Prompt
Document a real architecture decision for AutoScroll, including the alternatives considered and the consequences of the final choice.

### Decision
Use Django as the main web framework, with HTML, CSS, and JavaScript handling the user interface and browser-side automatic scrolling.

### Alternatives Considered
- A standalone Python application, which would not use the required Django web framework.
- A JavaScript-focused application, which would move away from the selected Python and Django stack.
- Handling scrolling primarily on the Django server, which would add unnecessary communication and complexity for a browser-based feature.

### Consequences
This approach keeps the application within the required technology stack and allows scrolling to happen in the browser. It also means the Django-rendered pages and JavaScript functionality must work together correctly.

### Review and Verification
Recorded the decision and its tradeoffs in ADR-001. Considered the alternatives and accepted the browser-side JavaScript dependency as a reasonable tradeoff for the application.

## M5 — Walking Skeleton and CI

### Goal
Implement a thin end-to-end slice of AutoScroll that allows a user to upload a PDF and view it in the browser, with automated testing through GitHub Actions.

### AI Assistance
ChatGPT assisted with implementing and troubleshooting the Django upload flow, document page, PDF display, automated test, and GitHub Actions workflow.

### Prompts and Changes

#### 1. Implementing PDF Upload
- Prompt/task: Create a Django workflow for uploading a PDF and displaying the uploaded document.
- Changes: Added the document model, upload view, document view, URL routes, and HTML templates.
- Verification: Tested the upload process in the browser.

#### 2. Fixing PDF Display
- Prompt/task: Troubleshoot why the uploaded PDF would not display inside the document page.
- Changes: Investigated the iframe response headers and changed `X_FRAME_OPTIONS` to `SAMEORIGIN`.
- Verification: Confirmed that the PDF displayed correctly after restarting the Django server.

#### 3. Automated Testing
- Prompt/task: Test the upload-to-document workflow.
- Changes: Added a Django test covering PDF upload, document creation, and the document page response.
- Verification: Ran the Django test suite and confirmed it passed.

#### 4. Continuous Integration
- Prompt: Configure GitHub Actions to check the Django project and run automated tests.
- Changes: Added a workflow under `.github/workflows/`.
- Verification: Pushed the changes and checked the GitHub Actions result.

### Human Review
I tested the application in the browser, reviewed the test output, and investigated the PDF display issue rather than relying only on the generated code.

### Final Result
A user can upload a PDF and open a page that displays it. The automated test checks the upload workflow, and GitHub Actions runs the project's checks and tests.

## M6 — Tests and Bug-Injection Demonstration

### AI Prompts Used
- Given my first two tests, add another test that is not covered by them that could be important to the project.

### Changes Made
- Added a test to verify that the document page loads successfully and contains the PDF viewer.
- Added a test to verify that requesting a nonexistent document returns a 404 response.
- Added a test to verify that the application displays the requested PDF rather than a different document.
- Generated a test coverage report using Coverage.py.
- Temporarily modified the document lookup logic so that the application always displayed the first document instead of the requested one.

### Bug-Injection Results
The injected fault caused the new test to fail. When the test requested the second PDF, the application displayed the first PDF instead. This demonstrated that the test suite could detect a user-facing bug that would not necessarily cause the application to crash.

After the test detected the problem, I restored the original document lookup logic. I then reran the tests to verify that the fix restored the expected behavior.

### Review and Verification
I reviewed the generated tests and ran them using Django's test runner. The tests checked the document page response, missing-document handling, and whether the correct PDF was displayed.

The bug-injection experiment was used to check whether the tests could identify incorrect application behavior rather than relying only on coverage percentages.

### Evidence
- Django test execution output.
- Coverage.py terminal report and HTML coverage report.
- Injected fault in `documents/views.py`.
- Test failure showing that the wrong PDF was displayed.
- Restored document lookup logic and passing test output.