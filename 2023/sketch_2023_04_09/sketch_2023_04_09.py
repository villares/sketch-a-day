import py5
import pyaudio
import numpy as np

"""Simple Blocking Stream PyAudio"""
CHUNK = 128  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at around 40 kHz
INTERVAL = 0.10  # Sampling Interval in Seconds

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
sample_size = int(INTERVAL*RATE/CHUNK)
data = []

def setup():
    global sw
    py5.size(600, 600)
    py5.no_fill()
    py5.color_mode(py5.HSB)
    sw = py5.width / sample_size
    py5.launch_repeating_thread(listen, 'listen')

def draw():
    py5.background(240)
    for i, v in enumerate(data):
        py5.stroke((64 + v / 4) % 255, 200, 200)
        py5.circle(i * sw, py5.height / 2, 64 + v / 4)

def listen():
    new_data = []
    for i in range(sample_size):  # STREAM INTERVAL
        sound_data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        new_data.append(np.amax(sound_data))
    data[:] = new_data
    
def exiting():
    stream.stop_stream()
    stream.close()
    p.terminate()

py5.run_sketch()