# 🔐 Secure UDP Communication: Alice & Bob's 

This project demonstrates secure communication between two parties (Alice and Bob) using UDP sockets and cryptography in Python.

## How to Run

### 1. Install Python and Dependencies

Ensure that Python have been installed. Then, install the required packages 
```bash
pip install rsa pycryptodome
```

We use PyCryptodome for implementing the RC4 stream cipher (ARC4), which encrypts and decrypts messages securely during communication between Alice and Bob.


### 2. Generate RSA Keys

Run the following script to generate the necessary RSA keys


This will create:
- `key.pem` in Alice's directory.
- `fingerprint.txt` in Bob's directory.

### 3. Prepare Password File

In Alice's directory, create a `password.txt` file in this format


### 4. Run the Host (Alice)

Open a terminal, navigate to Alice's directory, and run
```bash
python Alice.py
```

### 5. Run the Client (Bob)

Open another terminal, navigate to Bob's directory, and run
```bash
python Bob.py
```

Enter the username and password when prompted.

### 6. Start Communicating

Once connected, you can exchange secure messages. Type `exit` to close the connection.


