import socket

def encrypt(text):
    return ''.join(chr(ord(c) + 2) for c in text)

def decrypt(text):
    return ''.join(chr(ord(c) - 2) for c in text)

def server():
    s = socket.socket()
    s.bind(("127.0.0.1", 9999))
    s.listen(1)
    print("🔐 Server started... Waiting for client")
    conn, addr = s.accept()
    print("✅ Connected with", addr)

    while True:
        data = conn.recv(1024).decode()
        msg = decrypt(data)
        print("Client:", msg)

        reply = input("You: ")
        conn.send(encrypt(reply).encode())

def client():
    c = socket.socket()
    c.connect(("127.0.0.1", 9999))
    print("🔐 Connected to server")

    while True:
        msg = input("You: ")
        c.send(encrypt(msg).encode())

        data = c.recv(1024).decode()
        print("Server:", decrypt(data))

print("\nSecure Chat Application")
print("1. Server")
print("2. Client")

choice = input("Choose (1/2): ")

if choice == "1":
    server()
else:
    client()
