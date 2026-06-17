# Server State Artifacts

Санитизированные фрагменты текущего состояния VPS, которые можно держать в git как reference.

Это не полноценный IaC. Источник правды для автоматизации появится позже в Project 07 (Ansible). Здесь фиксируются только безопасные, несекретные конфиги и примеры.

## Files

- `sudoers-devops-codex.example` — ограниченный sudoers drop-in для диагностики и безопасных reload-команд.

## Related Git Repository On VPS

На самом сервере создан отдельный локальный git-репозиторий:

```text
/home/devops/vps-state
```

Назначение: хранить sanitized историю состояния VPS и rollback notes рядом с production-хостом. Это не замена provider snapshot и не место для secrets.

В публичный `devopsJourney` этот репозиторий не добавляется как submodule, чтобы не публиковать production SSH URL/IP и не связывать public portfolio с приватным server-state remote.
