# AI Gone Rogue - Secure Standalone CTF

## 🚀 How to Run

1. Install dependencies:
```bash
pip install flask
```

2. Start the CTF server:
```bash
python app.py
```

3. Visit: [http://localhost:5000](http://localhost:5000)

## 📦 Notes

- Flags are stored securely in `flags/flag_list.txt`
- User submissions are logged to `logs/ctf_log.txt`
- Challenge artifacts (images, binaries) are served from `static/challenge_assets/`
- Do **not** expose the `flags/` or `logs/` directory on public web servers

## 📁 Structure

- `app.py` - Main Flask server
- `templates/` - HTML templates
- `static/` - CSS, JS, and public challenge files
- `flags/` - Secure flag storage (not publicly served)
- `logs/` - Submission logs
