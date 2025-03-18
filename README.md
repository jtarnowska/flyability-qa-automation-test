# Setup of the project
1. Create an empty folder on your computer where the project will be placed.
2. Open Terminal/Command Prompt and clone the repository to this new folder:
`git clone https://github.com/jtarnowska/flyability-qa-automation-test.git`
3. Open project folder in IDE.
4. Open Terminal, move to the cloned project folder and create virtual environment: 
`python -m venv .venv`
5. Activate the virtual environment:
- for windows: `.venv/Scripts/Activate`
- for mac: `source .venv/bin/activate`
6. Install dependencies:
`pip install -r requirements.txt

# How to run tests
## All tests at once
`pytest .\tests\map_test.py` 
## Specific test
`pytest .\tests\map_test.py::{name_of_the_test}`
Example: `pytest .\tests\map_test.py::test_distance_display`
## Test with generating HTML report
`pytest .\tests\map_test.py --html=./reports/report.html --self-contained-html`

# Additional information:
- screenshots are available in .screenshots folder after running tests
- reports are available from the link visible in the terminal after running tests and are saved in .reports directory
- browsers are opened in en_GB language to make sure all selectors are always correct
- 