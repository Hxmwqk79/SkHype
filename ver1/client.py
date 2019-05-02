import socket
with socket.socket() as s:
    s.connect(('1.158.140.141', 8000))
    with open('file', 'rb') as f:
        s.sendall(f.read())
