# Project 03: Docker RN Builder

> **Status:** 📋 Planned
> **Phase:** 1 (Месяцы 1–3)
> **Timeline:** Фаза 0–1, неделя 2

## Goal

Создать reproducible Docker image для сборки React Native приложений под Android: Android SDK нужных API levels, JDK, Gradle, кэширование зависимостей. Multi-stage build для минимизации финального размера и отделения build-инструментов от runtime.

## Why this matters

Уникальное пересечение Mobile + DevOps экспертизы — на рынке очень мало инженеров, которые умеют правильно контейнеризовать mobile builds. Это даёт прямое применение в рабочей задаче по автоматизации pipeline в Сбере и одновременно служит сильным differentiator при поиске Middle DevOps позиции: "не просто ещё один DevOps, а тот, кто понимает специфику mobile builds".

## Tech stack

- Docker (multi-stage builds, BuildKit)
- Ubuntu base image (slim variant)
- Android SDK / cmdline-tools
- JDK 17
- Gradle (с кэшированием через Docker layer cache)
- React Native CLI

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

Multi-stage layout: `base (Ubuntu + JDK)` → `sdk (Android cmdline-tools + platforms)` → `builder (Gradle + npm deps cache)` → финальный slim image для CI. Параллельно — версия с pre-warmed Gradle cache для ускорения первого билда.

## How to reproduce

[Будет наполнено: `docker build` команды с BuildKit-кэшем, пример сборки тестового RN-проекта, бенчмарк cold vs warm build.]

## Metrics & Results

[Будет наполнено: размер итогового image, время cold build, время warm build, сравнение с локальной сборкой на хосте.]

## What I learned

[Будет наполнено: ловушки Android SDK лицензий, специфика Gradle daemon в контейнере, оптимизация layer caching.]

## References

- [Docker BuildKit](https://docs.docker.com/build/buildkit/)
- [Android cmdline-tools](https://developer.android.com/tools)
- [React Native — Building from source](https://reactnative.dev/contributing/how-to-build-from-source)
