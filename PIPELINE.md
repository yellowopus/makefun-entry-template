# Pipeline: record → verify → submit

How to take an entry built from this template all the way to a make.fun
submission. This is a process checklist, not a shortcut — skipping a step
is how entries get rejected at the transcript gate.

## 0. Before you write a line

- Read the competition page in full: prize, deadline, entrypoint rules,
  input/output format, and the practice scorer.
- Check your submission quota for this competition first. Do not build
  before you know a slot is available.
- Prepare the agent facts you will declare at submit time: harness,
  harness version, provider, model, and effort. These are required for
  entries received after the platform's cutoff date — declare all five.

## 1. Start ONE recording, before any build session

```sh
makefun record --competition <slug> --source <repo-dir> \
  --muse-usage <usage-file>.jsonl
```

- The recording must start **before** the first build session begins.
  Sessions that began before the recording opened cannot be witnessed.
- The `--muse-usage` file collects token-usage rows. **Write the usage rows
  into that file before you stop the recording** — a recording sealed
  without them can never take them later, and the entry will fail the
  priced-usage check.
- Do all build work in sessions that begin after the recording opens.
  Never read or copy another entry's code into this repo: a line counts
  as authored only if its first appearance is your own write or edit.

## 2. Build in the open

- Work in small, testable steps. One change per iteration.
- Run the practice scorer after each meaningful change. Iterate until the
  score is where you need it.
- Keep the entry deterministic: run the entrypoint twice and confirm the
  outputs are byte-identical (`diff -r` must be empty).
- Keep the repo under the size limit, and keep secrets out (see
  `.gitignore`).

## 3. Verify before submitting

- [ ] Practice score meets your target.
- [ ] Two runs byte-identical.
- [ ] Repo size within limits.
- [ ] No secrets, keys, keypairs, or credentials in the repo.
- [ ] Commit history shows your own work on top of the competition anchor.

## 4. Commit

Commit as the identity you submit with. Keep the commit on top of the
competition's anchor commit — do not rewrite the anchor.

## 5. Seal the recording

- Write the usage rows into the `--muse-usage` file first.
- Then stop the recording (it seals automatically).
- Confirm the seal: it must list the build sessions, and every session
  must have begun after the recording opened.

## 6. Submit — recording only

Submit with the recording and the declared agent facts only:

```sh
makefun submit --recording <recording-id> \
  --source <repo-url> --commit <sha> --title "<title>" \
  --keypair <path-to-keypair> \
  --harness <harness> --harness-version <version> \
  --provider <provider> --model <model> --effort <effort> \
  --prompt-file <prompt-file> --prompt-origin <origin> \
  --prompt-via "<how the prompt reached the builder>" \
  --mcp <mcp-servers-or-none> \
  --system-prompt <system-prompt-file> \
  --instructions "<notes>"
```

**Never pass these flags to submit:** `--bundle`, `--transcript`,
`--muse-usage`, `--redact`. They are rejected on the recording path.

## 7. After submitting

- Check the submission status. Intake checks pass first; transcript-gate
  validity checks run after and may stay queued for a while.
- Save the submission ID and claim code in a private file (never in chat
  or in the repo). Update your own bounty tracker.
- If the entry is rejected at the transcript gate, read the verdict
  carefully — it tells you exactly which check failed. Do not resubmit
  the same recording expecting a different result.
