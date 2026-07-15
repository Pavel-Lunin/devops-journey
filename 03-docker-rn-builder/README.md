# Project 03: Docker RN Builder

> **Status:** 🔄 In Progress
> **Phase:** 1 (Месяцы 1–3)
> **Timeline:** Docker fundamentals → clean Android builder

## Goal

Пройти путь от базовых Docker-упражнений до reproducible image для сборки React Native приложений под Android на чистом сборщике. Итоговый образ должен фиксировать версии JDK, Android SDK, Node.js и Gradle, поддерживать BuildKit cache и собирать demo-приложение без зависимости от локального Android toolchain.

## Why this matters

Проект соединяет текущую Mobile-экспертизу с DevOps-практикой. Контейнеризация Android build environment устраняет различия между локальными и CI-сборщиками, делает pipeline воспроизводимым и формирует portfolio artifact на стыке Mobile DevOps и Platform Engineering.

## Tech stack

**Текущие course labs:**

- Dockerfile: `FROM`, `WORKDIR`, `COPY`, `CMD`
- Docker bind mounts
- Docker Compose
- Service discovery между Python-приложением и MongoDB
- Базовые images: Python Alpine, Node.js Alpine, nginx, MongoDB

**Целевой RN Android builder:**

- Docker BuildKit и cache mounts
- JDK 17
- Android SDK cmdline-tools
- Node.js и React Native CLI
- Gradle с отдельным dependency cache

## Architecture

```text
course-labs/
├── python-app/          # build image и интерактивный CLI
├── node-app/            # запись в bind mount
├── nginx/               # раздача HTML из read-only bind mount
└── docker-compose-app/  # app → service DNS "mongo" → MongoDB
            │
            ▼
RN Android builder (следующая итерация)
base JDK → Android SDK → Node.js/Gradle cache → clean Android build
```

Учебные примеры изолированы в [`course-labs/`](./course-labs/), чтобы не смешивать упражнения курса с будущим production-grade builder image.

## How to reproduce

Требования: Docker Engine или Docker Desktop с Compose v2.

```bash
cd 03-docker-rn-builder/course-labs

# Python CLI
docker build -t course-python-cli ./python-app
docker run --rm -it course-python-cli

# Node.js и bind mount
docker build -t course-node-volume ./node-app
docker run --rm \
  --mount type=bind,src="$PWD/node-app",dst=/app \
  course-node-volume

# nginx и read-only bind mount
docker run --rm -p 8080:80 \
  --mount type=bind,src="$PWD/nginx",dst=/usr/share/nginx/html,readonly \
  nginx:alpine

# Python + MongoDB через Compose
docker compose -f docker-compose-app/docker-compose.yml up \
  --build --abort-on-container-exit
docker compose -f docker-compose-app/docker-compose.yml down
```

Команды сборки React Native Android demo будут добавлены вместе с первым вариантом builder image.

## Metrics & Results

| Метрика | Текущее значение |
|---|---:|
| Перенесено course labs | 4 |
| Dockerfile | 3 |
| Compose-конфигурации | 1 |
| Отработанные темы | image build, container command, bind mounts, service DNS |
| RN Android builder | следующая итерация |

Baseline для Android-сборки будет включать размер image, время cold build, время warm build и сравнение с локальной сборкой.

## What I learned

- Image — неизменяемый шаблон, а container — конкретный процесс с отдельным writable layer.
- `WORKDIR`, `COPY` и `CMD` задают filesystem и default process будущего container.
- Bind mount связывает lifecycle данных с хостом и подходит для локальной разработки, но снижает переносимость команды запуска.
- Compose создаёт общую сеть, поэтому приложение обращается к MongoDB по имени service `mongo`, а не по `localhost`.
- Текущие labs намеренно простые: base images и Python dependency пока не pinned, у MongoDB нет healthcheck, а containers запускаются от root. Эти ограничения станут чек-листом следующей итерации.

## References

- [Docker BuildKit](https://docs.docker.com/build/buildkit/)
- [Docker bind mounts](https://docs.docker.com/engine/storage/bind-mounts/)
- [Docker Compose networking](https://docs.docker.com/compose/how-tos/networking/)
- [Android cmdline-tools](https://developer.android.com/tools)
- [React Native — Building from source](https://reactnative.dev/contributing/how-to-build-from-source)
