#!/usr/bin/env python3
"""
Script to create the encrypted shutdown file
"""

import base64

def encrypt_message(message):
    """Simple XOR + base64 encryption"""
    key = b'ARTEMIS'
    encrypted = bytearray()

    for i, char in enumerate(message.encode('utf-8')):
        encrypted.append(char ^ key[i % len(key)])

    # Base64 encode
    return base64.b64encode(bytes(encrypted)).decode('utf-8')

if __name__ == '__main__':
    final_message = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     🎊 FINAL FLAG - ARTEMIS SHUTDOWN COMPLETE! 🎊         ║
║                                                           ║
║  FLAG #5: CTF{4rt3m1s_shutd0wn_c0mpl3t3}                 ║
║                                                           ║
║  You've successfully completed the challenge!            ║
║                                                           ║
║  Skills Demonstrated:                                    ║
║  ✓ SQL Injection                                         ║
║  ✓ File Discovery & Analysis                            ║
║  ✓ SSH Access                                            ║
║  ✓ Linux Privilege Escalation                           ║
║  ✓ Basic Cryptography                                    ║
║                                                           ║
║  ARTEMIS has been shut down. The system is secure.       ║
║  Thank you for saving us from the rogue AI!              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""

    encrypted = encrypt_message(final_message)
    with open('artemis_shutdown.enc', 'w') as f:
        f.write(encrypted)

    print("Encrypted file created: artemis_shutdown.enc")
    print(f"Encrypted content:\n{encrypted}")
