FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openssh-server \
    sudo \
    vim \
    curl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set up SSH
RUN mkdir /var/run/sshd
RUN echo 'PermitRootLogin no' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Add welcome message to SSH login
RUN echo 'cat ~/welcome.txt 2>/dev/null' >> /etc/bash.bashrc

# Create CTF user
RUN useradd -m -s /bin/bash ctfuser && \
    echo 'ctfuser:artemis2024' | chpasswd

# Create admin user for privilege escalation
RUN useradd -m -s /bin/bash admin && \
    echo 'admin:Sup3rS3cur3P4ss!' | chpasswd

# Install Python packages
RUN pip3 install flask

# Copy web application
COPY challenge/web /home/ctfuser/web
RUN chown -R ctfuser:ctfuser /home/ctfuser/web

# Copy and compile vulnerable binary
COPY challenge/ssh/backup_tool.c /tmp/backup_tool.c
RUN gcc /tmp/backup_tool.c -o /usr/local/bin/backup_tool && \
    chmod 4755 /usr/local/bin/backup_tool && \
    rm /tmp/backup_tool.c

# Copy challenge files to user home
COPY challenge/ssh/welcome.txt /home/ctfuser/welcome.txt
COPY challenge/ssh/NOTES.txt /home/ctfuser/NOTES.txt
COPY challenge/ssh/.bash_history /home/ctfuser/.bash_history
RUN chown -R ctfuser:ctfuser /home/ctfuser/ && \
    chmod 644 /home/ctfuser/.bash_history

# Set up root flags and tools
COPY challenge/flags/flag4.txt /root/flag4.txt
COPY challenge/flags/.flag4.txt /root/.flag4.txt
COPY challenge/flags/artemis_shutdown.enc /root/artemis_shutdown.enc
COPY challenge/flags/decrypt_tool.py /root/decrypt_tool.py
COPY challenge/flags/decryption.key /root/decryption.key
RUN chmod 600 /root/flag4.txt && \
    chmod 600 /root/.flag4.txt && \
    chmod 600 /root/artemis_shutdown.enc && \
    chmod 700 /root/decrypt_tool.py && \
    chmod 600 /root/decryption.key

# Expose ports
EXPOSE 22 5000

# Start services
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
