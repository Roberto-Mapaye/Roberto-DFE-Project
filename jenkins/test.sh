#!/bin/bash

echo "Test stage"

python3 -m venv venv
source venv/bin/activate

pip3 install pytest pytest-cov flask_testing
pip3 install -r frontend/requirements.txt
pip3 install -r backend/requirements.txt

mkdir test-reports


python3 -m pytest frontend --cov=frontend/application \
    --cov-report term-missing \
    --cov-report xml:test-reports/frontend_coverage.xml \
    --junitxml=test-reports/frontend-junit_report.xml

python3 -m pytest backend --cov=backend/application \
    --cov-report term-missing \
    --cov-report xml:test-reports/backend_coverage.xml \
    --junitxml=test-reports/backend-junit_report.xml

deactivate
rm -rf venv