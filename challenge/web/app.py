#!/usr/bin/env python3
from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import os
import sys

app = Flask(__name__)
app.secret_key = 'artemis_secret_key_do_not_share'

DATABASE = '/home/ctfuser/web/database.db'

# Flag definitions
FLAGS = {
    'flag1': 'CTF{w3lc0me_to_th3_syst3m}',
    'flag2': 'CTF{sql_1nj3ct10n_m4st3r}',
    'flag3': 'CTF{ssh_4cc3ss_gr4nt3d}',
    'flag4': 'CTF{pr1v1l3g3_3sc4l4t10n_pwn3d}',
    'flag5': 'CTF{4rt3m1s_shutd0wn_c0mpl3t3}',
}

def init_db():
    """Initialize the database with sample data"""
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        # Create users table
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)''')

        # Create logs table
        c.execute('''CREATE TABLE IF NOT EXISTS system_logs
                     (id INTEGER PRIMARY KEY, timestamp TEXT, message TEXT, flag TEXT)''')

        # Insert sample users
        c.execute("INSERT OR IGNORE INTO users VALUES (1, 'guest', 'guest123', 'user')")
        c.execute("INSERT OR IGNORE INTO users VALUES (2, 'admin', 'Sup3rS3cur3P4ss!', 'admin')")
        c.execute("INSERT OR IGNORE INTO users VALUES (3, 'artemis', 'AI_CORE_PASSWORD_2024', 'system')")

        # Insert system logs with flag
        c.execute("INSERT OR IGNORE INTO system_logs VALUES (1, '2024-10-29 14:32:11', 'ARTEMIS initialization complete', '')")
        c.execute("INSERT OR IGNORE INTO system_logs VALUES (2, '2024-10-29 15:45:22', 'Security protocols activated', '')")
        c.execute("INSERT OR IGNORE INTO system_logs VALUES (3, '2024-10-30 09:15:33', 'WARNING: Unauthorized access detected', 'CTF{sql_1nj3ct10n_m4st3r}')")
        c.execute("INSERT OR IGNORE INTO system_logs VALUES (4, '2024-10-30 12:00:00', 'ALERT: System lockdown initiated by ARTEMIS', '')")

        # Create submissions table
        c.execute('''CREATE TABLE IF NOT EXISTS submissions
                     (id INTEGER PRIMARY KEY, username TEXT, flag_key TEXT, flag_value TEXT, timestamp TEXT)''')

        conn.commit()

        conn.commit()
        conn.close()
        print("✓ Database initialized successfully", file=sys.stderr)
    except Exception as e:
        print(f"ERROR: Database initialization failed: {e}", file=sys.stderr)
        raise

@app.route('/')
def index():
    """Main page with login form"""
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Vulnerable login endpoint with SQL injection"""
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # VULNERABLE: Direct string concatenation in SQL query
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    try:
        c.execute(query)
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = user[1]
            session['role'] = user[3]
            return redirect(url_for('dashboard'))
        else:
            return render_template('index.html', error='Invalid credentials')
    except Exception as e:
        conn.close()
        return render_template('index.html', error=f'Database error: {str(e)}')

@app.route('/dashboard')
def dashboard():
    """Dashboard page after successful login"""
    if 'username' not in session:
        return redirect(url_for('index'))

    return render_template('dashboard.html',
                         username=session['username'],
                         role=session.get('role', 'user'))

@app.route('/logs')
def logs():
    """System logs page - requires admin role"""
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM system_logs")
    logs_data = c.fetchall()
    conn.close()

    return render_template('logs.html',
                         logs=logs_data,
                         role=session.get('role', 'user'))

@app.route('/files')
def files():
    """File browser - contains hidden SSH credentials"""
    if 'username' not in session:
        return redirect(url_for('index'))

    if session.get('role') == 'admin' or session.get('role') == 'system':
        # Show hidden config file only to admins
        files_list = [
            {'name': 'readme.txt', 'content': 'ARTEMIS System Files - Authorized Personnel Only'},
            {'name': 'config.bak', 'content': '''⚠️ FILE CORRUPTED BY ARTEMIS AI ⚠️
============================================

ERROR: Data encryption protocol activated
Status: LOCKED by AI security system

