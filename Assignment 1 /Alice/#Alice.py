#Alice
import socket
import hashlib
import rsa
import os

#Load password file
password_file = "password.txt"
passwords = {}
with open(password_file, "r") as f:
    for line in f:
        username, hashed_pw = line.strip().split(":")
        passwords[username] = hashed_pw

#Load public and private key pair
key_file ="key.pem"
with open(key_file, "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
public_key = private_key.public_key()

#create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", 5555))

print("Host is running and listening on port 5555...")

while True:
    #recieve message from bob
    data, addr = sock.recv(1024)
    username, nb =data.encode().split(",")
    username = username.strip()
    nb = bytes.fromhex(nb.strip())

    #sending public key and NA to client
    na = os.urandom(16)
    response = f"Alice,{public_key.save_pkcs1().decode()},{na.hex()}"
    sock.sendto(response.encode(), addr)

    #recieve encrypted password and key from client
    data, _ = sock.recvfrom(1024)
    encrypted_pw_k = datta

    #Decrypt password and key 
    decrypted_pw_k = rsa.decrpyt(encrypted_pw_k, private_key)
    pw,k = decrypted_pw_k[:8].decode(), decrypted_pw_k[8:]

    #verify password
    hashed_pw = hashlib.sha1(pw.encode()).hexdigest()
    if hashed_pw == passwords.get(username):
        print("Connection Okay")
        sock.sendto("Connection Okay".encode, addr)
    else:
        print("Connection Failed")
        sock.sendto("Connection Failed".encode(), addr)
        continue

    #establish shared secret key
    ssk = hashlib.sha1(k + nb + na).digest()

    #secure communication phase
    while True:
        data, _ = sock.recvfrom(1024)
        arc4 = ARC4.new(ssk)
        decrypted_msg = arc4.decrypt(data)
        msg, h = decrypted_msg[:-20], decrypted_msg[-20:]
        h_prime = hashlib.sha1(ssk + msg).digest()
        
        if h == h_prime:
            if msg.decode() == "exit":
                print("Connection Closed.")
                break
            print("Recieved message:", msg.decode())
        else:
            print("Decryption Error")