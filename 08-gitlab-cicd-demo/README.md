# Project 08: GitLab CI/CD Demo

> **Status:** 📋 Planned
> **Phase:** 2 (Месяцы 4–6)
> **Timeline:** Месяц 4 (параллельно с проектом 07)

## Goal

Реализовать полный CI/CD pipeline на GitLab CI для тестового приложения: stages `build → test → security scan → deploy`. Использовать GitLab Container Registry для образов, self-hosted GitLab Runner на VPS, Trivy для security scanning, manual approval gate для prod-деплоя.

## Why this matters

GitLab CI доминирует в РФ DevOps — особенно в крупных продуктовых компаниях и финтехе, где self-hosted GitLab часто заменяет GitHub. Демонстрация полного pipeline'a с security gates — top-tier signal для Middle позиций: рекрутёр сразу видит, что кандидат понимает не только "запустить тесты", но и concepts вроде artifacts, caching, environments, manual jobs и rollback.

## Tech stack

- GitLab CI/CD (`.gitlab-ci.yml`)
- Docker (для сборки и runner executor'а)
- GitLab Runner (self-hosted, docker executor)
- GitLab Container Registry
- Trivy (image vulnerability scanning)
- SAST / Secret Detection (встроенные GitLab templates)

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

Pipeline: `lint → build (docker) → test → trivy scan → push to registry → deploy to staging (auto) → deploy to prod (manual approval)`. Self-hosted runner на VPS подхватывает jobs, использует Docker socket binding для сборки образов.

## How to reproduce

[Будет наполнено: пример `.gitlab-ci.yml`, инструкция по регистрации runner'а, требования к GitLab project настройкам.]

## Metrics & Results

[Будет наполнено: длительность pipeline cold / warm, success rate, количество найденных Trivy уязвимостей в типичном образе.]

## What I learned

[Будет наполнено: caching strategies (зависимости vs build artifacts), nuances `rules:` vs `only/except`, security trade-offs Docker-in-Docker vs socket binding.]

## References

- [GitLab CI/CD documentation](https://docs.gitlab.com/ee/ci/)
- [GitLab Runner](https://docs.gitlab.com/runner/)
- [Trivy](https://aquasecurity.github.io/trivy/)
- [GitLab CI/CD best practices](https://docs.gitlab.com/ee/ci/yaml/optimize_pipeline.html)
