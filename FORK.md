# About this fork

This repository (`landscape82/EuroPi_Development`) is a development fork of
[Allen-Synthesis/EuroPi](https://github.com/Allen-Synthesis/EuroPi), the original EuroPi project by
Rory Allen / Allen Synthesis.

`main` here is kept in sync with upstream `main` via fast-forward merges, so it should generally
match upstream unless a fork-specific change is in progress that hasn't been merged upstream yet.

## Where to send things

* **Bugs/features relevant to the EuroPi module in general** (hardware, firmware behaviour,
  contrib scripts) should go to the
  [upstream repository](https://github.com/Allen-Synthesis/EuroPi/issues/new/choose) so the wider
  community benefits, per the [upstream contribution guidelines](contributing.md).
* **Changes specific to this fork** (this repo's own CI/branch-protection setup, experiments not
  yet ready to send upstream, personal build tweaks) belong here, as an issue or PR against this
  repository.

## Licensing note

Per the [licenses](README.md#license) this project ships under (Apache 2.0 for software,
CERN-OHL-S v2 for hardware, CC0 1.0 for documentation), modifying and redistributing an independent
build from this fork is permitted. The one thing upstream explicitly asks: don't use the
'Allen Synthesis' brand name on builds derived from modified files (CERN-OHL-S v2 §8.2).

## Working on this repo

See [`.github/CONTRIBUTING_FORK.md`](.github/CONTRIBUTING_FORK.md) for this repo's own
branch-protection and PR/CI workflow.

## Changelog

[`CHANGELOG.md`](CHANGELOG.md) stopped being updated at version 0.6.1. The changelog of record for
anything since — including this fork's own releases — is the
[Releases page](https://github.com/landscape82/EuroPi_Development/releases), generated
automatically from merged PRs.

## Security

See [`SECURITY.md`](SECURITY.md) for how to report a vulnerability.
