# Project 07: Ansible Playbooks

> **Status:** 📋 Planned
> **Phase:** 2 (Месяцы 4–6)
> **Timeline:** Месяц 4

## Goal

Описать через Ansible roles развёртывание всего VPS-стека "с нуля": common-setup (пользователи, sshd, timezone, ufw), nginx, apache, monitoring agents (Node Exporter), TLS-сертификаты. Playbook должен быть идемпотентным и проходить `--check` без ложных diff'ов.

## Why this matters

Ansible активно используется в РФ DevOps — особенно в банках и tier-1 компаниях; в вакансиях Yandex, VK Tech, Tinkoff он упоминается часто. Idempotent playbooks показывают понимание core DevOps-philosophy: "describe desired state, not steps". В связке с проектом 06 (Terraform создаёт VM, Ansible её настраивает) это рабочий шаблон, который встречается на интервью почти всегда.

## Tech stack

- Ansible (последняя стабильная версия)
- Ansible Vault (для secrets)
- Jinja2 (templates)
- YAML
- Roles structure (по официальным best practices)
- `ansible-lint`
- Molecule (тестирование ролей)

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

Структура: `inventories/{dev,prod}/`, `roles/{common,nginx,apache,monitoring,tls}/`, `playbooks/site.yml` как entrypoint. Secrets — через Ansible Vault, ключ хранится локально (НЕ в репозитории), есть `.vault_pass` в `.gitignore`.

## How to reproduce

[Будет наполнено: `ansible-playbook -i inventories/prod playbooks/site.yml --check`, описание ролей, требования к managed node.]

## Metrics & Results

[Будет наполнено: время `apply` от чистой Ubuntu до полностью настроенного хоста, количество tasks, % покрытия Molecule-тестами.]

## What I learned

[Будет наполнено: handlers vs notify, когда нужны custom modules, ловушки `become`, как держать playbook идемпотентным.]

## References

- [Ansible documentation](https://docs.ansible.com/)
- [Ansible best practices (Roles)](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html)
- [Molecule](https://ansible.readthedocs.io/projects/molecule/)
- [ansible-lint](https://ansible.readthedocs.io/projects/lint/)
