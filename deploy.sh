#!/bin/bash

echo "========================================"
echo "  ROGUE.AI CTF Challenge - Deployment"
echo "========================================"
echo ""

# Check if running with appropriate privileges
if [ "$EUID" -ne 0 ] && ! groups | grep -q docker; then
    echo "⚠️  Warning: This script requires either:"
    echo "   - Running with sudo: sudo ./deploy.sh"
    echo "   - User in docker group: sudo usermod -aG docker $USER"
    echo ""
    echo "Current user: $(whoami)"
    echo "Current groups: $(groups)"
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed"
    echo "Please install Docker first: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Error: Docker Compose is not installed"
    echo "Please install Docker Compose first: https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✓ Docker found"
echo "✓ Docker Compose found"
echo ""

# Stop any existing containers
echo "Stopping any existing containers..."
docker-compose down 2>/dev/null

# Build and start the challenge
echo ""
echo "Building and starting the CTF challenge..."
echo "This may take a few minutes on first run..."
echo ""

docker-compose up -d --build

# Wait for services to start
echo ""
echo "Waiting for services to initialize..."
sleep 5

# Check if container is running
if [ "$(docker ps -q -f name=rogue-ai-artemis)" ]; then
    echo ""
    echo "========================================"
    echo "  ✅ CTF Challenge Successfully Deployed!"
    echo "========================================"
    echo ""
    echo "🌐 Web Interface: http://localhost:5000"
    echo "🔐 SSH Access: ssh ctfuser@localhost -p 2222"
    echo ""
    echo "📋 First steps:"
    echo "   1. Open http://localhost:5000 in your browser"
    echo "   2. Look for the first flag on the main page"
    echo "   3. Try to login (hint: SQL injection or default creds)"
    echo ""
    echo "📚 Full player guide: see PLAYER_GUIDE.md"
    echo ""
    echo "🛑 To stop the challenge: docker-compose down"
    echo "📊 View logs: docker-compose logs -f"
    echo ""
else
    echo ""
    echo "❌ Error: Container failed to start"
    echo "Check logs with: docker-compose logs"
    exit 1
fi
