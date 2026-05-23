# Project 01: VPS Infrastructure

> **Status:** 🔄 In Progress
> **Phase:** 1 (Месяцы 1–3)
> **Timeline:** Месяц 1 — первый завершённый проект на пути

## Goal

Задокументировать существующий self-hosted VPS-стек: nginx как reverse proxy перед apache backend, Amnezia VPN endpoint, TLS, firewall (ufw). Превратить tribal knowledge в воспроизводимую документацию с диаграммами, конфигами и runbook'ами.

## Why this matters

Демонстрирует production-ready понимание инфраструктуры ещё до начала формального DevOps пути — это сильный signal для рекрутёров. Hands-on опыт с Linux, networking и web servers — фундамент, без которого следующие проекты (мониторинг, IaC, Kubernetes) не имеют смысла. Документация этого стека также становится reference-точкой для проектов 02 (мониторинг), 06 (Terraform-переписывание) и 07 (Ansible-роли).

## Tech stack

- Ubuntu Linux (server LTS)
- nginx (reverse proxy, TLS termination)
- apache2 (backend)
- systemd (управление сервисами)
- OpenSSL / Let's Encrypt (TLS)
- Amnezia VPN (VPN endpoint)
- ufw (firewall)

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

Высокоуровневая схема: `client → nginx (443/TLS) → apache (127.0.0.1:8080) → app`; параллельно Amnezia VPN endpoint на отдельном порту; ufw закрывает всё лишнее.

## How to reproduce

[Будет наполнено по мере работы над проектом. Цель — пошаговый runbook, по которому можно поднять идентичный стек на чистой Ubuntu VM.]

## Metrics & Results

[Будет наполнено: uptime, время восстановления после reboot, размер конфигурации, количество runbook-страниц.]

## What I learned

[Будет наполнено: ключевые insights об nginx upstream'ах, TLS-настройке, специфике Amnezia, ошибках при конфигурации firewall.]

## References

- [nginx documentation](https://nginx.org/en/docs/)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)
- [ufw man page](https://manpages.ubuntu.com/manpages/jammy/en/man8/ufw.8.html)
- [Amnezia VPN](https://amnezia.org/)
