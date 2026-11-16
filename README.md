# make.fun Entry Template

A minimal, original starting point for building a
[make.fun](https://make.fun) bounty entry. It gives you a working skeleton —
input handling, a deterministic pipeline, and output writing — so you can
focus on the bounty-specific logic instead of plumbing.

This template is a **starting point, not a submission**. Replace the
placeholder logic in `solve_case()` with your own approach, then follow the
pipeline in [PIPELINE.md](PIPELINE.md) to record, verify, and submit it.

## How it works

```
input/*.in  →  load & validate  →  solve_case()  →  write output/*.out
```

- `main.py` reads every `*.in` JSON file from the input directory.
- Each case is validated (must be a JSON object with a `case` id).
- `solve_case()` computes the output for one case. **This is the function
  you replace** — the default is a trivially simple baseline that echoes
  the input back, so the skeleton runs end-to-end before you write any
  real logic.
- Outputs are written as compact, deterministic JSON (`{"forecasts": [...]}`)
  with sorted keys, so repeated runs are byte-identical.

## Run locally

```sh
# put sample cases in ./sample-input, outputs land in ./sample-output
MAKEFUN_INPUT_DIR=sample-input MAKEFUN_OUTPUT_DIR=sample-output python3 main.py
```

Requires Python 3. Standard library only — no dependencies.

## Test it

```sh
python3 -m py_compile main.py
MAKEFUN_INPUT_DIR=sample-input MAKEFUN_OUTPUT_DIR=sample-output python3 main.py
MAKEFUN_INPUT_DIR=sample-input MAKEFUN_OUTPUT_DIR=sample-output python3 main.py
# the two runs must produce byte-identical files in sample-output/
diff -r sample-output sample-output
```

## Files

| File | What it is |
| --- | --- |
| [main.py](main.py) | The entry skeleton (replace `solve_case()`) |
| [PIPELINE.md](PIPELINE.md) | Record → verify → submit, step by step |
| [.gitignore](.gitignore) | Keeps keys, keypairs, usage files, and credentials out of git |
| [LICENSE](LICENSE) | MIT |

## Rules that matter

- **Original work only.** Write your logic fresh. Reading another entry
  first and then rewriting it from memory poisons authorship — start from
  this template instead.
- **Deterministic.** Same input, same output, every run. No timestamps, no
  randomness, no dict-order dependence in output files.
- **One recording, start to finish.** Start a single recording *before*
  the first build session, and submit from that recording only. See
  [PIPELINE.md](PIPELINE.md).

## License

MIT — see [LICENSE](LICENSE).
