# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **public learning journal**, not a software product. It is a 12-month, scaffolded plan for a Senior Mobile Engineer (RN, 6y, Сбер) to transition into a Middle DevOps Engineer role on the РФ market. Each top-level numbered directory is a self-contained portfolio project. Most projects are still 📋 Planned and currently contain only a README — there is no build system, test runner, lint config, or executable code in the repo today.

When the user asks you to "start" or "work on" a project, the expectation is to begin filling in that project's directory with real artifacts (configs, scripts, Terraform modules, Ansible roles, Dockerfiles, etc.), not to look for an existing codebase.

## Language and audience

- README, learning-log entries, project descriptions, and interview-prep materials are written in **Russian** (mixed with English technical terms). Match that style when editing those files — do not translate existing Russian content to English.
- The repository is public (github.com/Pavel-Lunin/devops-journey) and also serves as a portfolio for recruiters. Tone in committed files is professional and recruiter-facing; avoid sloppy phrasing or placeholder "TODO" left in shipped READMEs.

## Repository structure (the big picture)

The structure encodes the 12-month roadmap. Read the root [README.md](README.md) Roadmap and Projects tables first — they are the source of truth for what each numbered dir is for, what phase it belongs to, and the dependency order between projects (e.g. project 01 documents the VPS stack that projects 06/07 will later reproduce via Terraform / Ansible).

Top level:
- `01-vps-infrastructure/` … `10-mobile-cicd-patterns/` — ten portfolio projects, each with its own README, status badge, phase, and "Goal / Why / Tech stack / Architecture / How to reproduce / Metrics / What I learned / References" template. **Preserve this section template** when editing project READMEs.
- `learning-log/` — weekly journal entries (`YYYY-week-NN.md`) using the template in `2026-week-21.md`. One file per ISO week.
- `interview-prep/` — `system-design/` and `star-stories/` for РФ DevOps interviews.
- `certificates/` — PDFs/screenshots of obtained certs (currently empty); README tracks the certification roadmap (YC Associate → AWS SAA → CKA).

## Conventions to follow when adding content

- **Project READMEs:** keep the exact section headings shown in [01-vps-infrastructure/README.md](01-vps-infrastructure/README.md) (Goal, Why this matters, Tech stack, Architecture, How to reproduce, Metrics & Results, What I learned, References). Status line at the top uses the legend `📋 Planned · 🔄 In Progress · ✅ Complete`. If a project's status changes, also update the Projects table in the root README.
- **Bash scripts (project 04 and any auxiliary scripts):** target ShellCheck-clean, start with `set -euo pipefail`, include a header comment with usage and dependencies. Project layout for `04-bash-toolkit/` is intended to be `bin/` (executables) + `lib/` (shared functions) + `tests/` (bats) + `systemd/` (units/timers).
- **Secrets:** `.gitignore` already excludes `.env*`, `*.pem`, `*.key`, `*.crt`, `secrets/`, `*.tfvars` (except `.example`), `.vault_pass`, `inventory.local`, and `service-account*.json`. When adding examples, use the `.example` suffix so the ignore allowlist picks them up.
- **Terraform / Ansible:** state files, `.terraform/`, `*.retry`, and real `*.tfvars` are gitignored. Commit only `*.tfvars.example` and sanitized inventories.

## Git / remote

Pushes to `origin` use SSH with a dedicated key (`id_ed25519_github_anon`). `core.sshCommand` is already configured locally — do not change git remote URL or SSH config when committing.

## What NOT to do

- Do not invent build/test/lint commands — there is no package manifest, Makefile, or CI config yet. If the user asks "how do I run tests", the honest answer is "no test infrastructure exists in this repo yet; project 04 plans to use bats".
- Do not scaffold a project's full directory tree speculatively. Add files only when the user is actively working on that project — premature scaffolding pollutes the journal.
- Do not delete the "будет наполнено" / placeholder sections in planned-project READMEs unless you're filling them in with real content from work just completed.
