# Project 01: VPS Infrastructure

> **Status:** 🔄 In Progress
> **Phase:** 1 (Месяцы 1–3)
> **Timeline:** Месяц 1 — первый завершённый проект на пути

## Goal

Задокументировать существующий self-hosted VPS-стек: nginx как reverse proxy перед Apache backend (три vhost'а), AmneziaWG VPN endpoint в Docker, Node.js Telegram-бот под управлением PM2. Превратить tribal knowledge в воспроизводимую документацию с диаграммой, конфигами и списком известных дефектов конфигурации, которые планируется устранить в следующих итерациях.

## Why this matters

Демонстрирует production-ready понимание инфраструктуры ещё до начала формального DevOps пути — это сильный signal для рекрутёров. Hands-on опыт с Linux, networking, web-серверами, Docker и VPN — фундамент, без которого следующие проекты (мониторинг, IaC, Kubernetes) не имеют смысла. Документация этого стека также становится reference-точкой для проектов 02 (мониторинг), 06 (Terraform-переписывание) и 07 (Ansible-роли).

## Tech stack

- **OS:** Ubuntu 24.04.3 LTS (Noble), kernel 6.8, гипервизор KVM
- **Web edge:** nginx 1.24 (reverse proxy, upstream round-robin)
- **Web backend:** Apache 2.4 (три виртхоста на портах 8080/8081/8082, статика из `/var/www/html`)
- **Container runtime:** Docker 29.1 / containerd
- **VPN:** AmneziaWG (`wireguard-go` / `amneziawg-go` в userspace внутри контейнеров) + unbound DNS
- **App runtime:** Node.js v24 (через NVM) + PM2 (cluster/process manager, autostart через `pm2-devops.service`)
- **Init / service manager:** systemd (включая `pm2-devops.service` для PM2 resurrection)
- **Firewall:** ufw (enabled)
- **DNS resolver:** systemd-resolved
- **Provider:** FirstByte (FirstVDS), 2 vCPU / 1.9 GiB RAM / 19.5 GB ext4

## Architecture

```
              ┌───────────────────────── Public Internet ─────────────────────────┐
              │                          │                          │             │
              │ TCP :80                  │ UDP :42817               │ UDP :34367  │ TCP :22
              ▼                          ▼                          ▼             ▼
        ┌──────────┐               ┌──────────────┐          ┌──────────────┐  sshd
        │  nginx   │               │  amnezia-awg │          │ amnezia-awg2 │
        │ (proxy)  │               │ (Docker, wg) │          │ (Docker, wg) │
        └────┬─────┘               └──────┬───────┘          └──────┬───────┘
             │ upstream round-robin       │                         │
             │ → 127.0.0.1:{8080..8082}   └────────┬────────────────┘
             ▼                                     ▼
        ┌─────────────────────────┐       ┌────────────────┐
        │ apache2 (3 vhosts)      │       │  amnezia-dns   │
        │ DocumentRoot            │       │  (unbound)     │
        │ /var/www/html (static)  │       │  bridge:       │
        └─────────────────────────┘       │  amnezia-dns-  │
                                          │  net (Docker)  │
                                          └────────────────┘

        Поверх хоста, отдельно от Docker:
        ┌───────────────────────────────────────────────┐
        │ PM2 (systemd: pm2-devops.service)             │
        │   ├── fate-bot-production  (telegraf bot)     │
        │   └── fate-bot-staging                        │
        └───────────────────────────────────────────────┘
```

Сетевые интерфейсы: `ens3` (публичный), `docker0` (172.17.0.0/16, дефолтный bridge), `amn0` (172.29.172.0/24, кастомный bridge `amnezia-dns-net` для VPN-стека), несколько `veth*` пар на контейнер.

Диаграмма в графическом виде — `diagrams/architecture.png` (TODO, отрисовать в draw.io / Excalidraw).

## How to reproduce

Полный пошаговый runbook будет собран по мере работы над **project 07 (Ansible)** — именно там этот стек кодифицируется в roles и playbook'и. Сейчас фиксируется фактическое состояние; reproducibility — следующий этап.

Минимальный набор шагов на чистой Ubuntu 24.04 (high-level):

1. Базовый hardening: создать non-root sudoers, развернуть SSH-ключи, **отключить `PasswordAuthentication` и `PermitRootLogin`** (на действующем сервере оба сейчас включены — см. раздел *What I learned*).
2. `apt install nginx apache2 ufw docker.io` + NVM + Node.js + `npm i -g pm2`.
3. Apache: три vhost'а на 8080/8081/8082, в идеале на `127.0.0.1:*` вместо `*:*`.
4. nginx: server-блок на :80 с `upstream` round-robin на три Apache-порта.
5. ufw: разрешить только `22/tcp`, `80/tcp` (+ `443/tcp` после получения сертификата), и UDP-порты AmneziaWG.
6. Docker-compose / отдельные Dockerfile'ы для `amnezia-awg`, `amnezia-awg2`, `amnezia-dns` (исходники лежат в `/opt/amnezia/*` на текущем хосте).
7. `pm2 start ecosystem.config.json --env production && pm2 save && pm2 startup systemd` для автозапуска бота.

## Metrics & Results

| Метрика | Значение |
|---|---|
| Uptime сервера на момент диагностики | 113 дней непрерывной работы |
| Аптайм Apache | 13 дней (без рестартов после последнего конфига) |
| Аптайм AmneziaWG (основной endpoint) | 3 месяца |
| Использование диска (root ext4) | 5.6 G из 18 G (32%) |
| Использование RAM | ~900 MiB из 1.9 GiB; **swap не настроен** |
| Load average (1/5/15 min) | 0.08 / 0.17 / 0.16 |
| Трафик через основной VPN endpoint | ~3.7 TB in / ~3.9 TB out за 3 месяца |
| Установлено APT-пакетов | 360 |
| Доступно обновлений | 38 (1 — security) |

## What I learned

Главный вывод диагностики: **production VPS, отработавший без перезагрузки 113 дней, при этом имеет несколько системных недочётов, которые нельзя увидеть, пока специально не пройдёшься чек-листом.** Этот разрыв между «работает» и «настроено правильно» — и есть зона роста, ради которой делается весь journal.

Конкретно зафиксировано (и пойдёт в backlog исправлений):

- **TLS не настроен** — nginx слушает только :80, сертификата Let's Encrypt нет. Это первое, что нужно поднять (certbot + автообновление).
- **SSH-конфигурация слабая:** `PasswordAuthentication yes` + drop-in cloud-init с `PermitRootLogin yes` оставляют поверхность атаки. `/var/log/btmp` за время аптайма распух до **451 MB** неудачных попыток входа — наглядная иллюстрация, почему fail2ban + ключи-only это не теория.
- **Apache торчит наружу** на портах 8080/8081/8082 (bind на `*`, не `127.0.0.1`). Архитектурно правильно — оставить наружу только nginx, бэкенд держать на loopback. Это правится одной строкой в `ports.conf`.
- **Swap отсутствует** при 1.9 GiB RAM. При пике (например, рост памяти у Node.js + AmneziaWG-userspace процессов) — гарантированный OOM-kill. Минимум 1–2 GiB swap-файла стоит добавить.
- **PM2-процессы бота в статусе `stopped`** при включённом `pm2-devops.service` — расхождение между saved-state и runtime. Урок: PM2 без мониторинга это «думаю, что работает».
- **38 непримененных обновлений** (включая `containerd 1.7 → 2.2`, `gnutls`, `apparmor`). Unattended-upgrades либо не настроены, либо настроены не на тот набор.
- **userspace WireGuard** (`wireguard-go` через AmneziaWG) — отдельная категория знаний: модуль ядра `wireguard` не подгружен, всё работает в userspace внутри контейнеров с монтированием `/lib/modules`. Это компромисс ради DPI-resistance, но он стоит ~317 MiB RAM и ~8500 CPU-minutes за 3 месяца.

Эти пункты становятся roadmap'ом для project 07 (Ansible-роли): каждое исправление должно быть кодифицировано как идемпотентная роль, а не разовый ручной фикс.

## References

- [nginx documentation](https://nginx.org/en/docs/) — upstream-блоки, proxy_pass
- [Apache 2.4 docs: VirtualHost](https://httpd.apache.org/docs/2.4/vhosts/) — vhost-настройка и `Listen` директивы
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/) — пригодится при добавлении TLS
- [ufw man page](https://manpages.ubuntu.com/manpages/jammy/en/man8/ufw.8.html)
- [Amnezia / AmneziaWG](https://amnezia.org/) — userspace WireGuard с DPI-resistance
- [PM2 + systemd integration](https://pm2.keymetrics.io/docs/usage/startup/) — `pm2 startup systemd` + `pm2 save`
- [Lynis](https://cisofy.com/lynis/) — security audit tool, понадобится для следующей итерации hardening'а
