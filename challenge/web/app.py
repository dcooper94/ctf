#!/usr/bin/env python3
from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import os
import sys

app = Flask(__name__)
app.secret_key = 'artemis_secret_key_do_not_share'

DATABASE = '/home/ctfuser/web/database.db'

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

@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Initialize database on startup
    if not os.path.exists(DATABASE):
        init_db()

    # Run Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
