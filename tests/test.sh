#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

set +e
pytest /tests/test_outputs.py -rA
status=$?
set -e

if [ "$status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
  cat > /logs/verifier/ctrf.json <<'JSON'
{"results":{"tool":{"name":"pytest"},"summary":{"tests":5,"passed":5,"failed":0,"skipped":0},"tests":[]}}
JSON
else
  echo 0 > /logs/verifier/reward.txt
  cat > /logs/verifier/ctrf.json <<'JSON'
{"results":{"tool":{"name":"pytest"},"summary":{"tests":5,"passed":0,"failed":5,"skipped":0},"tests":[]}}
JSON
  exit 1
fi
