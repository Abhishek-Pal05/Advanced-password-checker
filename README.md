Advanced Password Checker

Purpose

The Advanced Password Checker is a Python-based security tool designed to help users:

Evaluate the strength of their passwords.

Generate strong and secure passwords.

Check whether their passwords have appeared in known data breaches.

Manage passwords securely using encryption.

Promote cybersecurity awareness and better password practices.

This project is ideal for students, ethical hackers, and developers who want to showcase security-focused tools on their resume or GitHub portfolio.

Features

Password Strength Checker
Calculates password entropy and categorizes strength (Weak, Moderate, Strong).

Password Generator
Generates random secure passwords using letters, digits, and special characters.

Data Breach Check
Uses the "Have I Been Pwned" API to check if a password has been exposed in data breaches.

Clipboard Auto-clear
Automatically copies the password to clipboard and clears it after 10 seconds for security.

Encrypted Password Vault
Securely saves generated passwords in an encrypted vault using cryptography.fernet.

Terminology

Entropy – A measure of unpredictability in the password. Higher entropy = stronger password.
Clipboard – Temporary system memory used to hold copied text (like a password).
Vault – Encrypted file that stores generated passwords securely.
Fernet – A symmetric encryption method used to encrypt/decrypt passwords in the vault.
HIBP API – "Have I Been Pwned" API, which checks if passwords are found in breached datasets.

Limitations

No GUI: Currently a CLI-based tool. Usability for non-tech users could be improved with a GUI.

Not a Full Password Manager: This is not a full-fledged password manager like Bitwarden or LastPass.

API Rate Limiting: Excessive breach checks may hit rate limits from the HIBP API.

No Username/Email Association: Passwords are saved without context like website or account info.

Requirements

Install all dependencies with:
nginx
Copy
Edit
pip install requests pyperclip cryptography
Python Version:

Python 3.7 or above recommended.

Required Libraries:

requests: for data breach API check

pyperclip: for clipboard access

cryptography: for vault encryption

Further Improvements

Develop a GUI using Tkinter or PyQt.

Add username/email fields and associate passwords with platforms.

Integrate cloud storage or sync (e.g., with Google Drive).

Add password import/export options in CSV or JSON format.

Include 2FA token generator or OTP-based verification.

Add password reuse detection within the vault.

Enable password vault search and update/delete functionality.

Ethical Considerations

This tool is designed only for personal and educational use.

Do not use this tool to test other users’ passwords or credentials without consent.

Never store or share passwords without proper encryption and permission.

Always follow cybersecurity best practices and respect privacy laws and regulations.
