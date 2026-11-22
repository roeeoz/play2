# play2

Second fixture repository for multi-repository factory QA (`greetlib`, a tiny greeting library). Companion of roeeoz/play1.

- `pip install -e ".[test]" && pytest`
- CI: `.github/workflows/ci.yml` (`test` runs pytest; `gate` fails iff a `CI_FAIL` file exists at the root).
