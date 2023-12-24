#!/usr/bin/env bash
# test

set -e
# set -x  # Uncomment this line for debugging

python -m pytest

# Run lint script
bash ./scripts/lint.sh
