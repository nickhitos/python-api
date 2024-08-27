# Palindrome Checker

## Description
This repository contains a simple Python function to check if a string is a palindrome, along with unit tests to verify its correctness.

This project uses GitHub Actions to automate the Continuous Integration (CI) and Continuous Deployment (CD) processes. The CI/CD pipeline is configured to automatically run tests every time new code is pushed to the repository, ensuring that any changes do not introduce errors or break existing functionality.

## Setup
To run locally, execute the following:

```bash
python -m pip install
pip install pytest pytest-cov
pytest test_palindrome.py