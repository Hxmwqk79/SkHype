import pyaudio
import socket
import threading
import Tkinter

window = Tkinter.Tk()
label = Tkinter.Label(window, text="You are server wether you like it or not.")
label.pack()

s = socket.socket()
s.bind(('', 3333))
s.listen(1)
print "Waiting for connection..."
c = s.accept()[0]

CHUNK = 1024 * 4
FOMRAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p1 = pyaudio.PyAudio()

p2 = pyaudio.PyAudio()


stream1 = p1.open(
    format=FOMRAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

stream2 = p2.open(
    format=FOMRAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)


class listenThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = c.recv(CHUNK)
            stream1.write(data)


# Create new threads
listen = listenThread()

# Start new Threads
listen.start()


class serverThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = stream2.read(CHUNK)
            c.send(data)


# Create new threads
server = serverThread()

# Start new Threads
server.start()

window.mainloop()

# stop stream (4)
stream1.stop_stream()
stream1.close()

stream2.stop_stream()
stream2.close()
# close PyAudio (5)
p1.terminate()
p2.terminate()
