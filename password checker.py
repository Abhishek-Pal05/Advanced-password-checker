import random
import string
import math
import re
import requests
import hashlib
import pyperclip
import time
import json
from cryptography.fernet import Fernet
import os

VAULT_FILE = "vault.json"
KEY_FILE = "vault.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, 'rb') as f:
        return f.read()

fernet = Fernet(load_key())

# Password Strength Checker
def calculate_entropy(password):
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'\d', password):
        pool_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        pool_size += len('!@#$%^&*(),.?":{}|<>')
    entropy = len(password) * math.log2(pool_size) if pool_size else 0
    return round(entropy, 2)

def check_password_strength(password):
    entropy = calculate_entropy(password)
    print(f"\n🔎 Password: {password}")
    print(f"Entropy: {entropy} bits")
    if entropy < 28:
        print("Strength: ❌ Very Weak")
    elif 28 <= entropy < 36:
        print("Strength: ⚠️ Weak")
    elif 36 <= entropy < 60:
        print("Strength: ✅ Moderate")
    else:
        print("Strength: 🔐 Strong")

# ========== Breach Check ==========
def check_breach(password):
    sha1_pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_pwd[:5]
    suffix = sha1_pwd[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    hashes = response.text.splitlines()

    for line in hashes:
        h, count = line.split(":")
        if h == suffix:
            print(f"⚠️ This password has been found in data breaches {count} times!")
            return True
    print("✅ This password was NOT found in any known breaches.")
    return False

# ========== Password Generator ==========
def generate_password(length=16):
    if length < 8:
        print("⚠️ It's recommended to use at least 8 characters.")
        return ""
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# ========== Clipboard & Auto-Clear ==========
def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("📋 Password copied to clipboard. Will auto-clear in 10 seconds...")
    time.sleep(10)
    pyperclip.copy('')
    print("🧹 Clipboard cleared.")

# ========== Save to Encrypted Vault ==========
def save_to_vault(password):
    entry = {"password": password}
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, 'rb') as f:
            encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            data = json.loads(decrypted_data)
    else:
        data = []

    data.append(entry)
    encrypted_data = fernet.encrypt(json.dumps(data).encode())
    with open(VAULT_FILE, 'wb') as f:
        f.write(encrypted_data)
    print("✅ Password saved to encrypted vault.")

# ========== Main Menu ==========
def main():
    print("🔐 Advanced Password Checker & Generator 🔐")
    while True:
        print("\nChoose an option:")
        print("1. Check password strength")
        print("2. Generate strong password")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            pwd = input("Enter password to check: ")
            check_password_strength(pwd)
            check_breach(pwd)
        elif choice == '2':
            length = int(input("Enter desired length (default 16): ") or "16")
            new_pwd = generate_password(length)
            print(f"\n🔐 Generated Password: {new_pwd}")
            check_password_strength(new_pwd)
            check_breach(new_pwd)
            copy_to_clipboard(new_pwd)
            save = input("💾 Save this password to vault? (y/n): ").lower()
            if save == 'y':
                save_to_vault(new_pwd)
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
