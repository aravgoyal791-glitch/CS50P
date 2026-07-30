"""
Tests for SecureVault (CS50P Final Project)
Run with: pytest test_project.py
"""

import pytest
from cryptography.fernet import Fernet

from project import (
    generate_password,
    check_password_strength,
    encrypt_password,
    decrypt_password,
    search_accounts,
)


def test_generate_password_length():
    pw = generate_password(length=20)
    assert len(pw) == 20

    pw_short = generate_password(length=4)
    assert len(pw_short) == 4


def test_generate_password_character_sets():
    pw = generate_password(length=50, use_upper=True, use_lower=False,
                            use_digits=False, use_special=False)
    assert pw.isupper()
    assert all(c.isalpha() for c in pw)

    pw_digits_only = generate_password(length=30, use_upper=False, use_lower=False,
                                        use_digits=True, use_special=False)
    assert pw_digits_only.isdigit()


def test_generate_password_invalid_input():
    with pytest.raises(ValueError):
        generate_password(length=2)  # too short

    with pytest.raises(ValueError):
        generate_password(length=10, use_upper=False, use_lower=False,
                           use_digits=False, use_special=False)  # no char sets


def test_check_password_strength_weak():
    rating, reasons = check_password_strength("abc")
    assert rating == "Weak"
    assert len(reasons) > 0


def test_check_password_strength_strong():
    rating, reasons = check_password_strength("Str0ng!Passw0rd123")
    assert rating == "Strong"


def test_check_password_strength_medium():
    rating, reasons = check_password_strength("password123")
    assert rating in ("Weak", "Medium")


def test_encrypt_decrypt_round_trip():
    key = Fernet.generate_key()
    original = "MySecretPassword123!"
    token = encrypt_password(original, key)
    assert token != original  # must not be stored in plaintext
    decrypted = decrypt_password(token, key)
    assert decrypted == original


def test_decrypt_with_wrong_key_fails():
    key1 = Fernet.generate_key()
    key2 = Fernet.generate_key()
    token = encrypt_password("hunter2", key1)
    with pytest.raises(ValueError):
        decrypt_password(token, key2)


def test_search_accounts():
    vault = {
        "github.com": {"username": "alice", "password": "xxx"},
        "gitlab.com": {"username": "bob", "password": "yyy"},
        "amazon.com": {"username": "alice_shop", "password": "zzz"},
    }
    assert set(search_accounts(vault, "git")) == {"github.com", "gitlab.com"}
    assert set(search_accounts(vault, "alice")) == {"github.com", "amazon.com"}
    assert search_accounts(vault, "nonexistent") == []