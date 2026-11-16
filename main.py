#!/usr/bin/env python3
"""make.fun entry template — deterministic skeleton (stdlib only).

Pipeline (three steps, each independently testable):
  1. load_cases()   — read and validate every ``*.in`` JSON file.
  2. solve_case()   — compute one case's output. TODO: replace this
                      placeholder with the bounty-specific logic.
  3. write_outputs() — write compact, deterministic ``*.out`` JSON.

Input and output directories come from MAKEFUN_INPUT_DIR and
MAKEFUN_OUTPUT_DIR (defaults: /input and /output).

The default solve_case() is a trivial baseline that echoes the case id
back with a null result, so the skeleton runs end-to-end before any real
logic exists. Replace it — do not ship the placeholder as an entry.
"""

from __future__ import annotations

import json
import os
from pathlib import Path


INPUT_DIRECTORY = Path(os.environ.get("MAKEFUN_INPUT_DIR", "/input"))
OUTPUT_DIRECTORY = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
INPUT_GLOB = "*.in"


def load_cases(input_dir: Path) -> list[dict]:
    """Step 1: read and validate every input case, in name order."""
    cases = []
    for input_path in sorted(input_dir.glob(INPUT_GLOB)):
        case = json.loads(input_path.read_text(encoding="utf-8"))
        if not isinstance(case, dict) or "case" not in case:
            raise ValueError(f"{input_path}: expected a JSON object with a 'case' id")
        cases.append(case)
    return cases


def solve_case(case: dict) -> dict:
    """Step 2: compute one case's output.

    TODO: replace this placeholder with the bounty-specific logic.
    Keep it deterministic: same input, same output, every run.
    No timestamps, no randomness, no network access.
    """
    return {"case": case["case"], "result": None}


def write_outputs(output_dir: Path, results: list[dict]) -> None:
    """Step 3: write one compact, deterministic ``*.out`` file per case."""
    output_dir.mkdir(parents=True, exist_ok=True)
    for result in results:
        output_path = output_dir / f"{result['case']}.out"
        output_path.write_text(
            json.dumps({"forecasts": [result]}, sort_keys=True, separators=(",", ":")),
            encoding="utf-8",
        )


def main() -> None:
    cases = load_cases(INPUT_DIRECTORY)
    results = [solve_case(case) for case in cases]
    write_outputs(OUTPUT_DIRECTORY, results)


if __name__ == "__main__":
    main()
