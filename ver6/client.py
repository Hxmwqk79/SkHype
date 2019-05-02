import pyaudio
import time
import socket

s = socket.socket()
s.connect(('', 8000))

CHUNK = 1024 * 4
FOMRAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format=FOMRAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

while True:
    data = stream.read(CHUNK)
    s.send(data)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()
