
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "logs/ctf_log.txt"
FLAG_FILE = "flags/flag_list.txt"

def log_event(event_type, content):
    with open(LOG_FILE, 'a') as log:
        log.write(f"{datetime.now()} - {event_type}: {content}\n")

@app.route("/")
def home():
    log_event("Access", "index")
    return render_template("index.html")

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

@app.route("/submit", methods=["POST"])
def submit_flag():
    flag = request.form.get("flag", "")
    log_event("Submission", flag)
    with open(FLAG_FILE, 'r') as f:
        valid_flags = [line.strip() for line in f.readlines()]
    if flag.strip() in valid_flags:
        return "✅ Correct Flag!"
    else:
        return "❌ Incorrect. Try again."

if __name__ == "__main__":
    app.run(debug=True)
