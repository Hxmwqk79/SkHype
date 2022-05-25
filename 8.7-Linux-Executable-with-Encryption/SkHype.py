import tkinter
import pyaudio
import socket
import threading
import signal
from os import urandom
from Crypto.Cipher import AES
import sys
try:
	is_server = ''
	ip = ''
	s = socket.socket()
	c = socket.socket()
	c2 = socket.socket()
	setupWindow = tkinter.Tk()
	def connect():
		global s
		global c
		global c2
		if is_server == "y":
			s.bind(('', 8000))
			s.listen(1)
			c = s.accept()[0]
			c2 = s.accept()[0]
			setupWindow.destroy()
		else:
			try:
				c = socket.socket()
				c2 = socket.socket()            
				c.connect((ip, 8000))
				c2.connect((ip, 8000))
				setupWindow.destroy()
				s.close()
				read_file = open("Contacts.txt", "r")
				readV = read_file.read()
				read_file.close()
				write_file = open("Contacts.txt", "w")
				write_file.write(readV + ip + "\n")
				write_file.close()
			except:
				error = tkinter.Tk()
				error_label = tkinter.Label(
					error, text="Couldn't connect, try again.")
				error_label.pack()
				error_button = tkinter.Button(
					error, text="OK", command=error.destroy)
				error_button.pack()
				error.mainloop()
	def server():
		global is_server
		is_server = 'y'
		server_button_text.set("Listening...")
		th1 = threading.Thread(target=connect)
		th1.daemon = True
		th1.start()
	def client():
		global is_server
		global ip
		is_server = 'n'
		ip = ip_entry.get()
		th2 = threading.Thread(target=connect)
		th2.daemon = True
		th2.start()
	ip_label = tkinter.Label(setupWindow, text='Enter peer IP:')
	ip_label.grid(row=0, column=0)
	ip_entry_text = tkinter.StringVar()
	with open('Contacts.txt', 'r') as f:
		lines = f.read().splitlines()
		last_line = lines[-1]
		ip_entry_text.set(last_line)
	ip_entry = tkinter.Entry(setupWindow, textvariable=ip_entry_text)
	ip_entry.grid(row=1, column=0)
	server_button_text = tkinter.StringVar()
	server_button_text.set("Create Server")
	server_button = tkinter.Button(
		setupWindow, textvariable=server_button_text, command=server)
	server_button.grid(row=0, column=1)
	ip_button_text = tkinter.StringVar()
	ip_button_text.set("Connect")
	ip_button = tkinter.Button(
		setupWindow, textvariable=ip_button_text, command=client)
	ip_button.grid(row=1, column=1)
	setupWindow.mainloop()

	# For Generating cipher text
	#sc = urandom(16)
	#ifive = urandom(16)
	sc = b'\xf7j\xfe\x05J\x1c\x0fr\xa3\xc8\xa8=\xd1\x93\xaf\xc0w\x0e\xba\xeb\xdd\xf9\x10\xa7\xc9Y\x01\xca\x9e%^\xd0'
	ifive = b'\x0f\xa3+\xb5\xe2\xed\xe4Q\x8d\x80m\x9d\xa3\xb3\xa6i'
	obj = AES.new(sc, AES.MODE_CTR, counter=lambda: ifive)
	def encrypt(plaintext):
		global sc
		global ifive
		obj = AES.new(sc, AES.MODE_CTR, counter=lambda: ifive)
		def __pad(self, plain_text):
			number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
			ascii_string = chr(number_of_bytes_to_pad)
			padding_str = number_of_bytes_to_pad * ascii_string
			padded_plain_text = plain_text + padding_str.encode()
			return padded_plain_text
		#padded_message = __pad(AES, plaintext)
		encrypted_text = obj.encrypt(plaintext)
		return encrypted_text
	def decrypt(scrambled):
		global sc
		global ifive
		def __unpad(plain_text):
			last_character = plain_text[len(plain_text) - 1:]
			return plain_text[:-ord(last_character)]
		rev_obj = AES.new(sc, AES.MODE_CTR, counter=lambda: ifive)
		decrypted_text = rev_obj.decrypt(scrambled)
		#unpad_decrypt = __unpad(decrypted_text)
		return decrypted_text

	CHUNK = 3024 * 4
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

	RUNNING = True

	def run_listen():
		while RUNNING:
			try:
				data = c.recv(CHUNK)
				decrypt_data = decrypt(data)
				stream1.write(decrypt_data)
			except:
				error = tkinter.Tk()
				error_label = tkinter.Label(
					error, text="Couldn't receive")
				error_label.pack()
				error_button = tkinter.Button(
					error, text="OK", command=error.destroy)
				error_button.pack()
				error.mainloop()
				break
	listen = threading.Thread(target=run_listen)
	listen.daemon = True
	listen.start()

	def run_talk():
		while RUNNING:
			try:
				data = stream2.read(CHUNK)
				encrypted_data = encrypt(data)
				c.send(encrypted_data)
			except:
				error = tkinter.Tk()
				error_label = tkinter.Label(
					error, text="Couldn't send" + str(sys.exc_info()[0]))
				error_label.pack()
				error_button = tkinter.Button(
					error, text="OK", command=error.destroy)
				error_button.pack()
				error.mainloop()
				break
	talk = threading.Thread(target=run_talk)
	talk.daemon = True
	talk.start()

	def quit():
		global RUNNING
		RUNNING = False
		c.close()
		s.close()
		c2.close()
		# stop stream (4)
		stream1.stop_stream()
		stream1.close()

		stream2.stop_stream()
		stream2.close()
		# close PyAudio (5)
		p1.terminate()
		p2.terminate()
		exit(0)


	def msg():	
		sendr = chat_entry.get()
		encrypted_text = encrypt(sendr)
		c2.send(encrypted_text)
		chat_label.insert(tkinter.END, '\n<me> ' + sendr)
		#message1 = c2.recv(128).decode('ascii')
		#print message1
	receive_text = True
	def receive():
		while receive_text == True:
			message = c2.recv(128)
			try:
				#chat_label.insert(tkinter.END, '\n' + str(message))
				unpad_decrypt = decrypt(message).decode('utf-8')
				#print(message)
				chat_label.insert(tkinter.END, '\n' + unpad_decrypt)
				#chat_label.insert(tkinter.END, '\n' + message[24:])
				#chat_label_text.set(message[24:])
			except:
				chat_label.insert(tkinter.END, '\n' + 'error')
				pass
	th = threading.Thread(target=receive)
	th.daemon = True
	th.start()
	window = tkinter.Tk()
	chat_label = tkinter.Text(window)
	chat_label.grid(row=0, column=0, rowspan=4, columnspan=2)
	chat_entry = tkinter.Entry(window, width=60)
	chat_entry.grid(row=4, column=0)
	chat_button = tkinter.Button(window, text="Send", command=msg)
	chat_button.grid(row=4, column=1)
	call_button = tkinter.Button(window, text="End Call", command=quit)
	call_button.grid(row=5, column=0)
	window.mainloop()
	receive_text = False
	RUNNING = False
	c.close()
	c2.close()
	s.close()
    # stop stream (4)
	stream1.stop_stream()
	stream1.close()
    
	stream2.stop_stream()
	stream2.close()
	# close PyAudio (5)
	p1.terminate()
	p2.terminate()
	exit(0)

except:
	pass
	
