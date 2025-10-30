# 🤖 ROGUE.AI: The ARTEMIS Incident - Project Summary

## Overview
A complete, standalone, beginner-friendly CTF challenge featuring a "rogue AI" theme. Players hack through multiple layers of security to shut down a malfunctioning AI system called ARTEMIS.

## Challenge Statistics
- **Difficulty:** Beginner to Intermediate
- **Estimated Time:** 1-2 hours for beginners
- **Stages:** 5 progressive challenges
- **Flags:** 5 total
- **Technologies:** Docker, Python, Flask, SSH, Linux

## What Players Learn
1. ✅ **SQL Injection** - Web application exploitation
2. ✅ **Reconnaissance** - File discovery and information gathering
3. ✅ **Linux Basics** - Command line navigation and file manipulation
4. ✅ **SSH Access** - Remote system access
5. ✅ **Privilege Escalation** - SUID exploitation and command injection
6. ✅ **Cryptography** - Basic encoding/decoding

## Project Structure
```
ctf/
├── README.md                      # Main documentation
├── PLAYER_GUIDE.md               # Player walkthrough with hints
├── SOLUTION.md                   # Complete solution for organizers
├── CTFD_SETUP.md                 # CTFd platform integration guide
├── PROJECT_SUMMARY.md            # This file
│
├── Dockerfile                    # Container definition
├── docker-compose.yml            # Easy deployment config
├── start.sh                      # Container startup script
├── deploy.sh                     # One-click deployment script
│
├── challenge/
│   ├── web/                      # Flask web application
│   │   ├── app.py               # Main app with SQL injection vuln
│   │   └── templates/           # HTML templates
│   │       ├── index.html       # Login page
│   │       ├── dashboard.html   # Main dashboard
│   │       ├── logs.html        # System logs page
│   │       └── files.html       # File browser
│   │
│   ├── ssh/                      # SSH challenge files
│   │   ├── backup_tool.c        # Vulnerable SUID binary source
│   │   ├── compile_vuln.sh      # Build script
│   │   ├── welcome.txt          # SSH welcome message
│   │   ├── NOTES.txt            # Hints about vulnerability
│   │   └── .bash_history        # Command history with clues
│   │
│   └── flags/                    # Flag files
│       ├── flag4.txt            # Privilege escalation flag
│       ├── artemis_shutdown.enc # Encrypted final flag
│       ├── decrypt_tool.py      # Decryption script
│       └── create_encrypted.py  # Encryption generation script
│
└── [Project documentation files]
```

## 🚀 Quick Start

### For CTF Organizers
```bash
# 1. Deploy the challenge
./deploy.sh

# 2. Access points:
#    Web: http://localhost:5000
#    SSH: ssh ctfuser@localhost -p 2222

# 3. Test using SOLUTION.md

# 4. Stop when done
docker-compose down
```

### For Players
```bash
# Start at the web interface
http://localhost:5000

# Follow clues to:
# 1. Find first flag (visible on main page)
# 2. Perform SQL injection
# 3. Discover SSH credentials
# 4. Escalate privileges
# 5. Decrypt final shutdown codes
```

## Challenge Flow

```
START
  ↓
[Web Portal] → FLAG 1 (Welcome)
  ↓
[SQL Injection] → FLAG 2 (System Logs)
  ↓
[File Discovery] → FLAG 3 (SSH Credentials)
  ↓
[SSH Access + Privilege Escalation] → FLAG 4 (Root Access)
  ↓
[Decrypt Shutdown Codes] → FLAG 5 (Victory!)
  ↓
END
```

## Technical Details

### Intentional Vulnerabilities
1. **SQL Injection** - app.py:44
   - Direct string concatenation in SQL query
   - No input sanitization
   - Educational SQL injection techniques

2. **Command Injection** - backup_tool.c:27
   - Unsanitized user input passed to `system()`
   - SUID binary running as root
   - Classic privilege escalation vulnerability

3. **Information Disclosure**
   - Backup configuration files exposed
   - SSH credentials in plaintext
   - Command history visible

### Security Controls (For Safe Deployment)
- Container isolation via Docker
- No outbound network access needed
- Runs on non-standard ports
- Easy cleanup and reset
- No persistent data outside container

## Flags Summary

| # | Flag | Challenge | Difficulty |
|---|------|-----------|------------|
| 1 | `CTF{w3lc0me_to_th3_syst3m}` | Visual inspection | Easy |
| 2 | `CTF{sql_1nj3ct10n_m4st3r}` | SQL injection | Easy |
| 3 | `CTF{ssh_4cc3ss_gr4nt3d}` | File discovery | Easy |
| 4 | `CTF{pr1v1l3g3_3sc4l4t10n_pwn3d}` | Privilege escalation | Medium |
| 5 | `CTF{4rt3m1s_shutd0wn_c0mpl3t3}` | Cryptography | Easy |

