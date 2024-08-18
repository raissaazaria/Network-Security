import rsa

# Generate a 2048-bit RSA key pair
public_key, private_key = rsa.newkeys(2048)

# Save the private key to a file
with open("key.pem", "wb") as key_file:
    key_file.write(private_key.save_pkcs1())

# Save the public key to a file (optional)
with open("public_key.pem", "wb") as pub_file:
    pub_file.write(public_key.save_pkcs1())
