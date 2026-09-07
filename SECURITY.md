# Security Policy

EuroPi is offline, standalone Eurorack module firmware — it has no network stack, no
authentication, and no exposure to untrusted input beyond physical CV/gate signals and files
copied to it over USB. The realistic security surface is limited to the firmware/tooling code
itself (e.g. a crash or hang from malformed save-state files) rather than remote exploitation.

## Reporting a vulnerability

If you find a security issue in this fork specific to `landscape82/EuroPi_Development` (CI/release
automation, workflow permissions, etc.), open a
[GitHub issue](https://github.com/landscape82/EuroPi_Development/issues/new/choose) or contact the
maintainer directly via the email on their GitHub profile.

If the issue also affects upstream firmware/hardware, please report it to
[Allen-Synthesis/EuroPi](https://github.com/Allen-Synthesis/EuroPi) as well — see
[FORK.md](FORK.md) for how issues are split between this fork and upstream.
