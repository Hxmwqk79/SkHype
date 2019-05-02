#!/usr/bin/python
import Tkinter
import pyaudio
import socket
import threading
import signal

is_server = ''
ip = ''
sa = socket.socket()
ca = socket.socket()
st = socket.socket()
ct = socket.socket()
setupWindow = Tkinter.Tk()


def connect_audio():
    global sa
    global ca
    if is_server == "y":
        sa.bind(('', 8000))
        sa.listen(1)
        ca = sa.accept()[0]
        setupWindow.destroy()
    else:
        try:
            ca = socket.socket()
            ca.connect((ip, 8000))
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


def connect_text():
    global st
    global ct
    if is_server == "y":
        st.bind(('', 9000))
        st.listen(1)
        ct = st.accept()[0]
    else:
        try:
            ct = socket.socket()
            ct.connect((ip, 9000))
        except:
            pass


def server():
    global is_server
    is_server = 'y'
    server_button_text.set("Listening...")
    audioth = threading.Thread(target=connect_audio)
    audioth.daemon = True
    audioth.start()
    textth = threading.Thread(target=connect_text)
    textth.daemon = True
    textth.start()


def client():
    global is_server
    global ip
    is_server = 'n'
    ip = ip_entry.get()
    ip_button_text.set("Connecting...")
    audioth = threading.Thread(target=connect_audio)
    audioth.daemon = True
    audioth.start()
    textth = threading.Thread(target=connect_text)
    textth.daemon = True
    textth.start()


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


class listenAudioThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while RUNNING:
            try:
                data = ca.recv(CHUNK)
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
listenAudio = listenAudioThread()
listenAudio.daemon = True

# Start new Threads
listenAudio.start()


class listenTextThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while RUNNING:
            try:
                data = ct.recv(CHUNK)
                message = data.decode('ascii')
                print("----------------------"+message)
            except:
                break
            if len(message) > 0:
                if chat_label_text.get() == "":
                    chat_label_text.set(message)
                else:
                    chat_label_text.set(chat_label_text.get() + "\n" + message)


# Create new threads
listenText = listenTextThread()
listenText.daemon = True

# Start new Threads
listenText.start()
print("Started listen text thread")


class talkThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while RUNNING:
            try:
                data = stream2.read(CHUNK)
                ca.send(data)
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
    ca.close()
    sa.close()
    ct.close()
    st.close()
    # stop stream (4)
    stream1.stop_stream()
    stream1.close()

    stream2.stop_stream()
    stream2.close()
    # close PyAudio (5)
    p1.terminate()
    p2.terminate()
    exit(0)


def send_message():
    message = chat_entry.get()
    ct.send(message.encode('ascii'))
    chat_entry.delete(0, len(message))


def send():
    th = threading.Thread(target=send_message)
    th.daemon = True
    th.start()


window = Tkinter.Tk()
chat_label_text = Tkinter.StringVar()
chat_label = Tkinter.Label(window, textvariable=chat_label_text)
chat_label.grid(row=0, column=0, rowspan=4, columnspan=4)
chat_entry = Tkinter.Entry(window)
chat_entry.grid(row=4, column=0, columnspan=3)
chat_button = Tkinter.Button(window, text="Send", command=send)
chat_button.grid(row=4, column=3, rowspan=1, columnspan=1)
call_button = Tkinter.Button(window, text="End Call", command=quit)
call_button.grid(row=5, column=0, columnspan=4)
window.mainloop()
