# PM2 Autostart Cleanup Result

Дата: 2026-06-17  
Scope: P0 cleanup для `pm2-devops.service`

## Почему

Audit `../audits/vps-audit-20260615T051516Z/` показал:

- `pm2-devops.service` был `enabled` и `failed` с 2026-01-31;
- PM2 apps `fate-bot-production`, `fate-bot-staging` и module `pm2-logrotate` были `stopped`;
- автозапуск создавал ложный failed-state, но фактически не поднимал рабочий сервис.

## Что сделано

Выполнено только:

```bash
sudo systemctl disable pm2-devops.service
sudo systemctl reset-failed pm2-devops.service
```

Не выполнялось:

- `systemctl restart`;
- `systemctl stop`;
- `pm2 start`;
- `pm2 delete`;
- `pm2 save`;
- reboot;
- Docker / AmneziaWG / UFW / routing changes.

## Проверка после изменения

```text
systemctl is-enabled pm2-devops.service -> disabled
systemctl is-active pm2-devops.service  -> inactive
systemctl status pm2-devops             -> inactive (dead)
systemctl --failed                      -> only rc-local.service remains failed
```

PM2 runtime не менялся:

```text
fate-bot-production -> stopped
fate-bot-staging    -> stopped
pm2-logrotate       -> stopped
```

## Rollback

Если PM2 autostart снова понадобится:

```bash
sudo systemctl enable pm2-devops.service
```

Запуск самих PM2 apps делать отдельным runbook'ом после проверки `.env`, app paths и ожидаемого production/staging состояния.

