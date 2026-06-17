# VPS Audit Summary

Audit time: 2026-06-15 05:15 UTC
Host: vm3849819.firstbyte.club
OS: Ubuntu 24.04.3 LTS, kernel 6.8.0-57-generic
Uptime: 137 days 14 hours
Report directory: /home/devops/vps-audit-20260615T051516Z

## A) Критично

- Temporary sudo NOPASSWD is currently enabled for `devops` for this audit. It gives root-equivalent access without password and should be removed after review. I did not remove it because this audit was explicitly read-only except report creation.
- `pm2-devops.service` is failed for 4+ months, and PM2 shows `fate-bot-production`, `fate-bot-staging`, and `pm2-logrotate` as `stopped`. If the Telegram bot is expected to be online, this is a production availability issue.

## B) Важно, но можно позже

- Swap is absent: `Swap: 0B`. With 1.9 GiB RAM and userspace AmneziaWG, add a small swap file in a planned safe change.
- `/var/log` uses 2.4G; persistent journald uses 1.8G; `/var/log/btmp` is 541M. This confirms sustained failed login noise and missing/insufficient journal retention limits.
- 26 APT packages are upgradable. Notable packages: `containerd` 1.7 -> 2.2, `runc`, `apparmor`, `libapparmor1`. No upgrade was run.
- Apache listens on `*:8080`, `*:8081`, `*:8082`. UFW default incoming policy is deny, but architecturally these backends should bind to `127.0.0.1` when changed safely.
- UFW allows `22/tcp` from Anywhere even though there is also a narrower rule for `46.242.14.134`. SSH password/root login is already disabled, but firewall scope can be tightened later.

## C) Безопасно исправить сейчас

- Remove the temporary sudoers drop-in when you finish reviewing the report:
  `sudo rm /etc/sudoers.d/devops-codex && sudo -k`
- Keep SSH hardening as-is. Effective config is good: `PasswordAuthentication no`, `KbdInteractiveAuthentication no`, `PermitRootLogin no`, `PubkeyAuthentication yes`.
- Add this audit directory path to the project notes/README if you want traceability for Project 01.

## D) Нельзя трогать без maintenance window

- Do not upgrade Docker/containerd/runc on the live VPN host without a rollback plan and maintenance window.
- Do not change Apache listen addresses, nginx upstreams, UFW, iptables/nftables, routing, Docker networks, or AmneziaWG containers without a maintenance window.
- Do not restart Docker, networking, AmneziaWG containers, or the whole server during routine audit work.

## Service snapshot

- `ssh`, `nginx`, `apache2`, and `docker` are active.
- Failed units: `pm2-devops.service`, `rc-local.service`.
- nginx config test: OK.
- Apache config test: OK.
- Local HTTP checks: nginx `127.0.0.1:80` and Apache `127.0.0.1:8080/8081/8082` returned `200 OK`.
- Docker containers are running: `amnezia-awg`, `amnezia-awg2`, `amnezia-dns`.
- Amnezia DNS container is healthy.

## What was not touched

- Docker: not changed, only `docker ps`, `docker stats`, `docker network ls/inspect` were run.
- AmneziaWG: not changed, containers were not restarted/stopped/started.
- UFW: not changed, only `ufw status verbose` was read.
- Routing: not changed, only `ip route` was read.
- iptables: not changed, only `iptables -S` and `iptables -t nat -S` were read.
- No server reboot, no service restart, no Docker compose action, no apt upgrade/autoremove/full-upgrade.

## Report files

- `01-basic-system.txt`
- `02-resources.txt`
- `03-systemd.txt`
- `04-network-firewall.txt`
- `05-docker-amnezia-readonly.txt`
- `06-nginx-apache.txt`
- `07-ssh-effective-config.txt`
- `08-apt.txt` and `apt-upgradable.txt`
- `09-logs-space.txt`
- `10-pm2.txt`
