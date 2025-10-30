#!/bin/bash

# Start SSH service
service ssh start

# Start Flask web application as ctfuser
su - ctfuser -c "cd /home/ctfuser/web && python3 app.py" &

# Keep container running
tail -f /dev/null
