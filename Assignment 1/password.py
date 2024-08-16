import hashlib

username = "Bob"
pw = "password123"
hashed_pw = hashlib.sha1(pw.encode()).hexdigest()

with open("Alice/password.txt", "w") as f:
    f.write(f"{username}:{hashed_pw}\n")
