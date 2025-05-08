# Advanced Password Checker

Purpose-
The Advanced Password Checker is a Python-based security tool that helps users evaluate the strength of their passwords, generate strong and secure ones, check for exposure in known data breaches, manage passwords with encryption, and promote better cybersecurity practices—making it an ideal project for students, ethical hackers, and developers to showcase on their resume or GitHub portfolio.

Features-
1. Password Strength Checker  
   Calculates password entropy and categorizes strength (Weak, Moderate, Strong).
2. Password Generator  
   Generates random secure passwords using letters, digits, and special characters.
3. Data Breach Check  
   Uses the "Have I Been Pwned" API to check if a password has been exposed in data breaches.
4. Clipboard Auto-clear  
   Automatically copies the password to clipboard and clears it after 10 seconds for security.
5. Encrypted Password Vault  
   Securely saves generated passwords in an encrypted vault using cryptography.fernet.

Terminology-
1. Entropy – A measure of unpredictability in the password. Higher entropy = stronger password.
2. Clipboard – Temporary system memory used to hold copied text (like a password).
3. Vault – Encrypted file that stores generated passwords securely.
4. Fernet – A symmetric encryption method used to encrypt/decrypt passwords in the vault.
5. HIBP API – "Have I Been Pwned" API, which checks if passwords are found in breached datasets.

Limitations-
1. No GUI: Currently a CLI-based tool. Usability for non-tech users could be improved with a GUI.
2. Not a Full Password Manager: This is not a full-fledged password manager like Bitwarden or LastPass.
3. API Rate Limiting: Excessive breach checks may hit rate limits from the HIBP API.
4. No Username/Email Association: Passwords are saved without context like website or account info.

Requirements-
Install all dependencies with:
1. nginx
2. Copy
3. Edit
4. pip install requests pyperclip cryptography
Python Version: Python 3.7 or above recommended.
Required Libraries:
1. requests: for data breach API check
2. pyperclip: for clipboard access
3. cryptography: for vault encryption

Further Improvements-
1. Develop a GUI using Tkinter or PyQt.
2. Add username/email fields and associate passwords with platforms.
3. Integrate cloud storage or sync (e.g., with Google Drive).
4. Add password import/export options in CSV or JSON format.
5. Include 2FA token generator or OTP-based verification.
6. Add password reuse detection within the vault.
7. Enable password vault search and update/delete functionality.

Ethical Considerations-
"This tool is designed strictly for personal and educational use. It must not be used to test or handle other users’ passwords or credentials without their explicit consent. Users should never store or share passwords unless they are properly encrypted and authorized to do so. Adhering to cybersecurity best practices and respecting all relevant privacy laws and regulations is essential when using this tool."
