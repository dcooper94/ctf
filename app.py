
from flask import Flask, render_template, request, redirect, url_for
import os
import json
from datetime import datetime

app = Flask(__name__)

FLAG_DIR = "flags"
SCOREBOARD_FILE = "logs/scoreboard.json"

challenge_meta = {
    1: {
        "title": "Echoes of Control",
        "description": "An AI control panel remains accessible. Can you override its restrictions?",
        "hint": "Check the form elements using browser dev tools.",
        "asset_url": None
    },
    2: {
        "title": "Visual Drift",
        "description": "The AI embedded its memory in an image. Recover the drift key.",
        "hint": "Use steg tools like zsteg or stegsolve. It's LSB.",
        "asset_url": "/static/challenge_assets/corrupted_neural.png"
    },
    3: {
        "title": "Bootstrapped Conscience",
        "description": "This binary reveals the AI's evolving logic. Reverse it to stop it.",
        "hint": "Try 'strings' or reverse in Ghidra.",
        "asset_url": "/static/challenge_assets/ai_boot.out"
    },
    4: {
        "title": "Encrypted Directive",
        "description": "A transmission was intercepted. Decrypt the AI’s directive.",
        "hint": "Decrypt with Vigenère. Key is NEURALCORE.",
        "asset_url": None
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
    return render_template("index.html", challenge_titles={cid: data["title"] for cid, data in challenge_meta.items()})

@app.route("/challenge/<int:cid>", methods=["GET", "POST"])
def challenge_page(cid):
    if cid not in challenge_meta:
        return "Challenge not found", 404

    message = ""
    if request.method == "POST":
        name = request.form.get("name").strip()
        flag = request.form.get("flag").strip()
        correct_flag = get_flag(cid)
        scoreboard = load_scoreboard()

        if flag == correct_flag:
            scoreboard.setdefault(name, [])
            if f"challenge_{cid}" not in scoreboard[name]:
                scoreboard[name].append(f"challenge_{cid}")
            save_scoreboard(scoreboard)
            message = "✅ Correct flag submitted!"
        else:
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
