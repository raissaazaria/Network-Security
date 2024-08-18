#Save Alice's public key's fingerprint
import hashlib

with open("Alice/key.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
public_key = private_key.public_key()
public_key_fingerprint = hashlib.sha1(public_key.save_pkcs1()).hexdigest()

with open("Bob/fingerprint.txt", "w") as f:
    f.write(public_key_fingerprint)