## Deployment Options

### 1. Single Shared Instance
- One container for all players
- **Pros:** Easy to manage, low resources
- **Cons:** Players may interfere with each other
- **Use Case:** Small events, workshops

### 2. Per-Team Instances
- One container per team
- **Pros:** Isolated, fair competition
- **Cons:** More resources required
- **Use Case:** Competitions, larger events

### 3. On-Demand Deployment
- Containers spawned per request
- **Pros:** Resource efficient, scalable
- **Cons:** Requires orchestration platform
- **Use Case:** Online CTFs, training platforms

## Resource Requirements

### Per Instance
- **CPU:** 0.5 cores
- **RAM:** 512 MB
- **Disk:** 1 GB
- **Ports:** 2 (web + SSH)

### For 20 Teams
- **CPU:** 10 cores
- **RAM:** 10 GB
- **Disk:** 20 GB
- **Bandwidth:** Minimal

## Testing Checklist

- [x] Docker build completes successfully
- [x] Web interface loads and displays FLAG 1
- [x] SQL injection bypasses authentication
- [x] Admin access reveals system logs with FLAG 2
- [x] Config file contains SSH credentials and FLAG 3
- [x] SSH service accepts connections
- [x] Welcome message displays on login
- [x] SUID binary has correct permissions
- [x] Command injection grants root access
- [x] FLAG 4 readable as root
- [x] Decryption tool works and displays FLAG 5

## Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Main documentation and setup | Organizers |
| `PLAYER_GUIDE.md` | Walkthrough with hints | Players |
| `SOLUTION.md` | Complete solution | Organizers |
| `CTFD_SETUP.md` | CTFd integration guide | Platform admins |
| `PROJECT_SUMMARY.md` | This overview | Everyone |

## Customization Guide

### Easy Modifications
- Change flag formats (app.py, flag files)
- Adjust difficulty (add/remove hints)
- Modify theme (HTML templates)
- Change credentials (Dockerfile, app.py)

### Advanced Modifications
- Add more stages
- Implement additional vulnerabilities
- Add network challenges
- Include forensics elements
- Add time-based restrictions

## Educational Value

This challenge demonstrates:
- **Real-world vulnerabilities** that exist in production systems
- **Proper attack methodology** from reconnaissance to exploitation
- **Hands-on learning** more effective than theory
- **Progressive difficulty** builds confidence
- **Immediate feedback** from flags motivates learners

## Success Metrics

### For a successful deployment:
- ✅ 70%+ completion rate for beginners
- ✅ Clear, helpful error messages
- ✅ Engaging theme and storyline
- ✅ Educational value in every stage
- ✅ Stable, reliable infrastructure
- ✅ Positive player feedback

## Future Enhancements

Potential additions:
- [ ] Web-based terminal (xterm.js)
- [ ] Real-time hint system
- [ ] Automated scoring API
- [ ] Multiple difficulty levels
- [ ] Additional vulnerability types
- [ ] Multiplayer cooperative mode
- [ ] Leaderboard integration
- [ ] Achievement system

## Support and Maintenance

### Common Issues
See `README.md` troubleshooting section

### Reset Challenge
```bash
docker-compose down
docker-compose up -d --build
```

### View Logs
```bash
docker-compose logs -f
```

### Update Challenge
```bash
git pull  # if using git
docker-compose down
docker-compose up -d --build
```

## Credits

**Created for:** Beginner CTF players learning cybersecurity

**Theme:** AI Gone Rogue / Robots-style hacking

**Technologies Used:**
- Docker & Docker Compose
- Python 3 & Flask
- OpenSSH
- Ubuntu 22.04
- SQLite3
- HTML/CSS

## License

Educational use encouraged. Modify freely for your CTF events!

---

## Quick Reference Commands

```bash
# Deploy
./deploy.sh

# Stop
docker-compose down

# Rebuild
docker-compose up -d --build

# View logs
docker-compose logs -f

# Access container
docker exec -it rogue-ai-artemis bash

# Reset database
docker-compose down && docker-compose up -d --build
```

---

**🎉 Challenge Complete! Ready for deployment!**

For detailed instructions, see:
- **Organizers:** `README.md` and `SOLUTION.md`
- **Players:** `PLAYER_GUIDE.md`
- **CTFd Setup:** `CTFD_SETUP.md`
