import socket
import hashlib
import rsa
import os
from Crypto.Cipher import ARC4

# Load fingerprint of Alice's public key
fingerprint_file = "fingerprint.txt"
with open(fingerprint_file, "r") as f:
    fingerprint = f.read().strip()

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client is running...")

# Step 1: Ask for input from Bob
username = input("Enter username: ")
pw = input("Enter password: ")

# Send first message to Host
nb = os.urandom(16)
sock.sendto(f"{username},{nb.hex()}".encode(), ("localhost", 5555))

# Step 2: Receive public key and NA from Host
data, _ = sock.recvfrom(1024)
alice, pk_hex, na_hex = data.decode().split(",")
pk = rsa.PublicKey.load_pkcs1(pk_hex.encode())
na = bytes.fromhex(na_hex.strip())

# Verify public key
if hashlib.sha1(pk.save_pkcs1()).hexdigest() != fingerprint:
    print("Public key mismatch. Terminating connection.")
    sock.close()
    exit()

# Step 3: Generate random key K and encrypt password and key with public key
k = os.urandom(16)
encrypted_pw_k = rsa.encrypt(pw.encode() + k, pk)

# Send encrypted password and key to Host
sock.sendto(encrypted_pw_k, ("localhost", 5555))

# Step 4: Receive connection status from Host
data, _ = sock.recvfrom(1024)
if data.decode() == "Connection Okay":
    print("Connection established.")
else:
    print("Connection failed. Quitting.")
    sock.close()
    exit()

# Step 5: Establish shared secret key
ssk = hashlib.sha1(k + nb + na).digest()

# Secure communication phase
while True:
    message = input("Enter message: ")
    if message == "exit":
        break
    h = hashlib.sha1(ssk + message.encode()).digest()
    arc4 = ARC4.new(ssk)
    ciphertext = arc4.encrypt(message.encode() + h)
    sock.sendto(ciphertext, ("localhost", 5555))

    data, _ = sock.recvfrom(1024)
    arc4 = ARC4.new(ssk)
    decrypted_msg = arc4.decrypt(data)
    msg, h = decrypted_msg[:-20], decrypted_msg[-20:]
    h_prime = hashlib.sha1(ssk + msg).digest()

    if h == h_prime:
        print("Received message:", msg.decode())
    else:
        print("Decryption Error")

sock.close()