import socket
import pyaudio
import wave
import sys

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8000))
    s.listen(1)
    (c, addr) = s.accept()

    chunks = []
    while True:
        chunk = c.recv(4096).decode('ascii')
        if not chunk:
            break
        chunks.append(chunk)

    print(chunks[0])

    def callback(in_data, frame_count, time_info, status):
        print(in_data, frame_count, time_info, status)
        data = chunks
        return (data, pyaudio.paContinue)

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=44100,
                    output=True,
                    stream_callback=callback)

    stream.write(str(chunks))

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()

    s.close()

print("Goodbye!")
