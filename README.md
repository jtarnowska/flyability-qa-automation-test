# Setup of the project

1. Clone the repository with `git clone`.
2. Move to the cloned project folder and create virtual environment: 

`python -m venv .venv`

3. Activate the virtual environment:
- for windows: `.venv/Scripts/Activate`
- for mac: `source .venv/bin/activate`
4. Install dependencies:

`pip install -r requirements.txt`

5. Run tests.

# How to run tests
By default, all tests are run on Chrome browser, but they are also working on Firefox and Edge (by using an option `--browser`)

## All tests at once
`pytest tests`

## Test with generating HTML report
`pytest tests --html=./reports/report.html --self-contained-html`

## Run tests on specific browser
`pytest tests --browser chrome`

`pytest tests --browser firefox`

`pytest tests --browser edge`

# Additional information:
- screenshots are available in `screenshots` folder after running tests
- reports are available after running tests and are saved in `reports` directory
- browsers are opened in `en-GB` language to make sure all selectors are always correct
