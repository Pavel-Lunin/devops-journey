# P1 Swap And Journald Result

Дата: 2026-06-18  
Scope: P1 remediation для swap и journald retention

## Почему

Audit `../audits/vps-audit-20260615T051516Z/` показал:

- swap отсутствовал: `Swap: 0B`;
- `/var/log` занимал около 2.4G;
- persistent journald занимал около 1.7-1.8G;
- `/var/log/btmp` занимал около 519-541M.

## Pre-change snapshot

Перед изменениями создан и запушен snapshot в private repo `vps-state`:

```text
2a9affe docs: capture pre p1 remediation state
```

Каталог на сервере:

```text
/home/devops/vps-state/snapshots/2026-06-18-pre-p1/
```

## Что сделано

Создан swapfile 2G без reboot:

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

Добавлен journald retention config:

```ini
# /etc/systemd/journald.conf.d/10-retention.conf
[Journal]
SystemMaxUse=500M
SystemKeepFree=1G
MaxRetentionSec=30day
```

Выполнен manual vacuum:

```bash
sudo journalctl --vacuum-size=500M
```

Не выполнялось:

- reboot;
- restart `systemd-journald`;
- Docker / AmneziaWG / UFW / routing changes;
- Apache bind changes;
- APT upgrade;
- forced logrotate.

## Проверка после изменения

```text
Swap: 2.0Gi
/swapfile file 2G USED 0B
journald disk usage: 497.1M
/var/log: 1023M
/var/log/journal: 498M
systemctl --failed: only rc-local.service remains failed
```

## btmp status

`/var/log/btmp` всё ещё крупный:

```text
/var/log/btmp ~519M
```

Проверка показала, что `/etc/logrotate.conf` отсутствует, а `logrotate` binary не найден через `command -v logrotate`. Поэтому btmp rotation не менялась в этой итерации. Это нужно вынести в отдельный шаг: установить/вернуть logrotate policy или настроить ротацию штатным для образа способом.

## Post-change snapshot

После изменений создан и запушен snapshot в private repo `vps-state`:

```text
648d48a docs: capture post p1 swap journald state
```

Каталог на сервере:

```text
/home/devops/vps-state/snapshots/2026-06-18-post-p1-swap-journal/
```

## Rollback

Rollback swap:

```bash
sudo swapoff /swapfile
sudo sed -i.bak '/\/swapfile none swap sw 0 0/d' /etc/fstab
sudo rm /swapfile
```

Rollback journald retention config:

```bash
sudo rm /etc/systemd/journald.conf.d/10-retention.conf
```

Note: applying/removing journald config to the running daemon normally requires restarting `systemd-journald`; do that only in a maintenance window if strict no-restart policy is active.

