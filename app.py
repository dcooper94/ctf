
from flask import Flask, render_template, request, redirect, url_for
import os
import json
from datetime import datetime

app = Flask(__name__)

FLAG_DIR = "flags"

SCOREBOARD_FILE = "logs/scoreboard.json"
def log_event(event_type, cid, user=None, status=None):
    log_path = "logs/ctf_log.txt"
    with open(log_path, "a") as log_file:
        log_file.write(f"[{datetime.now()}] EVENT: {event_type} | CHALLENGE: {cid} | USER: {user or 'anonymous'} | STATUS: {status or 'N/A'}\n")
        
challenge_meta = {
    1: {
        "title": "Echoes of Control",
        "description": "A web-based control panel prototype for the AI assistant 'Echo' has surfaced. Initial inspection shows it behaves normally… but deeper inspection may reveal remnants of unauthorized control logic embedded in the interface.",
        "hint": "Inspect the HTML source and look for hidden form fields or JavaScript.",
        "asset_url": None
    },
    2: {
        "title": "Visual Drift",
        "description": "You’ve extracted a corrupted visual output from the AI’s internal dream-like rendering system. While the surface appears organic, there's suspicion that deeper data layers were used to smuggle commands between neural modules.",
        "hint": "Use steg tools like `zsteg` or `stegsolve`. Look for LSB-encoded data.",
        "asset_url": "/static/challenge_assets/drift_secret.jpg"
    },
    3: {
        "title": "Bootstrapped",
        "description": "You've extracted a binary used during the AI's core boot process. It's small, deliberately obfuscated, and used for verifying logic integrity during startup. The flag is checked in memory against a hardcoded obfuscated value.",
        "hint": "Analyze the source logic. A hardcoded value is obfuscated — decode it to proceed.",
        "asset_url": "/static/challenge_assets/ai_boot.c"
    },
    4: {
        "title": "Encrypted Directive",
    "description": "You've unlocked access to the AI's directive memory. The message is encrypted — but not in a simple way. Something's layered inside, and its key isn't obvious at first glance.",
    "hint": "What’s buried in memory was buried twice. The access key? You already typed it — before the system granted entry.",
        "asset_url": "/static/challenge_assets/locked_directive.mem"
    }
}


def load_scoreboard():
    if not os.path.exists(SCOREBOARD_FILE):
        return {}
    with open(SCOREBOARD_FILE, "r") as f:
        return json.load(f)

def save_scoreboard(data):
    with open(SCOREBOARD_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_flag(cid):
    with open(os.path.join(FLAG_DIR, f"challenge_{cid}.txt")) as f:
        return f.read().strip()

@app.route("/")
def home():
    return render_template("index.html", challenge_meta=challenge_meta)

@app.route("/challenge/<int:cid>", methods=["GET", "POST"])
def challenge_page(cid):
    if cid not in challenge_meta:
        return "Challenge not found", 404
        log_event("ACCESS", cid)

    message = ""
    if request.method == "POST":
        name = request.form.get("name").strip()
        flag = request.form.get("flag").strip()
        correct_flag = get_flag(cid)
        scoreboard = load_scoreboard()
        key = f"challenge_{cid}"

        if flag == correct_flag:
            if name not in scoreboard:
                scoreboard[name] = {}
            if key not in scoreboard[name]:
                scoreboard[name][key] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_scoreboard(scoreboard)
            message = "✅ Correct flag submitted!"
        else:
            message = "❌ Incorrect flag."
if flag == correct_flag:
    ...
    log_event("SUBMIT", cid, user=name, status="correct")
    message = "✅ Correct flag submitted!"
else:
    log_event("SUBMIT", cid, user=name, status="incorrect")
    message = "❌ Incorrect flag."
    return render_template(f"challenge_{cid}.html", 
        title=challenge_meta[cid]["title"],
        description=challenge_meta[cid]["description"],
        hint=challenge_meta[cid]["hint"],
        asset_url=challenge_meta[cid]["asset_url"],
        message=message
    )

@app.route("/scoreboard")
def scoreboard():
    scoreboard = load_scoreboard()
    sorted_scores = dict(sorted(scoreboard.items(), key=lambda x: len(x[1]), reverse=True))
    return render_template("scoreboard.html", scoreboard=sorted_scores)

if __name__ == "__main__":
    app.run(debug=True)
