*# Python Learning Journey 🚀

This repository contains my Python projects as I learn programming and cybersecurity.

---

## ✅ Project 1: Mini Quiz Game 🎮

A beginner-friendly quiz game built with Python.

### Features:
- Multiple questions
- Score system
- Simple user interaction

### Run the project:

```bash
python quiz_game.py
---

## ✅ Project 2: Password Strength Checker 🔐

A simple cybersecurity tool that checks password strength.

### Checks:
- Length (8+ characters)
- Uppercase letters
- Numbers
- Special characters

Run it with:

```bash
python password_checker.py
import re

print("🔐 Password Strength Checker")

password = input("Enter your password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1

# Uppercase check
if any(char.isupper() for char in password):
    strength += 1

# Number check
if any(char.isdigit() for char in password):
    strength += 1

# Special character check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1

# Result
print("\nResult:")

if strength == 4:
    print("✅ Strong Password 💪")
elif strength == 3:
    print("🟡 Good Password 🙂")
elif strength == 2:
    print("🟠 Weak Password 😕")
else:
    print("🔴 Very Weak Password ❌")
