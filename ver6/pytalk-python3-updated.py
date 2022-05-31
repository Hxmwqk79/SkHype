import pyaudio
import socket
import threading

try:

	is_server = input("Are you server? (y/n)")

	if is_server == "y":
		s = socket.socket()
		s.bind(('', 8000))
		s.listen(1)
		c = s.accept()[0]
	else:
		ip = input("IP: ")
		c = socket.socket()
		c.connect((ip, 8000))

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

	while True:
		data = stream2.read(CHUNK)
		c.send(data)

	# stop stream (4)
	stream1.stop_stream()
	stream1.close()

	stream2.stop_stream()
	stream2.close()
	# close PyAudio (5)
	p1.terminate()
	p2.terminate()
except:
	pass