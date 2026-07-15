#!/usr/bin/env bash
# The definition of mechanical done. Run from the repo root. Sections run in order
# and fail fast: an item is not done until every hard section passes. Lint is
# advisory and never blocks the gate. Build already runs tsc --noEmit, so there is
# no separate typecheck section.
set -uo pipefail

echo "== 1/6 validate (queue + registry + critiques + content) =="
if ! python3 scripts/validate.py; then
  echo "VALIDATE FAILED"
  exit 1
fi

echo ""
echo "== 2/6 prose lint =="
if ! python3 scripts/prose_lint.py; then
  echo "PROSE LINT FAILED"
  exit 1
fi

echo ""
echo "== 3/6 pipeline test =="
if ! npm run test:pipeline; then
  echo "PIPELINE TESTS FAILED"
  exit 1
fi

echo ""
echo "== 4/6 test =="
if ! npm run test; then
  echo "TESTS FAILED"
  exit 1
fi

echo ""
echo "== 5/6 build (tsc --noEmit + vite build) =="
if ! npm run build; then
  echo "BUILD FAILED"
  exit 1
fi

echo ""
echo "== 6/6 lint (advisory) =="
if ! npm run lint; then
  echo "lint reported issues (advisory, not blocking the gate)"
fi

echo ""
echo "CHECK OK"
