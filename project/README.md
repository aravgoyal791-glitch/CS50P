# SecureVault

#### Video Demo: <https://youtu.be/KPKhoram6Sg?feature=shared>

#### Description

SecureVault is a command-line password manager written in Python for my
CS50P final project. It lets a user store, view, search, update, and
delete login credentials for different websites, generate strong random
passwords, and check how strong an existing password is — all from a
simple numbered menu.

The most important design decision in this project was around how
passwords are stored. A "password manager" that stores passwords in
plain-text JSON isn't really solving the problem it claims to solve, so
SecureVault encrypts every password with the `cryptography` library's
`Fernet` scheme (symmetric AES-128 encryption in CBC mode, authenticated
with HMAC) before it ever touches disk. The encryption key is generated
once on first run and saved to a separate file, `vault.key`, which is
excluded from version control via `.gitignore` — in a real deployment
this key would be protected by a master password, but that's listed as
a future improvement rather than something I wanted to fake for this
submission.

`project.py` contains `main()`, which drives the menu loop and handles
all user input/output, plus the required three-or-more additional
top-level functions. I split the logic so that every function that does
real work (`generate_password`, `check_password_strength`,
`encrypt_password`/`decrypt_password`, `search_accounts`,
`add_password`, `update_account`, `delete_account`) is separate from
input/output handling in `main()`. That split is what makes the project
testable: `test_project.py` calls these functions directly with known
inputs and checks their return values, rather than trying to test
`main()` itself, which just orchestrates `input()`/`print()` calls.

`load_vault`/`save_vault` handle reading and writing `vault.json`, which
stores, per website, a username and an encrypted password token.
Passwords are only decrypted and shown in the "View Saved Passwords"
screen after an explicit confirmation prompt, so a glance at the terminal
doesn't leak them.

## Files

- `project.py` — main program: menu, all core functions
- `test_project.py` — pytest test suite for the testable functions
- `requirements.txt` — `cryptography` and `pytest`
- `.gitignore` — keeps `vault.json` and `vault.key` out of version control

## How to run

```
pip install -r requirements.txt
python project.py
```

Run the tests with:

```
pytest test_project.py
```

## Future improvements

- Master password required to unlock the vault (currently the key file
  alone grants access)
- SQLite instead of JSON for larger vaults
- GUI version
- Cloud sync across devices
-