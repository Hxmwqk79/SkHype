import pyaudio
# create an audio object
pya = pyaudio.PyAudio()

# open stream based on the wave object which has been input.
stream = pya.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=1000,
    output=True)

# read data (based on the chunk size)
audata = "asdasdasdasdasdakjsflkjsdhflKJASDHFLAKJSDHFLKJASDHFLKJASDHFLAKJSDHFLAKJDHALsdj;OQA9IWRUEAsd"
stream.write(audata)

# cleanup stuff.
stream.close()
pya.terminate()
