import threading
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8000))
s.listen(1)
(c, addr) = s.accept()
# c.send(b'hi')
# data = c.recv(1024)
# print(data.decode('ascii'))


class listenThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            print(c.recv(2048).decode('ascii') + "\n")


class talkThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            message = input()
            c.send(("\n"+message).encode('ascii'))


# Create new threads
listen = listenThread()
talk = talkThread()

# Start new Threads
listen.start()
talk.start()
