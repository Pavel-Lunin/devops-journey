# Project 05: Yandex Cloud Setup

> **Status:** 📋 Planned
> **Phase:** 1 (Месяцы 1–3)
> **Timeline:** Месяц 3

## Goal

Перенести VPS-setup из проекта 01 на Yandex Cloud, выполнив всё руками через web console и `yc` CLI: VPC + subnets, Compute Instance, Network Load Balancer, Object Storage bucket для статики, IAM service accounts с минимальными правами.

## Why this matters

Yandex Cloud — основной cloud РФ-рынка, упоминается в большинстве вакансий tier-1 компаний. Hands-on опыт через консоль и CLI ценится выше теоретических знаний на интервью: рекрутёры различают "читал доки" и "поднимал руками". Этот проект также служит baseline'ом для проекта 06 (тот же setup, но уже через Terraform) — что даёт честный side-by-side: imperative vs declarative.

## Tech stack

- Yandex Cloud Compute (VM с публичным IP)
- Yandex Cloud VPC (network, subnets, security groups)
- Yandex Cloud Network Load Balancer
- Yandex Cloud Object Storage (S3-compatible)
- Yandex Cloud IAM (service accounts, минимальные роли)
- `yc` CLI

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

Высокоуровневая схема: `Internet → NLB → Compute Instance (nginx + apache, реплика setup'a из 01) → Object Storage (для статики)`. Отдельный service account для деплоя с правами только на нужные ресурсы.

## How to reproduce

[Будет наполнено: пошаговая инструкция с скриншотами консоли и эквивалентными `yc` командами; cost-оценка месячного хостинга.]

## Metrics & Results

[Будет наполнено: время setup, ежемесячная стоимость, latency vs текущий VPS.]

## What I learned

[Будет наполнено: специфика YC IAM-модели, ограничения free tier, отличия от AWS-подходов, на что обратить внимание при бюджетировании.]

## References

- [Yandex Cloud documentation](https://yandex.cloud/docs)
- [yc CLI reference](https://yandex.cloud/docs/cli/)
- [YC IAM concepts](https://yandex.cloud/docs/iam/concepts/)
