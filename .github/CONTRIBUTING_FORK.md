# Contributing to this fork

This document covers the merge process specific to `landscape82/EuroPi_Development`. For
guidelines on the content of a contribution itself (code style, contrib script format, docs,
testing), see upstream's [contributing.md](../contributing.md) — those still apply here.

## Branch protection on `main`

* All changes land via a pull request — direct pushes to `main` are blocked, including for the
  repo owner, other than an admin override for emergencies.
* A pull request needs:
  * **1 approving review from a code owner** (see [`.github/CODEOWNERS`](CODEOWNERS)).
  * **Passing CI**: the `run_tests / build` and `lint` checks from
    [Continuous Integration](workflows/continuous_integration.yml) must be green, and the branch
    must be up to date with `main` before merging (required checks are `strict`).
* Force-pushes and branch deletion are disabled on `main`.

## Typical flow

```
git checkout main
git pull origin main
git checkout -b <branch-name>
# make changes, commit
git push -u origin <branch-name>
gh pr create --repo landscape82/EuroPi_Development --base main --head <branch-name> \
  --title "..." --body-file <path-to-body>
```

Fill in the PR using [`.github/pull_request_template.md`](pull_request_template.md) — Summary,
What will be applied/fixed, Test steps.

## Syncing with upstream

`main` is periodically fast-forwarded from
[Allen-Synthesis/EuroPi](https://github.com/Allen-Synthesis/EuroPi):

```
git fetch https://github.com/Allen-Synthesis/EuroPi.git main
git merge --ff-only FETCH_HEAD
git push origin main
```

If this isn't a clean fast-forward, it means this fork has diverged with local-only commits on
`main` — resolve that before syncing rather than forcing it.
