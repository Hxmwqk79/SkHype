import socket

name = input("Name: ")
address = ('1.158.134.10', 8000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
while True:
    message = input("Message: ")

    if message == ":quit":
        s.send(message.encode('ascii'))
        s.close()
        exit()

    message = (name + ": " + message).encode('ascii')
    s.send(message)

    data = s.recv(2048)
    if not data:
        continue
    else:
        if data.decode('ascii') == ":quit":
            print("Chat closed.")
            s.close()
            exit()
        else:
            print(data.decode('ascii'))
