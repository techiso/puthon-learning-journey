import hashlib

print("🔐 Secure Login System (File Version)")
print("--------------------------------------")

# Menü
print("\n1 - Register")
print("2 - Login")

choice = input("Choose an option: ")

# REGISTER
if choice == "1":
    username = input("Create username: ")
    password = input("Create password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open("users.txt", "a") as file:
        file.write(username + ":" + hashed_password + "\n")

    print("\n✅ User registered successfully!")

# LOGIN
elif choice == "2":
    username = input("Enter username: ")
    password = input("Enter password: ")

    login_hash = hashlib.sha256(password.encode()).hexdigest()

    found = False

    with open("users.txt", "r") as file:
        for line in file:
            saved_user, saved_hash = line.strip().split(":")

            if saved_user == username and saved_hash == login_hash:
                found = True
                break

    if found:
        print("\n✅ Login Successful!")
    else:
        print("\n❌ Wrong username or password!")

else:
    print("\n❌ Invalid choice!")
