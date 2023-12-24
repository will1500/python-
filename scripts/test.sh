#!/usr/bin/env bash
# test

set -e
# set -x  # Uncomment this line for debugging

pytest --cov=samplemod --cov=tests --cov-report=term-missing

# Run lint script
bash ./scripts/lint.sh
