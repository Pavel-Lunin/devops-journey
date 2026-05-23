# Project 06: Terraform for Yandex Cloud

> **Status:** 📋 Planned
> **Phase:** 2 (Месяцы 4–6)
> **Timeline:** Месяцы 5–6

## Goal

Переписать manual setup из проекта 05 на Terraform с best practices: модули, remote state в YC Object Storage с locking через Lockbox, поддержка multi-environment (dev / staging / prod), переменные через `.tfvars`, secrets через Lockbox.

## Why this matters

Terraform — фактический стандарт IaC, упоминается в 80%+ DevOps вакансий. Просто "умею писать `.tf` файлы" недостаточно — рекрутёры спрашивают про модули, state management, drift, плановые vs импортируемые ресурсы. Modular structure и работающий remote state с locking показывают production mindset, а не learning-toy уровень.

## Tech stack

- Terraform (последняя стабильная версия)
- HCL (Terraform syntax)
- terraform-yandex-modules / собственные модули
- Yandex Cloud provider
- YC Object Storage (S3-compatible) для remote state
- YC Lockbox для secrets
- `tflint` + `tfsec` для линтинга и безопасности
- pre-commit hooks

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

Структура: `modules/` (network, compute, lb, storage), `environments/{dev,prod}/` с собственными `backend.tf` и `terraform.tfvars`, общий `versions.tf` для provider pinning. State хранится в Object Storage отдельно для каждого окружения.

## How to reproduce

[Будет наполнено: `terraform init / plan / apply` для каждого окружения, инициализация state-бакета bootstrap-скриптом.]

## Metrics & Results

[Будет наполнено: время `apply` с нуля, размер state-файла, количество ресурсов, drift-проверки.]

## What I learned

[Будет наполнено: state-management traps, разница `count` vs `for_each`, граната `terraform destroy`, как НЕ хранить secrets в .tfvars.]

## References

- [Terraform documentation](https://developer.hashicorp.com/terraform/docs)
- [Yandex Cloud Terraform provider](https://yandex.cloud/docs/tutorials/infrastructure-management/terraform-quickstart)
- [Terraform best practices](https://www.terraform-best-practices.com/)
- [tflint](https://github.com/terraform-linters/tflint), [tfsec](https://github.com/aquasecurity/tfsec)
