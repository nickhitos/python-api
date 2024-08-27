# Palindrome Checker

## Description
This repository contains a simple Python function to check if a string is a palindrome, along with unit tests to verify its correctness.

This project uses GitHub Actions to automate the Continuous Integration (CI) and Continuous Deployment (CD) processes. The CI/CD pipeline is configured to automatically run tests every time new code is pushed to the repository, ensuring that any changes do not introduce errors or break existing functionality.

## File Structure
- Function to verify palindromes is in ```palindrome.py```
- Unit tests are in ```test_palindrome.py```
- Actions to execute CI/CD tests are in ```.github/workflows/python-app.yml```

## Setup
To run locally, execute the following:

```bash
python -m pip install --upgrade pip
pip install pytest
pytest test_palindrome.py