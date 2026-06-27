# Learning Roadmap: Senior React Native -> Mobile DevOps / DevSecOps

Этот документ - живая траектория обучения. Его цель не в том, чтобы "выучить весь DevOps", а в том, чтобы последовательно нарастить фундаментальные DevOps-компетенции через реальные практические контуры:

- рабочий mobile CI/CD pipeline в Сбере;
- production VPS с AmneziaWG, Docker, systemd, logs, monitoring и security hardening;
- Telegram-бот как pet-service для CI/CD, deployment, observability и security-практик;
- публичный `devops-journey` как портфолио и журнал решений.

Ориентир по темам - [roadmap.sh/devops](https://roadmap.sh/devops): Linux, networking, Git, scripting, CI/CD, containers, configuration management, infrastructure as code, cloud, monitoring/logging, security, Kubernetes. В этой карте темы переупорядочены под текущий контекст: React Native, Jenkins, Vault, Nexus/SberOSC, MAST и эксплуатация собственного VPS.

## Целевая Позиция

Основной вектор: **Mobile DevOps / Platform Engineer с уклоном в DevSecOps**.

Почему это сильнее, чем абстрактный "DevOps Engineer":

- есть 6+ лет production-опыта в React Native и native mobile build systems;
- есть рабочая задача на стыке mobile, CI/CD, Jenkins, Vault, Nexus/SberOSC и clean builders;
- есть реальный VPS, где можно учить Linux, Docker, networking, monitoring, security и IaC;
- есть опыт устранения MAST-уязвимостей по отчётам security-команды;
- есть понятная ниша для РФ и международного рынка: mobile delivery, platform engineering, secure CI/CD.

## Практические Контуры

### 1. Работа: Mobile CI/CD В Сбере

Главный учебный проект. Всё, что можно применить на работе, имеет больший вес, чем учебный pet-project.

Зоны практики:

- Jenkins pipeline для React Native CLI;
- iOS и Android build stages на чистых сборщиках;
- подготовка проекта к корпоративным источникам зависимостей;
- Nexus / SberOSC;
- Vault и безопасная выдача секретов;
- MAST gate и remediation уязвимостей;
- артефакты сборки, публикация, traceability;
- метрики pipeline: длительность, частота падений, причины падений, queue time.

### 2. VPS: Production Linux Playground

Второй по важности контур. Здесь можно безопасно, но по-настоящему учить эксплуатацию.

Зоны практики:

- SSH, sudoers, users, systemd;
- Docker и контейнеры AmneziaWG;
- firewall, listening ports, basic networking;
- journald, log retention, weekly reports;
- monitoring и alerting;
- backup и server-state в git;
- security hardening;
- Ansible/Terraform в следующих фазах.

### 3. Telegram-Бот: Pet-Service

Сервис, на котором удобно отрабатывать delivery-практики end-to-end.

Зоны практики:

- Dockerfile;
- healthcheck;
- CI pipeline;
- deploy script;
- secrets через `.env.example` и внешнее хранилище;
- logs, metrics, alerts;
- vulnerability scanning;
- rollback.

### 4. Public Portfolio

Публичный репозиторий должен показывать не "я учил DevOps", а "я решал production-like задачи и документировал решения".

Артефакты:

- runbooks;
- architecture diagrams;
- sanitized Jenkins patterns;
- ADR;
- incident/postmortem notes;
- before/after метрики;
- Terraform/Ansible modules;
- monitoring dashboards screenshots или описания.

## Принципы Обучения

- Практика первична: каждая тема должна завершаться изменением в VPS, боте или рабочем pipeline.
- Теория нужна перед действием, но не вместо действия.
- Не учить Kubernetes до того, как стали уверенными Linux, Docker, CI/CD, networking и monitoring.
- Не делать cloud ради cloud: сначала понять локально, потом переносить в Yandex Cloud/AWS.
- Каждая рабочая задача должна превращаться в обезличенный публичный паттерн.
- Каждое улучшение должно иметь критерий готовности: метрика, runbook, тест, dashboard, pipeline result.
- Security изучать сразу, но без паралича: secrets, least privilege, dependency trust, MAST, SCA, container scan.

## Режим Наставничества

Эта траектория проходится в формате "учитель / старший товарищ". Цель - не просто выполнить команды, а добиться понимания: что проверяем, зачем это нужно, какой риск есть у действия, как откатиться и как объяснить результат другому инженеру.

Правила работы:

- Перед каждой группой практических команд формулируем цель: что хотим узнать или изменить.
- Production VPS трогаем осторожно: сначала read-only диагностика, затем план, затем минимальное изменение, затем проверка.
- Если команда может повлиять на доступность VPN, Docker, firewall, routing или SSH-доступ, сначала отдельно обсуждаем риск.
- После практики фиксируем вывод: что стало понятнее, что осталось непонятным, какой артефакт появился.
- Для каждой темы есть контрольные вопросы. Тема считается закрытой только когда ответы понятны своими словами.
- Если разговор уходит от глобальной цели или контекст становится слишком большим, открываем новую ветку чата и начинаем с ссылки на этот файл.

Как будет проходить обучение:

1. Короткая теория на 10-15 минут.
2. Разбор на твоём VPS или рабочем CI-контексте.
3. Практическое задание руками.
4. Проверка результата.
5. Мини-конспект в `learning-log`.
6. Обновление backlog/roadmap, если появились новые выводы.

Минимальный формат ответа ученика после задания:

```md
Что сделал:
Что увидел:
Что понял:
Что не понял:
Какая команда была самой важной:
```

## Фаза 0. Инвентаризация И Фундамент

Срок: 2 недели.

Цель: зафиксировать текущее состояние знаний, VPS, рабочего pipeline и бота. Не углубляться в новые инструменты до базовой карты.

### Темы

- Как устроен Linux-сервер: users, groups, permissions, services, logs.
- Как читать состояние системы: `systemctl`, `journalctl`, `ss`, `df`, `free`, `docker ps`.
- Как читать pipeline: stages, agents, credentials, artifacts, external systems.
- Как документировать инфраструктуру без раскрытия secrets.

### План Занятий

#### Урок 0.1. Карта VPS

Цель: понять, из каких крупных частей состоит сервер и как они связаны.

Что разбираем:

- что такое VPS и где проходит граница ответственности провайдера и владельца сервера;
- публичный IP, SSH-доступ, users;
- Docker и контейнеры AmneziaWG;
- nginx/apache, если они ещё используются;
- systemd services и timers;
- server-state в git;
- weekly report.

Практическое задание:

- подключиться к серверу;
- выполнить read-only команды: `hostnamectl`, `uptime`, `df -hT`, `free -h`, `systemctl --failed --no-pager`, `docker ps`;
- своими словами описать, что делает каждая команда;
- нарисовать простую схему: Internet -> VPS -> SSH/Docker/Amnezia/Web/Bot.

Критерии готовности:

- можешь объяснить, что на сервере является сервисом, что контейнером, что конфигом, что логом;
- можешь назвать 3 вещи, которые нельзя менять без плана: SSH, firewall/routing, Docker/Amnezia.

#### Урок 0.2. SSH И Доступ

Цель: понять, как ты попадаешь на сервер и почему SSH hardening важен.

Что разбираем:

- private key и public key;
- `devops` vs `root`;
- `PasswordAuthentication`;
- `PermitRootLogin`;
- `sudoers`;
- временный `Match Address` для Amnezia;
- риск потерять активный доступ.

Практическое задание:

- показать, каким пользователем ты вошёл: `whoami`, `id`;
- посмотреть SSH config grep-ом без вывода secrets;
- найти в логах успешный вход;
- объяснить, почему `systemctl reload ssh` безопаснее, чем необдуманный restart.

Критерии готовности:

- можешь объяснить разницу между key-based login и password login;
- понимаешь, зачем временный `Match Address` нужно удалить после решения Amnezia;
- знаешь, где смотреть SSH-логи.

#### Урок 0.3. systemd: Services И Timers

Цель: понять, как Linux запускает и контролирует фоновые процессы.

Что разбираем:

- `service`;
- `timer`;
- `enabled` vs `active`;
- `start`, `stop`, `reload`, `restart`, `status`;
- failed units;
- наши timers: weekly report, `clear-btmp`, `vps-log-retention`.

Практическое задание:

- посмотреть список failed units;
- посмотреть статус `ssh`, `docker`, `clear-btmp.timer`, `vps-log-retention.timer`;
- объяснить, чем timer отличается от cron;
- найти следующий запуск timer.

Критерии готовности:

- можешь прочитать `systemctl status`;
- понимаешь, почему `restart docker` опасен для Amnezia;
- можешь объяснить, как weekly email report запускается по расписанию.

#### Урок 0.4. Логи И Диагностика

Цель: научиться не гадать, а проверять состояние сервера через логи.

Что разбираем:

- `journalctl`;
- `/var/log`;
- `btmp`, `wtmp`, `lastlog`;
- log retention;
- weekly report;
- как искать проблему по времени.

Практическое задание:

- найти последние SSH-события;
- посмотреть размер `/var/log`;
- посмотреть `journalctl --disk-usage`;
- объяснить, как сейчас удаляются логи старше 7 дней.

Критерии готовности:

- можешь найти логи конкретного сервиса;
- можешь проверить, был ли failed unit;
- понимаешь разницу между текущим логом и архивом.

#### Урок 0.5. Docker И AmneziaWG

Цель: понять, что VPN работает в контейнерах и как смотреть его состояние без риска.

Что разбираем:

- Docker image, container, network, port mapping;
- `docker ps`;
- `docker logs`;
- `docker stats`;
- AmneziaWG containers;
- почему не делаем `docker restart` без maintenance window.

Практическое задание:

- посмотреть `docker ps`;
- посмотреть `docker stats --no-stream`;
- найти UDP-порты Amnezia;
- проверить, какие контейнеры в сети `amnezia-dns-net`.

Критерии готовности:

- можешь объяснить, чем image отличается от container;
- можешь сказать, какие контейнеры относятся к Amnezia;
- понимаешь, почему VPN может работать, даже если Amnezia app не может управлять пользователями.

#### Урок 0.6. Рабочий Mobile CI/CD Pipeline

Цель: сделать рабочий pipeline понятной системой, а не набором Jenkins stages.

Что разбираем:

- stages;
- agents / clean builders;
- workspace;
- Nexus/SberOSC;
- Vault;
- MAST;
- artifacts;
- failure modes.

Практическое задание:

- нарисовать as-is pipeline;
- выписать внешние зависимости;
- выписать типы secrets без значений;
- зафиксировать 5 типовых failure modes.

Критерии готовности:

- можешь объяснить, что нужно чистому iOS/Android сборщику;
- можешь объяснить, где в pipeline появляются secrets;
- можешь отделить проблему кода от проблемы инфраструктуры.

#### Урок 0.7. Telegram-Бот Как Учебный Сервис

Цель: выбрать, как бот станет pet-service для DevOps-практики.

Что разбираем:

- как бот сейчас запускается;
- где его код;
- где logs;
- какие secrets нужны;
- desired state: Docker, CI, deploy, monitoring, security scan.

Практическое задание:

- найти текущую схему запуска бота;
- описать, что нужно для безопасного deploy;
- составить backlog улучшений.

Критерии готовности:

- есть список шагов, как превратить бот в production-like сервис;
- понятно, какие secrets нельзя коммитить;
- понятно, какие метрики и alerts нужны.

#### Урок 0.8. Проверка Фазы 0

Цель: проверить понимание и закрыть инвентаризацию.

Формат проверки:

- 10-минутное объяснение VPS своими словами;
- 10-минутное объяснение рабочего pipeline своими словами;
- ответы на контрольные вопросы;
- ревизия backlog P0/P1/P2;
- запись итогов в `learning-log`.

Фаза 0 закрыта, если:

- есть обновлённая карта VPS;
- есть as-is схема mobile pipeline;
- есть список внешних зависимостей рабочего pipeline;
- есть список secrets по типам без значений;
- есть desired state для Telegram-бота;
- ты уверенно читаешь базовые команды диагностики.

### Практика На VPS

- Обновить `01-vps-infrastructure/README.md` фактическим состоянием после последних изменений.
- Описать временный SSH `Match Address` для Amnezia и план его удаления.
- Описать log retention: journald 7 дней, `btmp` backup 7 дней, daily `vps-log-retention.timer`.
- Проверить weekly email report после новой русской версии.
- Сформировать короткий runbook "Как смотреть логи и диагностику Amnezia".

### Практика На Работе

- Нарисовать as-is схему mobile pipeline.
- Разделить pipeline на зоны: checkout, dependencies, build Android, build iOS, tests, MAST, publish artifacts.
- Зафиксировать все внешние системы: Jenkins, Vault, Nexus/SberOSC, build cluster, artifact storage, security tools.
- Выписать список secrets и где они должны храниться. Без значений, только типы и владельцы.

### Практика На Боте

- Найти текущее состояние бота: как запускается, где лежит код, как деплоится, где logs.
- Описать desired state: Dockerized bot, healthcheck, CI/CD, observability.

### Артефакты

- `learning-roadmap.md`;
- обновлённый runbook по VPS;
- sanitized схема рабочего pipeline;
- backlog из 10 улучшений.

### Критерии Готовности

- Ты можешь за 10 минут объяснить, как работает текущий VPS.
- Ты можешь за 10 минут объяснить, как устроен рабочий mobile pipeline.
- Есть список следующих задач с приоритетами P0/P1/P2.

### Рыночная Ценность

- Linux basics;
- production diagnostics;
- CI/CD discovery;
- documentation culture;
- security-aware documentation.

## Фаза 1. Linux, Networking, Bash

Срок: 1 месяц.

Цель: уверенно работать с Linux и сетью на уровне, достаточном для эксплуатации собственного сервера и понимания CI agents.

### Темы

- Linux filesystem: `/etc`, `/var`, `/opt`, `/usr`, `/home`, `/tmp`.
- Users/groups: `root`, service users, sudoers, file ownership.
- Permissions: `chmod`, `chown`, sticky bit, executable scripts.
- systemd: unit, service, timer, enable/start/reload/restart/status.
- Logs: `journalctl`, `/var/log`, retention, rotation.
- Processes: `ps`, `top`, `htop`, `systemctl`, `kill`.
- Networking: TCP/UDP, ports, sockets, DNS, HTTP, TLS.
- Firewall basics: UFW, iptables/nftables concepts, without blind edits.
- Bash: `set -euo pipefail`, functions, arguments, exit codes, traps.
- Safe automation: dry-run, backups, idempotency, rollback.

### Практика На VPS

- Сделать final cleanup временного SSH-доступа для Amnezia после проверки приложения.
- Описать `systemd` timers: weekly report, `clear-btmp`, `vps-log-retention`.
- Добавить runbook "Как безопасно менять SSH config".
- Проверить listening ports и зафиксировать, что действительно должно быть открыто.
- Написать bash-скрипт read-only healthcheck:
  - uptime;
  - disk;
  - memory;
  - failed units;
  - Docker containers;
  - Amnezia ports;
  - log size.

### Практика На Работе

- Разобрать, под какими пользователями работают Jenkins agents.
- Понять, где workspace, где caches, где временные директории.
- Разобрать сетевые зависимости сборки:
  - Nexus/SberOSC;
  - Apple/Android tooling;
  - Vault;
  - artifact storage;
  - MAST service.
- Сделать checklist "что должно быть доступно чистому сборщику".

### Практика На Боте

- Сделать systemd unit или Docker Compose описание запуска.
- Добавить простой `/health` или command healthcheck.
- Настроить logs так, чтобы их можно было читать без PM2-env/secrets.

### Домашний Мини-Проект

Название: `04-bash-toolkit`.

Состав:

- `bin/vps-healthcheck`;
- `bin/docker-healthcheck`;
- `bin/log-summary`;
- `lib/common.sh`;
- `tests/` на bats позже;
- README с примерами вывода.

Цель:

- научиться писать безопасные shell scripts;
- получить reusable инструменты для своего VPS;
- подготовиться к CI automation.

### Критерии Готовности

- Скрипты проходят ShellCheck.
- Каждый скрипт имеет `--help`.
- Скрипты не печатают secrets.
- Есть README с примерами.
- Ты можешь объяснить разницу между `restart` и `reload`.
- Ты можешь объяснить, почему нельзя вслепую менять firewall/routing на production VPS.

### Рыночная Ценность

- Linux operations;
- Bash automation;
- troubleshooting;
- production safety;
- infrastructure documentation.

## Фаза 2. Jenkins И Mobile CI/CD

Срок: 1-1.5 месяца.

Цель: стать человеком, который понимает mobile pipeline не только как пользователь, а как platform engineer.

### Темы

- Jenkins declarative pipeline.
- Scripted blocks и Groovy basics.
- Agents/nodes/labels.
- Workspace lifecycle.
- Credentials binding.
- Artifacts and archives.
- Shared libraries.
- Pipeline parameters.
- Timeout/retry/stash/unstash.
- Parallel stages.
- Clean builders.
- Build reproducibility.

### Mobile-Specific Темы

- React Native CLI build flow.
- Node/Yarn/npm dependency resolution.
- Gradle dependency resolution and cache.
- CocoaPods dependency resolution and cache.
- Xcode DerivedData.
- Android SDK/NDK/JDK versions.
- iOS certificates/profiles/keychain.
- Fastlane role in mobile delivery.
- Artifact naming and traceability.

### Практика На Работе

- Довести iOS и Android stages на чистых сборщиках.
- Сделать dependency source map:
  - npm packages;
  - Maven/Gradle;
  - CocoaPods;
  - binary artifacts;
  - internal packages;
  - blocked external sources.
- Добавить понятные preflight checks:
  - есть доступ к Nexus/SberOSC;
  - доступен Vault;
  - доступны нужные SDK;
  - credentials не пустые;
  - workspace clean.
- Документировать failure modes:
  - dependency failed;
  - signing failed;
  - MAST failed;
  - publish failed;
  - infrastructure unavailable.

### Практика На VPS/Боте

- Сделать простой Jenkins-like pipeline в GitHub Actions или локально:
  - lint;
  - test;
  - build Docker image;
  - scan image;
  - deploy to VPS.
- Для бота добавить версионирование артефакта: git SHA, build date, image tag.

### Домашний Мини-Проект

Название: `03-docker-rn-builder`.

Состав:

- Dockerfile для Android React Native build environment;
- pinned versions: Node, JDK, Android SDK, Gradle;
- README "какие версии и почему";
- локальная команда build demo app;
- описание кешей.

Цель:

- понять, что значит reproducible build;
- связать домашний проект с рабочей задачей clean builders;
- получить portfolio artifact для Mobile DevOps.

### Критерии Готовности

- Есть схема рабочего pipeline.
- Есть baseline метрики build duration.
- Есть список самых частых причин падений.
- Clean builder stage работает или понятен блокер.
- Есть обезличенный public pattern в `10-mobile-cicd-patterns`.

### Рыночная Ценность

- Jenkins;
- mobile CI/CD;
- build reproducibility;
- enterprise dependency management;
- platform engineering.

## Фаза 3. Secrets, Nexus И Supply Chain

Срок: 1 месяц.

Цель: понять security boundary pipeline: откуда приходят зависимости, где живут secrets, кто чему доверяет.

### Темы

- Vault basics: auth methods, policies, KV secrets, audit, rotation.
- Jenkins credentials vs Vault.
- Least privilege.
- Secret masking limitations.
- Nexus/SberOSC как dependency boundary.
- Dependency confusion.
- Package pinning.
- Checksums and lockfiles.
- SBOM: CycloneDX/SPDX basics.
- SCA: dependency vulnerability scanning.
- MAST: mobile security testing and remediation workflow.

### Практика На Работе

- Описать secrets flow для mobile pipeline.
- Разделить secrets по типам:
  - signing;
  - repository auth;
  - deploy/publish;
  - security scanners;
  - service tokens.
- Уточнить владельцев secrets и rotation process.
- Для MAST:
  - классифицировать типовые findings;
  - описать remediation workflow;
  - выделить false positives и exception process.
- Проверить, что pipeline не печатает secrets в logs.

### Практика На Боте

- Убрать все secrets из репозитория.
- Добавить `.env.example`.
- Добавить gitleaks в CI.
- Добавить Trivy scan Docker image.
- Добавить dependency scan, если стек позволяет.

### Домашний Мини-Проект

Название: `secure-bot-delivery`.

Состав:

- Dockerized Telegram bot;
- `.env.example`;
- gitleaks config;
- Trivy scan;
- GitHub Actions pipeline;
- deploy с внешними secrets;
- README с threat model.

Цель:

- закрепить DevSecOps практики на маленьком сервисе;
- сделать понятный публичный проект без раскрытия внутренностей Сбера.

### Критерии Готовности

- Secrets не лежат в git.
- CI падает при найденном secret.
- Docker image сканируется.
- Есть threat model на 1 страницу.
- Есть объяснение, чем MAST отличается от SAST/SCA/DAST.

### Рыночная Ценность

- DevSecOps basics;
- Vault;
- secure CI/CD;
- supply chain security;
- mobile security gates.

## Фаза 4. Docker И Runtime Operations

Срок: 1 месяц.

Цель: перестать воспринимать Docker как "команду запуска контейнера" и начать понимать runtime, image lifecycle, networks, volumes, logs, resource limits.

### Темы

- Image layers.
- Dockerfile best practices.
- Multi-stage builds.
- Build args vs env.
- Volumes.
- Networks.
- Port mapping.
- Healthchecks.
- Logs.
- Restart policies.
- Resource limits.
- Container security basics.

### Практика На VPS

- Разобрать Amnezia контейнеры read-only:
  - images;
  - networks;
  - ports;
  - restart policies;
  - logs;
  - resource usage.
- Не менять Amnezia без отдельного maintenance window.
- Настроить Docker health summary в weekly report.

### Практика На Боте

- Перевести бота в Docker, если ещё не переведён.
- Добавить healthcheck.
- Добавить restart policy.
- Добавить structured logs.
- Добавить rollback на предыдущий image tag.

### Домашний Мини-Проект

Название: `bot-container-platform`.

Состав:

- Dockerfile;
- compose file;
- healthcheck;
- deploy script;
- rollback script;
- log command;
- README "как обслуживать".

Цель:

- получить маленькую platform для одного сервиса;
- подготовиться к Kubernetes без преждевременного Kubernetes.

### Критерии Готовности

- Бот запускается одной командой.
- Есть healthcheck.
- Есть rollback.
- Logs читаются без secrets.
- Есть описание Docker network/volume/ports.

### Рыночная Ценность

- Docker;
- container operations;
- service lifecycle;
- deployment automation.

## Фаза 5. Observability

Срок: 1-1.5 месяца.

Цель: перейти от "работает/не работает" к измеримым метрикам и понятным alerts.

### Темы

- Metrics, logs, traces.
- Prometheus architecture.
- Exporters.
- PromQL basics.
- Grafana dashboards.
- Alertmanager basics.
- SLI/SLO.
- Alert fatigue.
- Incident response basics.

### Практика На VPS

- Проект `02-monitoring-stack`.
- Node Exporter для хоста.
- cAdvisor или Docker metrics для контейнеров.
- Dashboard:
  - CPU;
  - memory;
  - disk;
  - swap;
  - network;
  - failed units;
  - Docker containers;
  - log size.
- Alerts:
  - disk > 80%;
  - service failed;
  - container down;
  - high swap;
  - weekly report failed.

### Практика На Работе

- Pipeline observability:
  - build duration p50/p95;
  - queue time;
  - stage duration;
  - success rate;
  - failure reason distribution;
  - MAST failure rate;
  - publish failure rate.
- Если Grafana/Prometheus недоступны, начать с Jenkins data export и таблицы.

### Практика На Боте

- Добавить `/metrics`, если стек позволяет.
- Метрики:
  - process uptime;
  - request count;
  - errors;
  - Telegram API failures.
- Alert, если бот недоступен.

### Домашний Мини-Проект

Название: `02-monitoring-stack`.

Состав:

- Prometheus;
- Grafana;
- Node Exporter;
- Docker metrics;
- alert rules;
- dashboard JSON;
- README with screenshots.

### Критерии Готовности

- Есть dashboard VPS.
- Есть минимум 3 actionable alerts.
- Есть runbook "что делать, если alert сработал".
- Есть before/after метрики по хотя бы одной оптимизации.

### Рыночная Ценность

- Observability;
- Prometheus/Grafana;
- incident response;
- SRE basics.

## Фаза 6. Configuration Management: Ansible

Срок: 1 месяц.

Цель: сделать VPS воспроизводимым и уменьшить ручные изменения.

### Темы

- Inventory.
- Playbooks.
- Roles.
- Variables.
- Templates.
- Handlers.
- Idempotency.
- Check mode.
- Vault for Ansible secrets.
- Tags.
- Rollback limitations.

### Практика На VPS

- Проект `07-ansible-playbooks`.
- Роли:
  - base users and packages;
  - ssh hardening;
  - Docker;
  - log retention;
  - weekly report;
  - bot deployment;
  - monitoring agent.
- Начать с read-only facts и dry-run.
- Потом переносить только уже понятные настройки.

### Практика На Работе

- Применить мышление idempotency к Jenkins agents:
  - что должно быть установлено;
  - какие версии;
  - как проверять drift;
  - как документировать bootstrap чистого сборщика.

### Домашний Мини-Проект

Название: `07-ansible-playbooks`.

Состав:

- inventory example;
- roles;
- templates;
- dry-run instructions;
- README "что будет изменено";
- no real secrets.

### Критерии Готовности

- Playbook можно запустить повторно без лишних изменений.
- Есть `--check` сценарий.
- SSH hardening и log retention описаны кодом.
- Бот разворачивается через Ansible.

### Рыночная Ценность

- Ansible;
- configuration management;
- reproducible infrastructure;
- operations maturity.

## Фаза 7. Infrastructure As Code И Cloud

Срок: 1.5 месяца.

Цель: понять cloud primitives и описывать инфраструктуру кодом.

### Темы

- Cloud IAM.
- VPC, subnets, routes, NAT, security groups.
- Compute instances.
- Load balancers.
- Object storage.
- Managed databases basics.
- Terraform providers/resources/data sources.
- State and remote state.
- Modules.
- Variables and outputs.
- Secret boundaries in Terraform.

### Практика

- Проект `05-yandex-cloud-setup`: руками поднять минимальный аналог VPS.
- Проект `06-terraform-yc`: описать этот setup Terraform.
- Не переносить production VPN сразу.
- Начать с bot service или статического demo.

### Практика На Работе

- Понять, какие cloud/platform primitives скрыты за корпоративным build cluster:
  - agents;
  - storage;
  - credentials;
  - network access;
  - isolation.
- Сформулировать вопросы DevOps-команде на дейли.

### Домашний Мини-Проект

Название: `06-terraform-yc`.

Состав:

- network;
- compute instance;
- security group;
- object storage for state or artifacts;
- outputs;
- `.tfvars.example`;
- README with cost notes.

### Критерии Готовности

- Инфраструктура создаётся через Terraform.
- State не коммитится.
- Есть destroy path.
- Есть cost awareness.
- Есть diagram.

### Рыночная Ценность

- Terraform;
- Yandex Cloud/AWS fundamentals;
- IaC;
- cloud networking.

## Фаза 8. Kubernetes Без Спешки

Срок: 1.5-2 месяца.

Цель: понять Kubernetes как runtime для сервисов, а не как набор команд.

### Темы

- Pod.
- Deployment.
- ReplicaSet.
- Service.
- Ingress.
- ConfigMap.
- Secret.
- Volumes.
- Requests/limits.
- Liveness/readiness probes.
- Rolling updates.
- Helm basics.
- GitOps basics.

### Практика

- Проект `09-k8s-self-hosted`.
- Сначала локально: kind или k3d.
- Потом Yandex Cloud или self-hosted cluster.
- Деплой Telegram-бота:
  - Deployment;
  - Secret;
  - ConfigMap;
  - Service;
  - health probes;
  - resource limits;
  - Helm chart.
- Потом GitOps через ArgoCD.

### Практика На Работе

- Не пытаться "внедрить Kubernetes" в mobile pipeline.
- Использовать знания для понимания build cluster:
  - почему agents ephemeral;
  - как работают clean environments;
  - как мыслить resource requests;
  - почему важно не хранить state в workspace.

### Критерии Готовности

- Ты можешь объяснить, как запрос попадает в pod.
- Бот задеплоен в Kubernetes.
- Есть probes и resource limits.
- Есть rollback.
- Есть dashboard/alerts.

### Рыночная Ценность

- Kubernetes basics;
- Helm;
- GitOps;
- cloud-native runtime.

## Фаза 9. DevSecOps Углубление

Срок: параллельно после Фазы 3, отдельный фокус 1 месяц.

Цель: сделать security не отдельной темой, а частью delivery pipeline.

### Темы

- OWASP Mobile Top 10.
- OWASP CI/CD Security risks.
- SLSA basics.
- SBOM.
- Signing artifacts.
- Provenance.
- Policy as code basics.
- Container hardening.
- Kubernetes security basics.
- Secret rotation.
- Threat modeling with STRIDE.

### Практика На Работе

- Обезличить опыт MAST remediation в `10-mobile-cicd-patterns`.
- Описать security gate lifecycle:
  - scan;
  - triage;
  - severity;
  - owner;
  - fix;
  - exception;
  - expiration.
- Предложить улучшения отчётности по MAST.

### Практика На Боте

- SBOM generation.
- Dependency scan.
- Container scan.
- Secret scan.
- Minimal Docker image.
- Read-only filesystem, если применимо.

### Критерии Готовности

- Есть security checklist для mobile CI/CD.
- Есть threat model для bot pipeline.
- Есть автоматические security checks в CI.
- Есть понимание, где security gate помогает, а где создаёт шум.

### Рыночная Ценность

- DevSecOps;
- mobile security;
- supply chain;
- secure CI/CD.

## Фаза 10. Интервью И Позиционирование

Срок: последние 1-2 месяца, но материалы собирать с первого дня.

Цель: подготовить доказательную базу для перехода в DevOps/Mobile Platform роль.

### Темы

- Linux interview basics.
- Networking interview basics.
- CI/CD design.
- Docker troubleshooting.
- Kubernetes basics.
- Terraform state.
- Observability scenarios.
- Security tradeoffs.
- Incident stories.

### Артефакты

- `interview-prep/system-design`;
- `interview-prep/star-stories`;
- public portfolio README;
- sanitized diagrams;
- resume bullets with metrics.

### STAR Stories

- Clean builders for React Native.
- Vault/Nexus/SberOSC integration.
- MAST remediation.
- VPS SSH hardening without losing access.
- Log retention and weekly report.
- Dockerized Telegram bot delivery.
- Monitoring and alerting rollout.

### Критерии Готовности

- Есть 8-10 STAR stories.
- Есть 3 system design walkthroughs.
- Есть резюме под Mobile DevOps / Platform Engineer.
- Есть список компаний и вакансий.

## Еженедельный Ритм

Минимальная стабильная схема:

- 2 вечера: рабочий Jenkins/mobile CI/CD контур.
- 1 вечер: VPS или Telegram-бот.
- 1 вечер: теория текущей фазы.
- 30 минут в день: английский.
- 1 раз в неделю: `learning-log/YYYY-week-NN.md`.

Формат weekly log:

```md
## Что изучал

## Что сделал руками

## Что применил на работе

## Что сломалось или было непонятно

## Что стало понятнее

## Артефакт недели

## План на следующую неделю
```

## Backlog Практических Задач

### P0

- Убрать временный SSH `Match Address`, когда Amnezia management окончательно заработает через безопасный способ.
- Обновить `01-vps-infrastructure/README.md` после последних изменений log retention и weekly report.
- Зафиксировать рабочий pipeline as-is в обезличенной схеме.
- Составить dependency source map для mobile проекта.

### P1

- Добавить monitoring stack на VPS.
- Dockerize Telegram-бота.
- Добавить CI для Telegram-бота.
- Добавить gitleaks и Trivy в bot CI.
- Сделать Docker RN Android builder.

### P2

- Ansible roles для VPS.
- Terraform YC demo.
- Kubernetes deploy для бота.
- GitOps через ArgoCD.
- Public write-up: "Mobile CI/CD clean builders: lessons learned".

## Как Понимать, Что Ты Растёшь

Плохой сигнал:

- читаешь много, но не меняешь ни VPS, ни bot pipeline, ни рабочий pipeline;
- учишь Kubernetes, но не можешь объяснить `systemctl status`;
- знаешь названия инструментов, но не можешь описать failure modes;
- нет метрик before/after.

Хороший сигнал:

- каждую неделю есть маленький артефакт;
- рабочая задача становится понятнее и измеримее;
- VPS становится менее ручным;
- бот получает настоящий CI/CD lifecycle;
- появляются sanitized материалы для портфолио;
- ты можешь объяснять tradeoffs: безопасность vs доступность, скорость сборки vs reproducibility, cache vs correctness.

## Рыночная Формула

К концу года целевое позиционирование должно звучать так:

> Senior React Native engineer moving into Mobile DevOps / Platform Engineering, with hands-on experience in Jenkins-based mobile CI/CD, clean iOS/Android builders, Vault-backed secrets, corporate dependency management, MAST remediation, Linux operations, Docker, monitoring, IaC basics and secure delivery practices.

Для РФ это хорошо ложится в:

- DevOps Engineer;
- Mobile DevOps Engineer;
- Platform Engineer;
- CI/CD Engineer;
- Build/Release Engineer;
- DevSecOps Engineer junior/middle track.

Для международного рынка это лучше подавать как:

- Mobile Platform Engineer;
- CI/CD Engineer;
- Build and Release Engineer;
- DevOps Engineer with mobile specialization.
