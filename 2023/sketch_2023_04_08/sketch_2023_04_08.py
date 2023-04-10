import py5
import pyaudio
import numpy as np

"""Simple Blocking Stream PyAudio"""
CHUNK = 128  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at around 40 kHz
INTERVAL = 0.1  # Sampling Interval in Seconds

# If you are having trouble  making sense of the above, this might help:
# CHUNK: How many slices of sound
# RATE: How Fast these slices are captured
# INTERVAL: How much time to listen
# INIT PyAudio Instance
p = pyaudio.PyAudio()
# OPEN/Configure Stream:
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def setup():
    py5.size(400, 400)
    py5.no_fill()

def draw():
    py5.background(240)
    sample_size = int(INTERVAL*RATE/CHUNK)
    w = py5.width / sample_size
    for i in range(sample_size):  # STREAN INTERVAL
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        v = np.amax(data)
        py5.circle(i * w, py5.height / 2, v / 10)
        
def exiting():
    stream.stop_stream()
    stream.close()
    p.terminate()

py5.run_sketch()