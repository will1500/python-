#!/usr/bin/env bash
#test

set -e
set -x

pytest --cov=samplemod --cov=tests --cov-report=term-missing ${@}
bash ./scripts/lint.sh
