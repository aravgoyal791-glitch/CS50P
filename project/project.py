"""
SecureVault - A command-line password manager
CS50P Final Project

Stores website credentials in an encrypted, local JSON vault.
Passwords are never written to disk in plain text: each password is
encrypted with a Fernet key (symmetric AES-based encryption) that is
generated once and stored in a separate local key file.
"""

import json
import os
import random
import string
import sys
from getpass import getpass

from cryptography.fernet import Fernet, InvalidToken

VAULT_FILE = "vault.json"
KEY_FILE = "vault.key"


def main():
    key = get_or_create_key(KEY_FILE)
    vault = load_vault(VAULT_FILE)

    while True:
        print_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            website = input("Website: ").strip()
            username = input("Username or email: ").strip()
            password = getpass("Password (input hidden): ").strip()
            if not website or not username or not password:
                print("All fields are required.\n")
                continue
            add_password(vault, website, username, password, key)
            save_vault(vault, VAULT_FILE)
            print(f"Saved credentials for '{website}'.\n")

        elif choice == "2":
            view_passwords(vault, key)

        elif choice == "3":
            query = input("Search by website or username: ").strip()
            matches = search_accounts(vault, query)
            if not matches:
                print("No matching accounts found.\n")
            else:
                for website in matches:
                    print(f"- {website} (username: {vault[website]['username']})")
                print()

        elif choice == "4":
            website = input("Website to update: ").strip()
            if website not in vault:
                print(f"No account found for '{website}'.\n")
                continue
            new_username = input(
                f"New username (leave blank to keep '{vault[website]['username']}'): "
            ).strip()
            new_password = getpass(
                "New password (leave blank to keep current, input hidden): "
            ).strip()
            update_account(
                vault,
                website,
                key,
                new_username=new_username or None,
                new_password=new_password or None,
            )
            save_vault(vault, VAULT_FILE)
            print(f"Updated '{website}'.\n")

        elif choice == "5":
            website = input("Website to delete: ").strip()
            if website not in vault:
                print(f"No account found for '{website}'.\n")
                continue
            confirm = input(f"Type 'yes' to confirm deleting '{website}': ").strip().lower()
            if confirm == "yes":
                delete_account(vault, website)
                save_vault(vault, VAULT_FILE)
                print(f"Deleted '{website}'.\n")
            else:
                print("Cancelled.\n")

        elif choice == "6":
            length_input = input("Password length (default 16): ").strip()
            length = int(length_input) if length_input.isdigit() else 16
            use_upper = confirm_yes("Include uppercase letters? (Y/n): ")
            use_lower = confirm_yes("Include lowercase letters? (Y/n): ")
            use_digits = confirm_yes("Include numbers? (Y/n): ")
            use_special = confirm_yes("Include special characters? (Y/n): ")
            try:
                generated = generate_password(
                    length, use_upper, use_lower, use_digits, use_special
                )
                print(f"Generated password: {generated}\n")
            except ValueError as e:
                print(f"Error: {e}\n")

        elif choice == "7":
            password = getpass("Enter password to check (input hidden): ")
            rating, reasons = check_password_strength(password)
            print(f"Strength: {rating}")
            for reason in reasons:
                print(f"  - {reason}")
            print()

        elif choice == "8":
            print("Goodbye.")
            sys.exit(0)

        else:
            print("Invalid choice. Please select 1-8.\n")


def print_menu():
    print("=" * 40)
    print("SecureVault - Password Manager")
    print("=" * 40)
    print("1. Add Password")
    print("2. View Saved Passwords")
    print("3. Search Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Generate Strong Password")
    print("7. Password Strength Checker")
    print("8. Exit")


def confirm_yes(prompt):
    """Ask a yes/no question. Defaults to yes on blank input."""
    answer = input(prompt).strip().lower()
    return answer in ("", "y", "yes")


def get_or_create_key(key_path):
    """Load the Fernet encryption key from disk, creating it if needed."""
    if os.path.exists(key_path):
        with open(key_path, "rb") as f:
            return f.read()
    key = Fernet.generate_key()
    with open(key_path, "wb") as f:
        f.write(key)
    return key


def load_vault(vault_path):
    """Load the vault JSON file into a dict. Returns empty dict if missing."""
    if not os.path.exists(vault_path):
        return {}
    with open(vault_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_vault(vault, vault_path):
    """Write the vault dict to disk as JSON."""
    with open(vault_path, "w") as f:
        json.dump(vault, f, indent=2)


def encrypt_password(password, key):
    """Encrypt a plaintext password, returning a string token."""
    f = Fernet(key)
    token = f.encrypt(password.encode())
    return token.decode()


def decrypt_password(token, key):
    """Decrypt a stored token back into the plaintext password."""
    f = Fernet(key)
    try:
        return f.decrypt(token.encode()).decode()
    except InvalidToken:
        raise ValueError("Could not decrypt password: invalid key or corrupted data.")


def add_password(vault, website, username, password, key):
    """Add a new encrypted account entry to the vault dict."""
    vault[website] = {
        "username": username,
        "password": encrypt_password(password, key),
    }
    return vault


def view_passwords(vault, key):
    """Print all saved accounts; reveal passwords only after confirmation."""
    if not vault:
        print("No saved accounts yet.\n")
        return
    for website, data in vault.items():
        print(f"- {website} (username: {data['username']})")
    print()
    reveal = confirm_yes("Reveal passwords? (y/N): ")
    if reveal:
        for website, data in vault.items():
            try:
                plain = decrypt_password(data["password"], key)
            except ValueError as e:
                plain = f"[{e}]"
            print(f"- {website}: {plain}")
    print()


def search_accounts(vault, query):
    """Return website keys whose website name or username matches query."""
    query = query.lower()
    return [
        website
        for website, data in vault.items()
        if query in website.lower() or query in data["username"].lower()
    ]


def update_account(vault, website, key, new_username=None, new_password=None):
    """Update the username and/or password for an existing account."""
    if website not in vault:
        raise KeyError(f"No account found for '{website}'.")
    if new_username:
        vault[website]["username"] = new_username
    if new_password:
        vault[website]["password"] = encrypt_password(new_password, key)
    return vault


def delete_account(vault, website):
    """Remove an account entry from the vault dict."""
    if website not in vault:
        raise KeyError(f"No account found for '{website}'.")
    del vault[website]
    return vault


def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a random password from the requested character sets."""
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    pools = []
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_special:
        pools.append("!@#$%^&*()-_=+[]{}?")

    if not pools:
        raise ValueError("At least one character type must be selected.")

    # Guarantee at least one character from each selected pool
    password_chars = [random.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    password_chars += [random.choice(all_chars) for _ in range(length - len(pools))]
    random.shuffle(password_chars)
    return "".join(password_chars)


def check_password_strength(password):
    """
    Rate a password as Weak, Medium, or Strong and explain why.
    Returns a tuple of (rating, list_of_reasons).
    """
    reasons = []
    score = 0

    if len(password) >= 12:
        score += 2
        reasons.append("Good length (12+ characters).")
    elif len(password) >= 8:
        score += 1
        reasons.append("Acceptable length (8-11 characters), but 12+ is stronger.")
    else:
        reasons.append("Too short: use at least 8 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        reasons.append("Add uppercase letters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        reasons.append("Add lowercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        reasons.append("Add numbers.")

    if any(c in "!@#$%^&*()-_=+[]{}?" for c in password):
        score += 1
    else:
        reasons.append("Add special characters (e.g. !@#$%).")

    if score >= 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, reasons


if __name__ == "__main__":
    main()