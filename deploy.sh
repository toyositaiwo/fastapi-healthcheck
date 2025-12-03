cat << 'EOF' > deploy.sh
#!/bin/bash

cd /root/fastapi-healthcheck

echo "Pulling latest changes..."
git pull origin main

echo "Restarting FastAPI service..."
systemctl restart fastapi

echo "Deployment complete."
EOF

