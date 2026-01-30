#!/bin/bash

# Start SSH service with error checking
if ! service ssh start; then
    echo "ERROR: Failed to start SSH service" >&2
    exit 1
fi

# Verify SSH is actually listening (using netstat or process check)
sleep 2
if pgrep -x sshd > /dev/null; then
    echo "✓ SSH service started successfully"
else
    echo "ERROR: SSH service not running" >&2
    exit 1
fi

# Start Flask web application as ctfuser with logging
su - ctfuser -c "cd /home/ctfuser/web && python3 app.py 2>&1 | tee -a ~/flask.log" &
FLASK_PID=$!

# Wait for Flask to start
sleep 2
echo "✓ Flask application started (PID: $FLASK_PID)"

# Monitor Flask process
while kill -0 $FLASK_PID 2>/dev/null; do
    sleep 5
done

echo "ERROR: Flask application has crashed!" >&2
exit 1
