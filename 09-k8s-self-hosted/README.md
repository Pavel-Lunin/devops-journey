# Project 09: Self-Hosted Kubernetes

> **Status:** 📋 Planned
> **Phase:** 3 (Месяцы 7–9)
> **Timeline:** Месяцы 7–9 — флагманский проект года

## Goal

Поднять production-grade self-hosted Kubernetes-кластер на Yandex Cloud VM'ках через kubespray (Ansible), с полным observability-стеком (kube-prometheus-stack + Loki), nginx-ingress + cert-manager для TLS, ArgoCD для GitOps-управления приложениями. VM'ки создаются через Terraform из проекта 06.

## Why this matters

**Флагманский проект года** — это всё, что я учил, собранное в одну работающую систему. Self-hosted Kubernetes — характерная специфика РФ-рынка (в отличие от EU/US, где доминируют managed-сервисы вроде EKS/GKE/AKS): многие крупные РФ-компании по compliance-соображениям держат K8s сами на своих VM или bare-metal. Один работающий проект 09 в портфолио закрывает требования по K8s, observability, GitOps, IaC и Ansible — то есть весь Middle DevOps stack одним экспонатом.

## Tech stack

- Kubernetes (последняя LTS-версия)
- kubespray (Ansible-based installer)
- Terraform (создание VM в YC, переиспользует модули из проекта 06)
- Helm
- nginx-ingress-controller
- cert-manager (Let's Encrypt)
- kube-prometheus-stack (Prometheus, Grafana, Alertmanager, kube-state-metrics)
- Loki + Promtail (логи)
- ArgoCD (GitOps)
- `kubectl`, `kustomize`

## Architecture

> Архитектурная диаграмма будет добавлена в `diagrams/architecture.png`

3 control plane node + 3 worker node на YC Compute. Внешний NLB перед ingress-controller'ом. ArgoCD синхронизирует манифесты из отдельного app-config репозитория. Observability-стек разворачивается через Helm, dashboard'ы Grafana — как ConfigMap'ы в git. Backup etcd на YC Object Storage.

## How to reproduce

[Будет наполнено: bootstrap-инструкция от пустой YC-папки до работающего кластера, разделена на phases: `terraform apply` → `ansible-playbook kubespray/cluster.yml` → `helm install` базового стека → `argocd app create` для пользовательских apps.]

## Metrics & Results

[Будет наполнено: время полного bootstrap, MTTR при killing-control-plane сценарии, ресурсы кластера, стоимость в YC.]

## What I learned

[Будет наполнено: nuances etcd-бэкапов, networking quirks (CNI), почему упало в первый раз, как ArgoCD меняет mental model деплоя.]

## References

- [Kubernetes documentation](https://kubernetes.io/docs/)
- [kubespray](https://github.com/kubernetes-sigs/kubespray)
- [Helm](https://helm.sh/docs/)
- [ArgoCD](https://argo-cd.readthedocs.io/)
- [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
- "Kubernetes the Hard Way" — Kelsey Hightower
