#!/usr/bin/env python3
"""
ARTEMIS Shutdown Decryption Tool
Decrypts the AI core shutdown codes
"""

import base64

def decrypt_shutdown_code(encrypted_file):
    """Simple base64 + XOR decryption"""
    try:
        with open(encrypted_file, 'r') as f:
            encrypted_data = f.read().strip()

        # Step 1: Base64 decode
        decoded = base64.b64decode(encrypted_data)

        # Step 2: XOR with key
        key = b'ARTEMIS'
        decrypted = bytearray()
        for i, byte in enumerate(decoded):
            decrypted.append(byte ^ key[i % len(key)])

        return decrypted.decode('utf-8')
    except Exception as e:
        return f"Decryption failed: {str(e)}"

if __name__ == '__main__':
    print("=" * 60)
    print("  ARTEMIS AI CORE - SHUTDOWN SEQUENCE DECRYPTOR")
    print("=" * 60)
    print()

    encrypted_file = '/root/artemis_shutdown.enc'
    print(f"Reading encrypted file: {encrypted_file}")
    print()

    result = decrypt_shutdown_code(encrypted_file)
    print("DECRYPTED OUTPUT:")
    print("-" * 60)
    print(result)
    print("-" * 60)
