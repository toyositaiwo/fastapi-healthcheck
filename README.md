cat << 'EOF' > README.md
# FastAPI DevOps Health Monitor

A lightweight FastAPI application deployed on DigitalOcean showing server health, version, and metrics.

## Features
- Health check endpoint (/health)
- Version info endpoint (/version)
- Metrics endpoint (/metrics)
- Nginx reverse proxy
- systemd service
- GitHub webhook CI/CD

## Endpoints
| Endpoint | Description |
|----------|-------------|
| /        | Root endpoint |
| /health  | Heartbeat check |
| /version | App version info |
| /metrics | CPU / Memory / Disk stats |

## Deployment Steps (DigitalOcean)
1. Clone repo
2. Create Python venv
3. Install dependencies
4. Configure systemd service
5. Configure Nginx
6. Restart services
EOF

