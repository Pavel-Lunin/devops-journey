# Project 04: Bash Toolkit

> **Status:** 🔄 In Progress
> **Phase:** 1 (Месяцы 1–3)
> **Timeline:** Continuous, активная работа с месяца 1

## Goal

Собрать коллекцию production-ready bash-скриптов для повседневной автоматизации: мониторинг состояния VPS, парсинг логов, backup, log rotation, проверки доступности сервисов. Все скрипты — ShellCheck-clean, с понятной структурой, error handling и helpful `--help`.

## Why this matters

Bash-экспертиза — must-have для любой DevOps позиции; это язык, на котором "склеивается" всё остальное. ShellCheck-clean код и аккуратные `set -euo pipefail` показывают внимание к деталям и production mindset. Кроме того, эти скрипты — реальные инструменты, которые я использую ежедневно на VPS, что делает их живым портфолио, а не academic exercise.

## Tech stack

- Bash (target — POSIX-совместимость где возможно)
- ShellCheck (CI-проверка)
- awk, sed, jq (текстовая обработка)
- systemd timers (вместо cron для новых задач)
- cron (для legacy совместимости)

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

Структура папки: `bin/` — исполняемые скрипты, `lib/` — переиспользуемые функции (logging, error handling), `tests/` — bats-тесты, `systemd/` — unit-файлы и timer'ы. Каждый скрипт начинается с заголовка с описанием, usage и зависимостями.

## How to reproduce

[Будет наполнено: `make install`, описание каждого скрипта, требования к среде.]

## Metrics & Results

[Будет наполнено: количество скриптов, % покрытия bats-тестами, ShellCheck score, частота использования по логам.]

## What I learned

[Будет наполнено: idioms `set -euo pipefail`, trap handlers, безопасная работа с пробелами в именах файлов, отличия sh vs bash, ловушки subshell'ов.]

## References

- [ShellCheck](https://www.shellcheck.net/)
- [Bash strict mode](http://redsymbol.net/articles/unofficial-bash-strict-mode/)
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
- [bats-core (Bash Automated Testing System)](https://github.com/bats-core/bats-core)
