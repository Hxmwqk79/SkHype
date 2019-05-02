import Tkinter
import pyaudio
import socket
import threading
import signal
is_server = ''
ip = ''
s = socket.socket()
c = socket.socket()
c2 = socket.socket()
setupWindow = Tkinter.Tk()
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
        except:
            error = Tkinter.Tk()
            error_label = Tkinter.Label(
                error, text="Couldn't connect, try again.")
            error_label.pack()
            error_button = Tkinter.Button(
                error, text="OK", command=error.destroy)
            error_button.pack()
            error.mainloop()
def server():
    global is_server
    is_server = 'y'
    server_button_text.set("Listening...")
    connect()
def client():
    global is_server
    global ip
    is_server = 'n'
    ip = ip_entry.get()
    connect()
ip_label = Tkinter.Label(setupWindow, text='Enter peer IP:')
ip_label.grid(row=0, column=0)
ip_entry = Tkinter.Entry(setupWindow)
ip_entry.grid(row=1, column=0)
server_button_text = Tkinter.StringVar()
server_button_text.set("Create Server")
server_button = Tkinter.Button(
    setupWindow, textvariable=server_button_text, command=server)
server_button.grid(row=0, column=1)
ip_button_text = Tkinter.StringVar()
ip_button_text.set("Connect")
ip_button = Tkinter.Button(
    setupWindow, textvariable=ip_button_text, command=client)
ip_button.grid(row=1, column=1)
setupWindow.mainloop()


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

RUNNING = True


class listenThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while RUNNING:
            try:
                data = c.recv(CHUNK)
                stream1.write(data)
            except:
                error = Tkinter.Tk()
                error_label = Tkinter.Label(
                    error, text="Lost connection")
                error_label.pack()
                error_button = Tkinter.Button(
                    error, text="OK", command=error.destroy)
                error_button.pack()
                error.mainloop()
                break


# Create new threads
listen = listenThread()
listen.daemon = True

# Start new Threads
listen.start()


class talkThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while RUNNING:
            try:
                data = stream2.read(CHUNK)
                c.send(data)
            except:
                error = Tkinter.Tk()
                error_label = Tkinter.Label(
                    error, text="Lost connection")
                error_label.pack()
                error_button = Tkinter.Button(
                    error, text="OK", command=error.destroy)
                error_button.pack()
                error.mainloop()
                break


# Create new threads
talk = talkThread()
talk.daemon = True

# Start new Threads
talk.start()


def quit():
    global RUNNING
    RUNNING = False
    c.close()
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


def msg():
    sendr = chat_entry.get()
    c2.send('~~~~~~~~~~~~111111111111' + str(sendr).encode('ascii'))
    #message1 = c2.recv(128).decode('ascii')
    #print message1
receive_text = True
def receive():
    while receive_text == True:
        message = c2.recv(128).decode('ascii')
        try:
            if message[:24] == '~~~~~~~~~~~~111111111111':
                chat_label_text.set(message[24:])
        except:
            pass
th = threading.Thread(target=receive)
th.daemon = True
th.start()
window = Tkinter.Tk()
chat_label_text = Tkinter.StringVar()
chat_label_text.set('msg')
chat_label = Tkinter.Label(window, textvariable=chat_label_text)
chat_label.grid(row=0, column=0, rowspan=4, columnspan=4)
chat_entry = Tkinter.Entry(window)
chat_entry.grid(row=4, column=0, columnspan=3)
chat_button = Tkinter.Button(window, text="Send", command=msg)
chat_button.grid(row=4, column=3, rowspan=1, columnspan=1)
call_button = Tkinter.Button(window, text="End Call", command=quit)
call_button.grid(row=5, column=0, columnspan=4)
window.mainloop()
receive_text = False
RUNNING = False
c.close()
c2.close()
s.close()