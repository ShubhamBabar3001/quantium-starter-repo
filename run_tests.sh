#!/bin/bash

# 1. Activate the project virtual environment
source venv/Scripts/activate

# 2. Execute the test suite
pytest test_app.py

# 3. Capture the test exit code
TEST_EXIT_CODE=$?

# 4. Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi