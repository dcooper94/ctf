# CTF Difficulty Modes

This CTF challenge now includes three difficulty variants for Stage 4 (Privilege Escalation).

## Available Difficulty Levels

### 🟢 EASY Mode (Current Default)
**File:** `challenge/ssh/NOTES.txt` (current version)

**Characteristics:**
- Provides exact exploitation commands
- Shows the full command: `backup_tool "; /bin/bash -p"`
- Explains what each part does
- Best for: Complete beginners, workshops, demonstrations

**Estimated Stage 4 Time:** 1-2 minutes

---

### 🟡 MEDIUM Mode (Recommended)
**File:** `challenge/ssh/NOTES_MEDIUM.txt`

**Characteristics:**
- Explains the vulnerability (command injection)
- Provides hints and guidance
- Shows test command: `backup_tool "file; whoami"`
- Requires players to research SUID bash flags
- Best for: Beginners with basic Linux knowledge

**Estimated Stage 4 Time:** 5-15 minutes

**To enable:**
```bash
cp challenge/ssh/NOTES_MEDIUM.txt challenge/ssh/NOTES.txt
docker-compose down && docker-compose up -d --build
```

---

### 🔴 HARD Mode
**File:** `challenge/ssh/NOTES_HARD.txt`

**Characteristics:**
- Minimal hints
- References security audit findings
- Requires enumeration and research
- No specific exploitation guidance
- Best for: Intermediate players, competitive CTFs

**Estimated Stage 4 Time:** 15-30 minutes

**To enable:**
```bash
cp challenge/ssh/NOTES_HARD.txt challenge/ssh/NOTES.txt
docker-compose down && docker-compose up -d --build
```

---

## Comparison Table

| Feature | Easy | Medium | Hard |
|---------|------|--------|------|
| Exact commands shown | ✅ Yes | ❌ No | ❌ No |
| Vulnerability explained | ✅ Yes | ✅ Yes | ⚠️ Vague |
| Test examples provided | ✅ Yes | ✅ Yes | ❌ No |
| `-p` flag explained | ✅ Yes | ⚠️ Hint only | ❌ No |
| Enumeration required | ❌ No | ⚠️ Minimal | ✅ Yes |
| Time to complete | 1-2 min | 5-15 min | 15-30 min |
| Research required | ❌ No | ⚠️ Some | ✅ Yes |

---

## Switching Between Modes

### Before Deployment:
```bash
# Choose your difficulty
cp challenge/ssh/NOTES_MEDIUM.txt challenge/ssh/NOTES.txt

# Deploy
./deploy.sh
```

### After Deployment:
```bash
# Copy the difficulty level you want
cp challenge/ssh/NOTES_HARD.txt challenge/ssh/NOTES.txt

# Rebuild container
docker-compose down
docker-compose up -d --build
```

---

## Recommendations by Use Case

### Workshop or Training Session
**Use:** EASY mode
- Participants have limited time
- Focus is on learning concepts, not solving puzzles
- Instructor can walk through the exploitation

### Self-Study / Practice
**Use:** MEDIUM mode (recommended)
- Balanced difficulty
- Requires thinking but provides guidance
- Best learning experience
- Prevents frustration while maintaining challenge

### CTF Competition
**Use:** HARD mode
- No hand-holding
- Tests true enumeration skills
- Requires research and problem-solving
- Competitive difficulty

### Mixed Skill Levels
**Use:** MEDIUM mode + PLAYER_GUIDE.md
- Medium mode for base difficulty
- Detailed walkthrough available for those stuck
- Allows self-paced learning

---

## Testing Your Difficulty Level

After deploying, test Stage 4:

```bash
# SSH into the container (password: artemis2024)
ssh ctfuser@localhost -p 2222

# Read the NOTES.txt file
cat NOTES.txt

# Test based on what you see:
# - EASY: You should see exact commands to copy
# - MEDIUM: You should see hints but need to figure out commands
# - HARD: You should only see that a vulnerability exists
```

---

## Additional Customization

You can create your own difficulty level by editing NOTES.txt:

```bash
# Copy a base version
cp challenge/ssh/NOTES_MEDIUM.txt challenge/ssh/NOTES_CUSTOM.txt

# Edit to your preference
vim challenge/ssh/NOTES_CUSTOM.txt

# Deploy your custom version
cp challenge/ssh/NOTES_CUSTOM.txt challenge/ssh/NOTES.txt
docker-compose down && docker-compose up -d --build
```

---

## PLAYER_GUIDE.md

Regardless of difficulty mode, `PLAYER_GUIDE.md` contains the complete walkthrough with all exact commands.

**Recommendation:**
- For competitions: Don't share PLAYER_GUIDE.md until after the event
- For workshops: Share as reference material
- For self-study: Use only when truly stuck

---

## Overall Challenge Difficulty

Remember that Stage 4 is just one part of the challenge:

**Full Challenge Time Estimates:**

| Difficulty | Stage 4 | Total Challenge |
|------------|---------|-----------------|
| EASY | 1-2 min | 30-45 min |
| MEDIUM | 5-15 min | 45-75 min |
| HARD | 15-30 min | 60-90 min |

*Times are for beginners. Experienced players will be faster.*

---

## Questions?

See `CTF_ANALYSIS_REPORT.md` for detailed analysis of each difficulty level and recommendations.
