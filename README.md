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
---

## ✅ Project 3: Mini ATM System 💳

A simple Python ATM simulation.

### Features:
- Balance display
- Deposit money
- Withdraw money
- PIN verification

### Run it with:

```bash
python atm_system.py
---

## ✅ Project 4: To-Do List App 📝

A simple Python app to manage daily tasks.

### Features:
- Add new tasks
- View all tasks
- Remove tasks
- Exit system

### Run it with:

```bash
python todo_app.py
---

## ✅ Project 5: Website IP Finder 🌐

A simple cybersecurity networking tool that finds the IP address of a website.

### Run it with:

```bash
python ip_finder.py
# Project 6: Simple Port Scanner 🔍

import socket

print("🔍 Simple Port Scanner")
print("----------------------")

target = input("Enter an IP address (example: 127.0.0.1): ")

ports = [21, 22, 80, 443]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"✅ Port {port} is OPEN")
    else:
        print(f"❌ Port {port} is CLOSED")

    sock.close()

print("\nScan finished.")
# Project 7: Log Analyzer Tool 📄

print("📄 Log Analyzer Tool")
print("---------------------")

filename = input("Enter log file name (example: log.txt): ")

keywords = ["error", "failed", "attack", "warning"]

try:
    with open(filename, "r") as file:
        content = file.read().lower()

    print("\n--- Analysis Result ---")

    for word in keywords:
        count = content.count(word)
        print(f"'{word}' found: {count} times")

    print("\n✅ Log analysis finished.")

except FileNotFoundError:
    print("❌ File not found. Please check the file name.")
--

## ✅ Project 8: Password Generator 🔐

A tool that generates strong random passwords.

Run it with:

```bash
python password_generator.py
