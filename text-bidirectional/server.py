import socket

name = input("Name:")


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


host = 'localhost'
port = get_open_port()
address = (host, 8000)
print(address)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)

server_socket.listen(1)
(s, addr) = server_socket.accept()
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
