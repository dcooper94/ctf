#!/bin/bash
# Compile the vulnerable SUID binary
gcc -o vuln_binary backup_tool.c
chmod 4755 vuln_binary
echo "Vulnerable binary compiled successfully"
