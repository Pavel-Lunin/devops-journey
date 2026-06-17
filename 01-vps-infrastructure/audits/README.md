# VPS Audit Snapshots

Каталог хранит read-only снимки состояния production VPS. Эти файлы нужны как evidence для Project 01 и как baseline перед следующими изменениями.

## Snapshots

| Дата | Каталог | Кратко |
|---|---|---|
| 2026-06-15 | `vps-audit-20260615T051516Z/` | Первый полный read-only audit после SSH hardening: systemd, ресурсы, сеть, Docker/AmneziaWG, nginx/Apache, APT, логи, PM2 |

## Правила

- Не хранить secrets: приватные ключи, `.env`, токены, PM2/Docker env.
- Raw audit files не редактировать после загрузки — если вывод устарел, добавить новый snapshot или отдельный addendum.
- Изменения production-сервера фиксировать отдельным runbook'ом в `../runbooks/`.

