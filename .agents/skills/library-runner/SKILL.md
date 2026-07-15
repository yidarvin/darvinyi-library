---
name: library-runner
description: "Build, critique, resolve, and report progress for this queue-built non-fiction library. Use whenever a request says run the next one, run the next N, critique the next one, resolve critiques, queue status, rerun, add, or reprioritize in a repo containing prompts/queue.md and content/registry.json. Terra builds and resolves; Sol independently critiques. Do NOT use for a one-off component edit unrelated to queue state, or for a general README change."
---

# library-runner

Use this repository's lifecycle: `pending → draft → done`. Terra builds a pending
chapter and marks it draft. Sol critiques the draft. Sol alone approves and marks done.
When Sol returns `verdict: revise`, Terra fixes the required findings and sets
`verdict: resolved`; Sol then re-reviews.

## Roles and defaults

- Builder and resolver: `gpt-5.6-terra`, `high` reasoning effort.
- Critic: `gpt-5.6-sol`, `high` reasoning effort.
- The driver owns commits and pushes. Agents never commit or push.
- `npm run check` is mandatory after every action. `scripts/mark.py` is the only way
  to change a chapter status.

## Run the next one

1. Run `python3 scripts/decide.py next` and follow its action.
2. For `build`, read the book brief, authoring spec, and diagram vocabulary. Research
   primary sources, create original prose and diagrams, pass the gate, and mark draft.
3. For `critique`, read the draft and imported components independently. Write an
   append-only critique file with required and advisory findings. Approve only if there
   are no required findings.
4. For `resolve`, apply every required finding, verify previous fixes still hold, pass
   the gate, and append a concrete builder resolution.
5. Use `./runqueue.sh --count 1` to run a full action loop. It commits and pushes each
   clean state transition; use `--no-push` for local-only work.

## Worked example

`thinking-fast-and-slow` begins pending. Terra builds it and `mark.py` changes it to
draft. Sol writes `content/critiques/thinking-fast-and-slow.md`. If Sol approves,
`mark.py` changes it to done and the queue row becomes `DONE`. If Sol revises, Terra
updates only that chapter and records `verdict: resolved`; Sol reviews it again.

## Queue status and changes

- Run `python3 scripts/decide.py status` for the next action and critique counts.
- Add or reorder books in both queue and registry, then run `npm run validate`.
- Never mark a chapter done without an approving critique. Never truncate critique
  history.

## When NOT to use this skill

- A small direct React, CSS, or prose fix outside queue state: no skill, plain editing.
- A general repo document: use technical-writing-and-docs.
- A review of a human-authored diff: use code-review.

## Provenance and maintenance

- Authored and verified: 2026-07-15 against this repo's scripts and Codex CLI 0.144.4.
- Re-verify with:

```bash
bash -n runqueue.sh
python3 scripts/decide.py status
npm run check
python3 /Users/darvin/.agents/skills/skill-authoring-standard/scripts/lint_skill.py --strict .agents/skills/library-runner/SKILL.md
```

- Most likely to change: Codex model IDs, Codex CLI flags, and the queue lifecycle.
