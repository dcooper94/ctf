
from flask import Flask, request
import datetime

app = Flask(__name__)

def log_event(event_type, content):
    with open('logs/ctf_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()} - {event_type}: {content}\n")

@app.route('/log/access', methods=['GET'])
def access_log():
    log_event("Access", request.args.get('challenge', 'Unknown'))
    return 'Access logged'

@app.route('/log/submit', methods=['POST'])
def submit_log():
    flag = request.form.get('flag', 'NoFlag')
    log_event("Submission", flag)
    return 'Submission logged'

if __name__ == "__main__":
    app.run(debug=False, port=5001)
