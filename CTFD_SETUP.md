# CTFd Setup Guide for ROGUE.AI Challenge

This guide explains how to add this challenge to your CTFd platform.

## Challenge Configuration

### Basic Information
- **Name:** ROGUE.AI - The ARTEMIS Incident
- **Category:** Web / Linux
- **Type:** Standard or Dynamic Scoring
- **Description:**
  ```
  🤖 ARTEMIS AI System - Emergency Access Required

  ARTEMIS, our corporate AI security system, has gone rogue and locked everyone out.
  Your mission is to hack through multiple security layers to shut down the AI before it's too late!

  This is a multi-stage challenge designed for beginners. You'll learn:
  - SQL Injection
  - File Discovery
  - SSH Access
  - Linux Privilege Escalation
  - Basic Cryptography

  🌐 Web Interface: http://YOUR_SERVER:5000
  🔐 SSH Access: ssh ctfuser@YOUR_SERVER -p 2222

  Find 5 flags throughout your journey!
  ```

### Points and Flags

#### Option 1: Single Challenge with 5 Flags (Recommended for Beginners)
Create one challenge with all 5 flags:

- **Initial Points:** 500
- **Flags (all accepted):**
  - `CTF{w3lc0me_to_th3_syst3m}`
  - `CTF{sql_1nj3ct10n_m4st3r}`
  - `CTF{ssh_4cc3ss_gr4nt3d}`
  - `CTF{pr1v1l3g3_3sc4l4t10n_pwn3d}`
  - `CTF{4rt3m1s_shutd0wn_c0mpl3t3}`
- **Flag Type:** Static (case-insensitive)

#### Option 2: Progressive Challenges (Recommended for Competition)
Create 5 separate challenges that unlock sequentially:

1. **ROGUE.AI - Part 1: Initial Access**
   - Points: 50
   - Flag: `CTF{w3lc0me_to_th3_syst3m}`
   - Requirements: None

2. **ROGUE.AI - Part 2: SQL Injection**
   - Points: 100
   - Flag: `CTF{sql_1nj3ct10n_m4st3r}`
   - Requirements: Complete Part 1

3. **ROGUE.AI - Part 3: File Discovery**
   - Points: 100
   - Flag: `CTF{ssh_4cc3ss_gr4nt3d}`
   - Requirements: Complete Part 2

4. **ROGUE.AI - Part 4: Privilege Escalation**
   - Points: 150
   - Flag: `CTF{pr1v1l3g3_3sc4l4t10n_pwn3d}`
   - Requirements: Complete Part 3

5. **ROGUE.AI - Part 5: Final Shutdown**
   - Points: 100
   - Flag: `CTF{4rt3m1s_shutd0wn_c0mpl3t3}`
   - Requirements: Complete Part 4

**Total Points:** 500

### Connection Info
Add this to the "Connection Info" field:
```
🌐 Web: http://YOUR_CTF_SERVER:5000
🔐 SSH: ssh ctfuser@YOUR_CTF_SERVER -p 2222
📚 Hints and guides available in challenge files
```

### Hints (Optional - Recommended for Beginners)

#### Hint 1 (50 points):
```
For SQL injection, try entering ' OR '1'='1 in the username field.
This makes the database query always return true!
```

#### Hint 2 (25 points):
```
After logging in as admin, check the File Browser for configuration
backup files (.bak). They often contain sensitive information.
```

#### Hint 3 (75 points):
```
Once you have SSH access, search for SUID binaries:
find / -perm -4000 2>/dev/null

SUID binaries run with their owner's permissions. If owned by root and vulnerable,
you can escalate privileges!
```

#### Hint 4 (50 points):
```
The backup_tool is vulnerable to command injection. Try using a semicolon (;)
to inject additional commands:
backup_tool "; /bin/bash"
```

### Files to Upload
You can attach these files to the challenge in CTFd:
- `SOLUTION.md (organizers only)` - Complete player walkthrough
- `deploy.sh` - Deployment script (for reference)

### Tags
Add these tags for better organization:
- `web`
- `linux`
- `sql-injection`
- `privilege-escalation`
- `beginner-friendly`
- `multi-stage`

## Deployment Options

### Option 1: Per-Team Instance (Recommended)
Deploy one container per team to prevent interference:

```yaml
# docker-compose-team1.yml
version: '3.8'
services:
  artemis-ctf-team1:
    build: .
    container_name: rogue-ai-team1
    ports:
      - "5001:5000"
      - "2221:22"
    restart: unless-stopped
```

Repeat for each team with different ports.

### Option 2: Shared Instance (Not Recommended)
Use a single instance for all teams. Note: Teams may interfere with each other.

### Option 3: On-Demand Deployment
Use a tool like [ctfd-whale](https://github.com/frankli0324/ctfd-whale) for automatic per-user container deployment.

## Infrastructure Requirements

### Minimum per instance:
- **CPU:** 0.5 cores
- **RAM:** 512 MB
- **Disk:** 1 GB
- **Ports:** 2 (one for web, one for SSH)

### For 20 teams:
- **CPU:** 10 cores
- **RAM:** 10 GB
- **Disk:** 20 GB
- **Network:** Firewall rules to allow ports 5000-5020 and 2220-2240

## Security Considerations

1. **Network Isolation:** Deploy in an isolated network or use Docker network isolation
2. **Resource Limits:** Set CPU and memory limits in docker-compose.yml:
   ```yaml
   deploy:
     resources:
       limits:
         cpus: '0.5'
         memory: 512M
   ```
3. **Monitoring:** Log all container activities
4. **Cleanup:** Automatically restart containers between rounds to reset state

## Testing Before Competition

1. Deploy the challenge on your test server
2. Go through the complete solution (see SOLUTION.md)
3. Verify all flags are accessible
4. Test with a beginner to ensure difficulty is appropriate
5. Check server performance under load

## Player Support

### Common Questions

**Q: I can't connect to SSH**
A: Make sure you're using the correct port (usually 2222) and wait 10-15 seconds after deployment.

**Q: How do I do SQL injection?**
A: Try entering `' OR '1'='1` in the username field. This bypasses the authentication.

**Q: I'm stuck on privilege escalation**
A: Look for files in the home directory that might give you hints. Use `find / -perm -4000 2>/dev/null` to find SUID binaries.

**Q: What's a SUID binary?**
A: It's a program that runs with the file owner's permissions, not the user running it. If it's owned by root and has vulnerabilities, you can use it to gain root access.

## Monitoring and Maintenance

### Check if containers are running:
```bash
docker ps | grep artemis
```

### View logs:
```bash
docker logs rogue-ai-artemis
```

### Restart a container:
```bash
docker-compose restart
```

### Reset challenge (clean state):
```bash
docker-compose down
docker-compose up -d --build
```

## Scoring Suggestions

### Static Scoring:
- All 5 flags in one challenge: **500 points**
- Split into 5 challenges: **50, 100, 100, 150, 100 points**

### Dynamic Scoring:
- **Initial Value:** 500 points
- **Minimum Value:** 100 points
- **Decay Function:** Linear or logarithmic based on solves

## Post-Competition

After the competition:
1. Collect feedback from participants
2. Review solve rates to adjust difficulty
3. Check if any unintended solutions were found
4. Share the official solution and walkthrough

## Additional Resources

- Player Guide: `SOLUTION.md (organizers only)`
- Solution Walkthrough: `SOLUTION.md`
- Technical Documentation: `README.md`

---

**Good luck with your CTF! 🚀**

For questions or issues, refer to the main README.md or create an issue in your challenge repository.
