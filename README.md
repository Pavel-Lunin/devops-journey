# Pavel Lunin

**Senior Mobile Engineer | Mobile DevOps & Platform Engineering**

12-месячный публичный journal моего перехода от Senior Mobile Engineer к Middle DevOps Engineer. Этот репозиторий одновременно — учебный дневник, playground для проектов и portfolio для рекрутёров.

---

## Table of Contents

- [Bio](#bio)
- [Goals](#goals)
- [Roadmap](#roadmap)
- [Projects](#projects)
- [Tech Stack](#tech-stack)
- [Currently Learning](#currently-learning)
- [Contact](#contact)

---

## Bio

Senior Mobile Engineer с 6 годами коммерческой разработки на React Native в РФ. Сейчас работаю в Сбере над крупным mobile-продуктом и веду внутреннюю инициативу по автоматизации mobile CI/CD pipeline — именно эта задача стала естественным мостом к DevOps. За плечами production-эксплуатация собственного VPS (nginx, apache, VPN, TLS), глубокое знакомство с Jenkins, Fastlane и native build-инструментами iOS/Android. Цель этого репозитория — за 12 месяцев пройти путь от self-taught DevOps practitioner до позиции Middle DevOps Engineer в одной из tier-1 РФ-компаний, документируя каждый шаг публично.

---

## Goals

Конкретные measurable цели на 12 месяцев (2026):

- 🎯 **Карьерная цель:** оффер Middle DevOps Engineer в РФ к концу 2026 года (Yandex, VK Tech, Tinkoff, Ozon, Сбер internal)
- 📜 **Сертификации:**
  - Yandex Cloud Associate
  - AWS Solutions Architect Associate (SAA-C03)
  - Certified Kubernetes Administrator (CKA)
- 🇬🇧 **Английский:** B2 reading + базовый conversational (для долгосрочной опции международного pivot через 2–3 года)
- 🚀 **Production impact:** довести до прода как минимум одно значимое улучшение mobile CI/CD pipeline на текущей работе

---

## Roadmap

| Фаза       | Месяцы | Фокус                                     | Ключевые результаты                                                                                       |
| ---------- | ------ | ----------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Фаза 1** | 1–3    | Discovery + первый production improvement | VPS документирован, Docker-builder для RN, мониторинг, первый production fix в Jenkins pipeline на работе |
| **Фаза 2** | 4–6    | Ansible + GitLab CI + AWS SAA             | VPS воспроизводится через Ansible, полный GitLab CI demo, сертификат AWS SAA                              |
| **Фаза 3** | 7–9    | Kubernetes + CKA                          | Self-hosted K8s кластер на YC, GitOps через ArgoCD, сертификат CKA                                        |
| **Фаза 4** | 10–12  | Job hunt                                  | Резюме, system design, STAR stories, активные интервью, оффер                                             |

---

## Projects

| #   | Project                                             | Status         | Phase      | Описание                                                                           |
| --- | --------------------------------------------------- | -------------- | ---------- | ---------------------------------------------------------------------------------- |
| 01  | [VPS Infrastructure](./01-vps-infrastructure/)      | 🔄 In Progress | 1          | Документация существующего self-hosted VPS (nginx + apache + Amnezia VPN)          |
| 02  | [Monitoring Stack](./02-monitoring-stack/)          | 📋 Planned     | 1          | Prometheus + Grafana + Node Exporter + Alertmanager для VPS                        |
| 03  | [Docker RN Builder](./03-docker-rn-builder/)        | 📋 Planned     | 1          | Reproducible Docker image для сборки React Native (Android)                        |
| 04  | [Bash Toolkit](./04-bash-toolkit/)                  | 🔄 In Progress | 1          | Production-ready bash-скрипты автоматизации, ShellCheck-clean                      |
| 05  | [Yandex Cloud Setup](./05-yandex-cloud-setup/)      | 📋 Planned     | 1          | Manual setup VPS-стека на Yandex Cloud (Compute, VPC, NLB, Object Storage)         |
| 06  | [Terraform YC](./06-terraform-yc/)                  | 📋 Planned     | 2          | Тот же setup через Terraform с модулями и remote state                             |
| 07  | [Ansible Playbooks](./07-ansible-playbooks/)        | 📋 Planned     | 2          | Idempotent roles для развёртывания всего VPS-стека "с нуля"                        |
| 08  | [GitLab CI/CD Demo](./08-gitlab-cicd-demo/)         | 📋 Planned     | 2          | Полный pipeline: build → test → security scan → deploy                             |
| 09  | [K8s Self-Hosted](./09-k8s-self-hosted/)            | 📋 Planned     | 3          | **Флагман:** self-hosted Kubernetes на YC через kubespray + ArgoCD + observability |
| 10  | [Mobile CI/CD Patterns](./10-mobile-cicd-patterns/) | 📋 Planned     | continuous | Обезличенные architectural patterns из enterprise mobile-опыта                     |

Легенда: 📋 Planned · 🔄 In Progress · ✅ Complete

---

## Tech Stack

**Languages**

- TypeScript (production, 6+ лет)
- Bash (intermediate, активно прокачиваю)
- Python (basic, для скриптов и automation)
- Groovy (Jenkins pipelines)

**Containers & Orchestration**

- Docker (intermediate)
- Kubernetes (learning)

**Infrastructure as Code**

- Terraform (learning)
- Ansible (learning)

**CI/CD**

- Jenkins (production)
- GitHub Actions (intermediate)
- GitLab CI (learning)

**Cloud**

- Yandex Cloud (learning)
- AWS (learning, target — SAA сертификат)

**Observability**

- Prometheus, Grafana (learning, hands-on в проекте 02)
- Sentry, Dynatrace (production-опыт с mobile)

**Mobile (текущая экспертиза)**

- React Native, Fastlane
- Native iOS / Android build-системы (Xcode, Gradle)
- Jenkins-based mobile pipelines на enterprise scale

---

## Currently Learning

🔄 **Active focus (Фаза 1, месяцы 1–3):**

- Документирование production VPS-стека (проект 01) — превращаю tribal knowledge в воспроизводимую документацию
- Bash toolkit (проект 04) — ежедневная практика, ShellCheck в редакторе
- Docker для mobile builds (проект 03) — параллельно с рабочей задачей по автоматизации pipeline в Сбере
- Prometheus + Grafana основы — подготовка к проекту 02

📚 **Reading:**

- "The Linux Command Line" — William Shotts
- Prometheus docs + "Prometheus: Up & Running"

---

## Contact

- 📧 Email: [pavelunin@icloud.com](mailto:pavelunin@icloud.com)
- 💼 LinkedIn: [pavel-lunin-832796210](https://www.linkedin.com/in/pavel-lunin-832796210)
- 📱 Telegram: [@Lunin_Pavel](https://t.me/Lunin_Pavel)
- 🌐 GitHub: [Pavel-Lunin](https://github.com/Pavel-Lunin)

---

_Этот README обновляется по мере прогресса. Последнее обновление: см. git log._
