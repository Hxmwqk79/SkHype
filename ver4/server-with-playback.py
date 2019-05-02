import socket
import pyaudio
import wave
import sys

keepListening = True

while keepListening:

    with socket.socket() as s:
        s.bind(('',8000))
        s.listen(1)
        with s.accept()[0] as c:
            chunks = []
            while True:
                chunk = c.recv(4096)
                if not chunk: break
                chunks.append(chunk)
        with open('server.wav','wb') as f:
            f.write(b''.join(chunks))

    answer = input("Message recieved: play message? (y/n)")
    if answer == "n":
        keepListening = False

    CHUNK = 1024

    # if len(sys.argv) < 2:
    #     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    #     sys.exit(-1)

    #wf = wave.open(sys.argv[1], 'rb')
    wf = wave.open('server.wav', 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()

print("Goodbye!")
