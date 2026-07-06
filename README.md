# Dynamo Terminal-Bench Fix

This repository contains a corrected Harbor/Terminal-Bench task for parsing an Apache-style access log and producing a strict JSON report.

## Fixed issues

- Corrected `artifacts` to a top-level array pointing to `/app/report.json`.
- Rewrote ambiguous instructions into exact output requirements.
- Removed the leaked reference solution from the agent image.
- Replaced the weak verifier with tests that validate exact JSON fields and values.
- Corrected verifier outputs to `/logs/verifier/reward.txt` and `/logs/verifier/ctrf.json`.
- Disabled unnecessary Internet access.
