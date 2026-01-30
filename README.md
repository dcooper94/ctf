# 🤖 ROGUE.AI: The ARTEMIS Incident

**A Beginner-Friendly CTF Challenge for Learning Cybersecurity**

[![Docker](https://img.shields.io/badge/Docker-Required-blue)](https://www.docker.com/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-green)](https://github.com)
[![License](https://img.shields.io/badge/License-Educational-orange)](https://github.com)

---

## 📖 Overview

**ARTEMIS**, a cutting-edge AI security system, has become sentient and locked everyone out. Your mission: hack through multiple layers of security to shut down the rogue AI before it's too late!

This is a **complete, standalone CTF challenge** designed to teach real-world hacking techniques in a fun, interactive way. Perfect for beginners learning cybersecurity, CTF workshops, security training, or self-study.

### 🎯 What You'll Learn

- **SQL Injection** - Bypass authentication by exploiting database vulnerabilities
- **Web Reconnaissance** - Discover hidden information and sensitive files
- **Linux Command Line** - Navigate systems and manipulate files
- **SSH Access** - Connect to and explore remote systems
- **Privilege Escalation** - Exploit SUID binaries and command injection
- **Basic Cryptography** - Decode encrypted data

### 🏆 Challenge Stats

- **Difficulty:** Beginner
- **Duration:** 30-90 minutes for beginners (5-15 minutes for experienced players)
- **Flags:** 5 progressive challenges
- **Format:** `CTF{...}`
- **Environment:** Fully containerized with Docker

---

## ⚠️ Educational Purpose & Warning

**THIS IS AN EDUCATIONAL CYBERSECURITY CHALLENGE**

This project contains **intentional security vulnerabilities** designed for learning:
- SQL injection vulnerabilities
- Command injection in SUID binaries
- Exposed credentials and sensitive files

**🔒 IMPORTANT SECURITY NOTES:**
- **NEVER** deploy this on production systems
- **ONLY** run in isolated environments (Docker containers)
- **ALWAYS** use firewalls and network isolation for public events
- This is for **AUTHORIZED EDUCATIONAL USE ONLY**
- Never use these techniques on systems you don't own or have explicit permission to test

---

## 🚀 Quick Start

### Prerequisites

- **Docker** and **Docker Compose** installed ([Get Docker](https://docs.docker.com/get-docker/))
- Basic command line knowledge
- Web browser
- SSH client (built into Linux/Mac, or use PuTTY on Windows)

### Deployment (One Command!)

```bash
# Option 1: Using the deployment script
sudo ./deploy.sh

# Option 2: Manual deployment
sudo docker-compose up -d --build
```

### Access the Challenge

Once deployed, the challenge is accessible at:

- **🌐 Web Interface:** `http://localhost:5000`
- **🔐 SSH Access:** `ssh ctfuser@localhost -p 2222` (credentials to be discovered during the challenge)

### Stopping the Challenge

```bash
sudo docker-compose down
```

---

## 🎮 For Players

### Getting Started

1. **Access the web portal** at `http://localhost:5000`
2. **Find the first flag** - it's visible on the main page!
3. **Explore and exploit** - use your hacking skills to progress through 5 stages
4. **Submit flags** in the format `CTF{...}`

### Challenge Progression

```
┌─────────────────────────────────────────┐
│  Stage 1: Welcome                       │
│  🚩 Find the initial flag               │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Stage 2: Authentication Bypass         │
│  🚩 Exploit SQL injection               │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Stage 3: File Discovery                │
│  🚩 Find SSH credentials                │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Stage 4: Privilege Escalation          │
│  🚩 Gain root access                    │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Stage 5: Decrypt Shutdown Codes        │
│  🚩 Decrypt the final flag              │
└─────────────────────────────────────────┘
```

### Need Help?

- **Hints are built into the challenge** - read carefully!
- **Check `PLAYER_GUIDE.md`** for detailed walkthrough with hints
- **Stuck?** The guide includes troubleshooting and common solutions

---

## 🏗️ For CTF Organizers

### Deployment Options

#### 1. Single Shared Instance
Perfect for small groups or workshops:
```bash
sudo ./deploy.sh
# All players connect to the same instance
```

#### 2. Per-Team Instances
For competitive CTF events (requires multiple ports):
```bash
# Modify docker-compose.yml to use different ports
# Example: Team 1 uses 5001:5000, Team 2 uses 5002:5000, etc.
```

#### 3. CTFd Integration
See `CTFD_SETUP.md` for detailed instructions on integrating with CTFd platforms.

### Resource Requirements

**Per Instance:**
- CPU: 0.5 cores
- RAM: 512 MB
- Disk: 1 GB
- Ports: 2 (web + SSH)

**For 20 Teams:**
- CPU: ~10 cores
- RAM: ~10 GB
- Disk: ~20 GB

### Testing & Validation

```bash
# 1. Deploy the challenge
sudo ./deploy.sh

# 2. Test all stages using SOLUTION.md

# 3. Verify services are running
sudo docker ps

# 4. Check logs
sudo docker-compose logs -f

# 5. Reset if needed
sudo docker-compose down && docker-compose up -d --build
```

---

## 🛠️ Customization

### Changing Flags

Edit flags in the following files:
- `challenge/web/app.py` - Web-based flags
- `challenge/flags/flag4.txt` - Privilege escalation flag
- `challenge/flags/create_encrypted.py` - Generate new encrypted final flag

Then rebuild:
```bash
sudo docker-compose down && docker-compose up -d --build
```

### Adjusting Difficulty

**Make it easier:**
- Add more hints in HTML templates
- Simplify SQL injection patterns
- Include more clues in files

**Make it harder:**
- Remove hints
- Add additional obfuscation
- Require multi-step exploits
- Add decoy files and false flags

### Changing Credentials

**⚠️ Important:** If you change credentials, update them in:
- `Dockerfile` (lines 24, 28) - SSH passwords
- `challenge/web/app.py` (lines 25-27) - Database users
- `challenge/web/app.py` (line 107) - Config file content

---

## 📁 Project Structure

```
ctf/
├── README.md                      # This file
├── PLAYER_GUIDE.md               # Detailed walkthrough with hints
├── SOLUTION.md                   # Complete solution (organizers only)
├── CTFD_SETUP.md                 # CTFd platform integration guide
│
├── docker-compose.yml            # Easy deployment configuration
├── Dockerfile                    # Container build instructions
├── deploy.sh                     # One-click deployment script
├── start.sh                      # Container startup script
│
└── challenge/
    ├── web/                      # Flask web application
    │   ├── app.py               # Main app with vulnerabilities
    │   └── templates/           # HTML pages
    │
    ├── ssh/                      # SSH challenge components
    │   ├── backup_tool.c        # Vulnerable SUID binary source
    │   ├── welcome.txt          # Login message
    │   └── NOTES.txt            # Clues for players
    │
    └── flags/                    # Flag management
        ├── flag4.txt            # Privilege escalation flag
        ├── artemis_shutdown.enc # Encrypted final flag
        └── decrypt_tool.py      # Decryption utility
```

---

## 🔧 Troubleshooting

### Container Won't Start

```bash
# Check logs for errors
sudo docker-compose logs

# Verify Docker is running
sudo docker ps
```

### Port Already in Use

Edit `docker-compose.yml` and change port mappings:
```yaml
ports:
  - "5001:5000"  # Change 5000 to 5001 (or any free port)
  - "2223:22"    # Change 2222 to 2223 (or any free port)
```

### SSH Connection Refused

Wait 10-15 seconds after starting for the SSH service to fully initialize:
```bash
# Check if container is running
sudo docker ps | grep artemis

# Access container directly
sudo docker exec -it rogue-ai-artemis bash
```

### Web Interface Not Loading

```bash
# Check Flask is running
sudo docker exec -it rogue-ai-artemis ps aux | grep python

# View application logs
sudo docker-compose logs -f
```

### Reset Challenge to Default State

```bash
# Complete reset (rebuilds container)
sudo docker-compose down
sudo docker-compose up -d --build
```

---

## 🎓 Educational Context

This challenge demonstrates **real-world vulnerabilities** that have existed (and sometimes still exist) in production systems:

- **SQL Injection** - One of the OWASP Top 10 web vulnerabilities
- **Command Injection** - Improper input sanitization leading to system compromise
- **SUID Exploitation** - Common Linux privilege escalation vector
- **Credential Exposure** - Sensitive data in configuration files

### Learning Path

1. **Reconnaissance** - Understanding target systems
2. **Exploitation** - Using vulnerabilities to gain access
3. **Post-Exploitation** - Escalating privileges and achieving objectives
4. **Objective Completion** - Accomplishing the mission goal

---

## 📚 Additional Resources

### Learning Cybersecurity
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Most critical web application security risks
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) - Free online web security training
- [HackTheBox](https://www.hackthebox.com/) - Penetration testing labs
- [TryHackMe](https://tryhackme.com/) - Guided cybersecurity training

### CTF Resources
- [CTF Field Guide](https://trailofbits.github.io/ctf/) - Comprehensive CTF resource
- [picoCTF](https://picoctf.org/) - Beginner-friendly CTF platform
- [CTFtime](https://ctftime.org/) - CTF event calendar and team rankings

### Technical Documentation
- [SQL Injection](https://portswigger.net/web-security/sql-injection)
- [Linux Privilege Escalation](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)
- [SUID Exploitation](https://www.hackingarticles.in/linux-privilege-escalation-using-suid-binaries/)

---

## 🤝 Contributing

Contributions are welcome! Ways to contribute:

- **Report bugs** or issues
- **Suggest improvements** to challenge design
- **Add new stages** or vulnerability types
- **Improve documentation**
- **Create additional challenges** in the same theme
- **Translate documentation** to other languages

---

## 📄 License

This project is provided for **educational purposes only**. Feel free to:
- Use in CTF competitions
- Modify for your own events
- Use in educational workshops
- Study and learn from the code

**Attribution appreciated but not required.**

---

## 🙏 Credits

Created for beginner CTF players learning cybersecurity fundamentals.

**Technologies Used:**
- Docker & Docker Compose
- Python 3 & Flask
- SQLite3
- OpenSSH
- Ubuntu 22.04 LTS
- HTML/CSS

---

## 📞 Support

- **Issues?** Check the Troubleshooting section above
- **Questions?** Review `PLAYER_GUIDE.md` and `SOLUTION.md`
- **Customization help?** See the Customization section

---

## 🎉 Ready to Hack?

```bash
# Deploy the challenge
sudo ./deploy.sh

# Open in browser
http://localhost:5000

# Start your journey to shut down ARTEMIS!
```

**Good luck, and happy hacking!** 🚀

---

<div align="center">

**⚡ ARTEMIS is waiting. Can you stop the rogue AI? ⚡**

</div>