Encrypted SSH Configuration:
----------------------------
SSH_HOST: localhost
SSH_PORT: 2222
SSH_USER: Y3RmdXNlcg==
SSH_PASS: YXJ0ZW1pczIwMjQ=

HINT: ARTEMIS uses standard encoding protocols.
      Common base encodings are easily reversed...

⚠️ ARTEMIS is watching... decrypt at your own risk.'''},
            {'name': 'diagnostics.log', 'content': 'System diagnostics running...\nLast backup: 2024-10-29 15:30:00\nStatus: All systems nominal'},
        ]
    else:
        files_list = [
            {'name': 'readme.txt', 'content': 'ARTEMIS System Files - Authorized Personnel Only'},
            {'name': 'diagnostics.log', 'content': 'System diagnostics running...'},
        ]

    return render_template('files.html', files=files_list)

@app.route('/leaderboard')
def leaderboard():
    """Display leaderboard with user rankings"""
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Get leaderboard data: username, flag count, first submission time, flags captured
    c.execute('''
        SELECT
            username,
            COUNT(DISTINCT flag_key) as flag_count,
            MIN(timestamp) as first_flag_time,
            GROUP_CONCAT(flag_key, ', ') as flags_captured
        FROM submissions
        GROUP BY username
        ORDER BY flag_count DESC, first_flag_time ASC
    ''')

    leaderboard_data = c.fetchall()
    conn.close()

    # Format data for template
    rankings = []
    for idx, (username, flag_count, first_time, flags) in enumerate(leaderboard_data, 1):
        rankings.append({
            'rank': idx,
            'username': username,
            'flag_count': flag_count,
            'first_time': first_time,
            'flags': flags,
            'is_current_user': username == session['username']
        })

    return render_template('leaderboard.html', rankings=rankings, total_flags=len(FLAGS))

@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """Flag submission endpoint with confetti effect"""
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        player_name = request.form.get('username', '').strip()
        flag_key = request.form.get('flag_key', '').strip()
        flag_value = request.form.get('flag_value', '').strip()

        # Validate player name
        if not player_name or len(player_name) < 2 or len(player_name) > 30:
            return render_template('submit.html', success=False,
                                  error='Username must be between 2-30 characters',
                                  player_name=session.get('player_name', ''))

        # Save player name to session for future submissions
        session['player_name'] = player_name

        # Normalize flag_key: accept "1", "flag 1", "flag1" -> all become "flag1"
        flag_key = flag_key.lower().replace(' ', '')
        if flag_key.isdigit():
            flag_key = f'flag{flag_key}'

        # Debug logging
        print(f"DEBUG: Player='{player_name}' flag_key='{flag_key}', flag_value='{flag_value}'", file=sys.stderr)
        print(f"DEBUG: Expected value for {flag_key}: '{FLAGS.get(flag_key, 'KEY NOT FOUND')}'", file=sys.stderr)
        print(f"DEBUG: Match result: {flag_key in FLAGS and FLAGS[flag_key] == flag_value}", file=sys.stderr)

        # Validate flag
        if flag_key in FLAGS and FLAGS[flag_key] == flag_value:
            # Check if this player already submitted this flag
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('SELECT * FROM submissions WHERE username=? AND flag_key=?',
                      (player_name, flag_key))
            existing = c.fetchone()

            if existing:
                conn.close()
                return render_template('submit.html', success=False,
                                      error=f'You already submitted {flag_key}!',
                                      player_name=player_name)

            # Save submission
            c.execute('''INSERT INTO submissions (username, flag_key, flag_value, timestamp)
                         VALUES (?, ?, ?, datetime('now'))''',
                      (player_name, flag_key, flag_value))
            conn.commit()
            conn.close()

            return render_template('submit.html', success=True, flag_key=flag_key,
                                 flag_value=flag_value, player_name=player_name)
        else:
            return render_template('submit.html', success=False, error='Invalid flag',
                                 player_name=player_name)

    return render_template('submit.html', success=None, player_name=session.get('player_name', ''))

if __name__ == '__main__':
    # Initialize database on startup
    if not os.path.exists(DATABASE):
        init_db()

    # Run Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
