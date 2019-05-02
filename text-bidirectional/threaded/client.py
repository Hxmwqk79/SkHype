import threading
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 8000))
# data = s.recv(1024)
# print(data.decode('ascii'))
# s.send(b'bye')


class listenThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            print(s.recv(2048).decode('ascii') + "\n")


class talkThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            message = input()
            s.send(("\n"+message).encode('ascii'))


# Create new threads
listen = listenThread()
talk = talkThread()

# Start new Threads
listen.start()
talk.start()
