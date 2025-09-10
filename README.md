# 🧠 AI Gone Rogue — CTF Challenge

A standalone, self-hosted beginner-to-intermediate Capture The Flag (CTF) experience.  
Track down a rogue AI's memory leaks, encrypted messages, and bootloader exploits to stop its escape.

---

## 🚀 How to Run

1. **create a venv inside the ctf folder**
   ```bash
   python3 -m venv venv
   ```
and then activate the virtual environment 
   ```bash
   source venv/bin/activate
   ```
>[!NOTE]
>You can exit the virtual environment at any time with:

   ```bash
   deactivate
   ```

2. **Run the server**
   ```bash
   python3 app.py
   ```

3. **Visit**  
   http://localhost:5000

---

## 📁 Project Structure

```
📦 root/
├── app.py                      # 🔁 Main Flask server and routing logic
├── templates/                 # 🎨 HTML templates for each challenge + main UI
├── static/
│   ├── css/                   # 💅 CSS styles
│   ├── js/                    # 🧠 JS logic and flag submission
│   └── challenge_assets/      # 📎 Public files (images, binaries, source)
├── flags/                     # 🔐 Secure flag storage (NOT publicly served)
│   ├── challenge_1.txt
│   ├── challenge_2.txt
│   └── ...
├── logs/
│   ├── scoreboard.json        # 🏆 Per-user score tracking
│   └── ctf_log.txt            # 📝 Event logs (access + flag submits)
└── README.md                  # 📘 You're here
```

---

## 🧩 Challenges Overview

| ID | Title                    | Category         | Description Summary                             |
|----|--------------------------|------------------|--------------------------------------------------|
| 1  | Echoes of Control        | Web Exploitation | Chat with the rogue AI, uncover its control panel at `Echoes_of_Control/control_panel.php`, and inspect it for the override code |
| 2  | Visual Drift             | Steganography    | Extract hidden memory from a corrupted image     |
| 3  | Bootstrapped Conscience | Reversing        | Reverse an obfuscated binary boot directive      |
| 4  | Encrypted Directive      | Crypto           | Decrypt a layered Vigenère + Base64 transmission |

Each challenge is solved by submitting a flag in the format:

```
coops{...}
```

---

## 🛡️ Logging

- All flag submissions and challenge accesses are logged in:
  - `logs/ctf_log.txt`  
  - Format includes timestamp, challenge ID, user name, and status
- Scoreboard data is stored in:
  - `logs/scoreboard.json`

---

## 🧪 Testing It

Test access:
```bash
curl http://localhost:5000/challenge/1
```

Test a flag submission:
```bash
curl -X POST http://localhost:5000/challenge/1 \
  -F "name=testuser" \
  -F "flag=coops{test_flag}"
```

---

## 📦 Deployment Notes

- Fully offline — no internet access required
- Best hosted as a standalone Flask app on a subdomain or VPS
- Not compatible with WordPress without full reimplementation in PHP

---

Made for cyber explorers 👾
