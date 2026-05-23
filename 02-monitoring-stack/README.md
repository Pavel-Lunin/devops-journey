# Project 02: Monitoring Stack

> **Status:** 📋 Planned
> **Phase:** 1 (Месяцы 1–3)
> **Timeline:** Месяц 2

## Goal

Развернуть на VPS стек мониторинга Prometheus + Grafana + Node Exporter с базовыми dashboard'ами (CPU, RAM, disk, network) и алертингом через Alertmanager (минимум — Telegram-канал).

## Why this matters

Observability — обязательное требование для любой Middle DevOps позиции. Без понимания, что значит "наблюдать за системой", невозможно говорить об SLO/SLA, post-mortem'ах и production-ownership. Этот проект также даёт прямой transfer skills в рабочую задачу: добавление мониторинга в Jenkins-based mobile CI/CD pipeline на текущей работе.

## Tech stack

- Prometheus (метрики, scrape, PromQL)
- Grafana (dashboard'ы, alerting UI)
- Node Exporter (system metrics)
- Alertmanager (routing алертов)
- Docker Compose (оркестрация локального стека)
- nginx (reverse proxy перед Grafana с TLS)

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

Высокоуровневая схема: Node Exporter на VPS → Prometheus (scrape каждые 15s) → Grafana (visualization) + Alertmanager (routing). Всё в docker-compose, persistence через volumes, доступ снаружи только через nginx + Basic Auth + TLS.

## How to reproduce

[Будет наполнено: `docker-compose up -d`, конфиги Prometheus / Alertmanager, JSON dashboard'ов, инструкция по импорту.]

## Metrics & Results

[Будет наполнено: количество метрик, latency scrape, размер TSDB через месяц, время реакции на синтетический алерт.]

## What I learned

[Будет наполнено: PromQL idioms, label cardinality, отличия pull vs push, как НЕ настраивать алерты.]

## References

- [Prometheus documentation](https://prometheus.io/docs/)
- [Grafana documentation](https://grafana.com/docs/)
- "Prometheus: Up & Running" — Brian Brazil
- [Awesome Prometheus alerts](https://samber.github.io/awesome-prometheus-alerts/)
