# P0/P1 Remediation Plan — VPS Infrastructure

Дата: 2026-06-17  
Baseline: `../audits/vps-audit-20260615T051516Z/`

## Safety boundary

Не делать без отдельного maintenance window:

- reboot;
- `systemctl restart docker`;
- `systemctl restart networking`;
- `docker compose down/up`;
- `ufw reload`, `ufw enable`, `ufw reset`;
- изменение routing, iptables/nftables, Docker networks, `amn0`, `docker0`;
- `apt upgrade`, `full-upgrade`, `dist-upgrade`, `autoremove`;
- Docker/containerd/runc upgrade.

## Current findings

### P0

- `pm2-devops.service` failed с 2026-01-31.
- `fate-bot-production`, `fate-bot-staging`, `pm2-logrotate` в PM2 имеют `stopped`.
- Если бот не должен работать, автозапуск PM2 нужно отключить и убрать failed-state.

### P1

- Swap отсутствует: `Swap: 0B`.
- `/var/log` занимает 2.4G, journald — 1.8G, `/var/log/btmp` — 541M.
- Apache слушает `*:8080`, `*:8081`, `*:8082`; менять bind только в отдельное окно.
- UFW разрешает `22/tcp` from Anywhere; менять firewall только в отдельное окно.
- 26 APT packages upgradable, включая `containerd`, `runc`, `apparmor`; runtime packages обновлять только в maintenance window.

## P0: PM2 autostart cleanup

Цель: если бот сейчас не нужен, убрать ложный failed service и автозапуск PM2. Это не трогает Docker, AmneziaWG, UFW и routing.

Read-only precheck:

```bash
systemctl cat pm2-devops --no-pager
sudo systemctl status pm2-devops --no-pager -l
bash -lc 'source ~/.nvm/nvm.sh 2>/dev/null || true; pm2 status || true'
```

Change commands:

```bash
sudo systemctl disable pm2-devops.service
sudo systemctl reset-failed pm2-devops.service
```

Optional cleanup if PM2 should not resurrect these apps:

```bash
bash -lc 'source ~/.nvm/nvm.sh 2>/dev/null || true; pm2 save'
```

Verification:

```bash
systemctl is-enabled pm2-devops.service || true
systemctl --failed --no-pager
bash -lc 'source ~/.nvm/nvm.sh 2>/dev/null || true; pm2 status || true'
```

Rollback:

```bash
sudo systemctl enable pm2-devops.service
```

## P1: Add swapfile

Цель: снизить риск OOM на VPS с 1.9 GiB RAM и userspace AmneziaWG. Не требует reboot и не трогает Docker/VPN.

Recommended size: 2 GiB.

Change commands:

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

Verification:

```bash
free -h
swapon --show
grep -n '/swapfile' /etc/fstab
```

Rollback:

```bash
sudo swapoff /swapfile
sudo sed -i.bak '/\/swapfile none swap sw 0 0/d' /etc/fstab
sudo rm /swapfile
```

## P1: journald retention

Цель: ограничить рост `/var/log/journal`, который сейчас занимает около 1.8G.

Suggested drop-in:

```ini
# /etc/systemd/journald.conf.d/10-retention.conf
[Journal]
SystemMaxUse=500M
SystemKeepFree=1G
MaxRetentionSec=30day
```

Change commands:

```bash
sudo mkdir -p /etc/systemd/journald.conf.d
printf '%s\n' '[Journal]' 'SystemMaxUse=500M' 'SystemKeepFree=1G' 'MaxRetentionSec=30day' | sudo tee /etc/systemd/journald.conf.d/10-retention.conf
sudo systemd-analyze cat-config systemd/journald.conf
sudo journalctl --vacuum-size=500M
```

Note: applying config to the running journald normally requires `systemctl restart systemd-journald`; postpone that to maintenance window if strict no-restart policy is active.

Verification:

```bash
journalctl --disk-usage
sudo du -h -d1 /var/log | sort -h
```

## P1: btmp rotation

Цель: остановить рост `/var/log/btmp`, который вырос до 541M из-за failed login noise.

Check current policy:

```bash
grep -Rni 'btmp' /etc/logrotate.conf /etc/logrotate.d 2>/dev/null || true
```

Suggested policy:

```text
/var/log/btmp {
    monthly
    rotate 1
    create 0660 root utmp
    minsize 1M
}
```

Не запускать forced rotation без отдельного решения: это меняет forensic history.

## Deferred to maintenance window

- Bind Apache to `127.0.0.1:8080/8081/8082`.
- Restrict SSH UFW rule from `Anywhere` to trusted IPs.
- Enable/configure fail2ban.
- Apply Docker/containerd/runc updates.
- Add TLS/certbot.

