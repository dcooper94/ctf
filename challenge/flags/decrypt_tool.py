#!/usr/bin/env python3
"""
ARTEMIS Shutdown Decryption Tool
Decrypts the AI core shutdown codes
Requires decryption key as argument
"""

import base64
import sys

def decrypt_shutdown_code(encrypted_file, key):
    """Simple base64 + XOR decryption"""
    try:
        with open(encrypted_file, 'r') as f:
            encrypted_data = f.read().strip()

        # Step 1: Base64 decode
        decoded = base64.b64decode(encrypted_data)

        # Step 2: XOR with provided key
        key_bytes = key.encode('utf-8')
        decrypted = bytearray()
        for i, byte in enumerate(decoded):
            decrypted.append(byte ^ key_bytes[i % len(key_bytes)])

        return decrypted.decode('utf-8')
    except Exception as e:
        return f"Decryption failed: {str(e)}"

if __name__ == '__main__':
    print("=" * 60)
    print("  ARTEMIS AI CORE - SHUTDOWN SEQUENCE DECRYPTOR")
    print("=" * 60)
    print()

    # Check for decryption key argument
    if len(sys.argv) < 2:
        print("ERROR: Decryption key required!")
        print()
        print("Usage: python3 decrypt_tool.py <decryption_key>")
        print()
        print("HINT: The decryption key is hidden somewhere in /root/")
        print("      Look for files containing 'key' or 'decrypt'")
        print("      Try: ls -la /root/ | grep -i key")
        print("      Or:  find /root -name '*key*' 2>/dev/null")
        print()
        sys.exit(1)

    decryption_key = sys.argv[1]
    encrypted_file = '/root/artemis_shutdown.enc'

    print(f"Decryption key: {decryption_key}")
    print(f"Reading encrypted file: {encrypted_file}")
    print()

    result = decrypt_shutdown_code(encrypted_file, decryption_key)

    if "Decryption failed" in result or "CTF{" not in result:
        print("DECRYPTION FAILED!")
        print("-" * 60)
        print("The decryption key you provided is incorrect.")
        print("Make sure you're using the exact key from the key file.")
        print("-" * 60)
    else:
        print("DECRYPTED OUTPUT:")
        print("-" * 60)
        print(result)
        print("-" * 60)
