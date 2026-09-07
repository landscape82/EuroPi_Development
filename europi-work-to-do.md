# Work to do

Roadmap for this fork, built from the repo audit and a review of upstream's open issues
([Allen-Synthesis/EuroPi/issues](https://github.com/Allen-Synthesis/EuroPi/issues)). Not a
changelog — see [FORK.md](FORK.md) for where that lives. Update this file as items are picked up
or closed out.

## Already resolved on this fork (nothing to do)

Two of upstream's five open issues turned out to already be fixed here, from earlier work this
session:

- **[upstream #478](https://github.com/Allen-Synthesis/EuroPi/issues/478) — Pico detection method
  always falls back to GP24 method.** Exact match for the bug fixed in
  `software/firmware/europi_hardware.py` (`PICO_MODEL == "pico2"` vs. the real value `"pico 2"`).
  Fixed and tested here; not yet contributed back upstream — worth opening an upstream PR since
  it's a small, self-contained, already-verified fix.
- **[upstream #310](https://github.com/Allen-Synthesis/EuroPi/issues/310) — CI fails when using
  `time` module in `firmware/experimental`.** Exact match for the `time`/`utime` mocking gap
  fixed via the global `mock_time_module` autouse fixture in `software/tests/conftest.py`. Also
  worth contributing back upstream — it's a test-infra fix, not a firmware behavior change, so
  low risk to send.

## Upstream issues to watch, not act on yet

- **[upstream #444](https://github.com/Allen-Synthesis/EuroPi/issues/444) — Lower the Pico 2
  overclock from 300MHz to 275MHz.** Our config (`europi_config.py`) currently matches upstream's
  300MHz. The upstream maintainer's latest comment (2026-03-23) is leaning toward *not* just
  lowering the default, but adding a `CPU_FREQ_HZ` override field so users can tune it themselves
  while keeping 300MHz as-is for boards that handle it fine. Implementing a blanket 275MHz change
  now would contradict where that discussion is heading — wait for upstream to settle on an
  approach before touching this.
- **[upstream #467](https://github.com/Allen-Synthesis/EuroPi/issues/467) — Pico W runs out of
  space installing the contrib package via `mip`/package manager.** A real memory-budget problem
  (stripping comments/whitespace from shipped files, conditionally excluding wireless-only files
  on non-W boards, etc.), actively being explored upstream. Non-trivial and best left to upstream
  since it likely needs build-process changes shared across the whole project, not just this fork.
- **[upstream #456](https://github.com/Allen-Synthesis/EuroPi/issues/456) — Add software support
  for input-detection hardware on the new SMD board revision.** Needs the physical new-revision
  hardware to test against (binary-pulse detection tuning, false-positive risk) — not actionable
  without that hardware in hand.

## Code

- **Investigate `firmware/bootloader.py:122`** — self-flagged TODO
  (`self.save_state()  # TODO: isn't this the wrong state?`) around save/load of user config.
  Plan: read the full save/load flow to see what state is actually active at that call site vs.
  what should be saved, check upstream history/issues for prior context, write a test that proves
  current behavior (right or wrong) before changing anything, then fix + test on its own
  branch/PR if it's confirmed broken.
- **Close test-coverage gaps**, lowest-effort/highest-value first — most of
  `firmware/experimental/*` and `firmware/tools/*` sit at 2–33% coverage (e.g. `euclid.py` 2%,
  `bisect.py` 13%, `thread.py` 7%, `math_extras.py` 12%). Plan: one small PR per module, starting
  with modules that have real logic rather than thin wrappers. Skip trying to fully cover the ~30
  `software/contrib/*.py` user scripts beyond the existing import-smoke test in `test_menu.py` —
  low value for the effort; at most cover 2-3 of the more complex ones if it becomes worthwhile.

## Documentation / CI

Nothing outstanding here as of this writing — CI hardening (docs build gated on PRs, deduped
triggers, timeouts, concurrency, extended dependabot) and doc gaps (changelog note,
`SECURITY.md`) were closed out earlier. Add new items here as they come up.
