# Project 10: Mobile CI/CD Patterns

> **Status:** 📋 Planned
> **Phase:** Continuous — обновляется по мере накопления опыта
> **Timeline:** Throughout 12-month journey

## Goal

Собрать коллекцию обезличенных architectural patterns и lessons learned из рабочего опыта с mobile CI/CD на enterprise scale: organisation pipeline'ов, артефакт-менеджмент, кэширование, distribution, codesigning, мульти-app monorepo, fastlane lanes, оркестрация через Jenkins. Без компании-specific деталей и кода, только generic паттерны.

## Why this matters

Уникальный angle на пересечении Mobile + DevOps: на DevOps-рынке это редкая комбинация и сильный differentiator против "standard" Middle DevOps кандидатов. Качественные generic patterns без NDA-нарушений — ценный контент и для community, и для рекрутёров: показывает, что я умею не просто writing scripts, а думать архитектурно. Также материал служит базой для STAR-stories на интервью (см. `../interview-prep/star-stories/`).

## Tech stack

- Markdown (статьи и патт-описания)
- Mermaid / Excalidraw (диаграммы)
- Структурированные шаблоны под каждый паттерн

## Architecture

> Архитектурные диаграммы будут в `diagrams/` — отдельно по каждому паттерну (Mermaid inline, для сложных — Excalidraw `.png`)

Структура: каждый паттерн — отдельный markdown-файл со схемой `Problem → Forces / Constraints → Solution → Trade-offs → When NOT to use`. Это формат, заимствованный из классического pattern-language подхода — рекрутёры и инженеры читают такое быстро.

## How to reproduce

Не применимо — это не код, а knowledge base.

## Metrics & Results

[Будет наполнено: количество описанных паттернов, охват тем (build / test / distribute / sign / monitor), внешний фидбек если будет публикация на Хабре / в блоге.]

## What I learned

[Будет наполнено: накопительная рефлексия о том, как mobile CI/CD отличается от backend CI/CD, какие концепции переносятся напрямую, а какие требуют адаптации.]

## References

- "Continuous Delivery" — Jez Humble, David Farley
- [Fastlane documentation](https://docs.fastlane.tools/)
- [Pattern-Oriented Software Architecture (POSA)](https://en.wikipedia.org/wiki/Pattern-Oriented_Software_Architecture) — формат описания паттернов
