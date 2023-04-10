import sounddevice as sd
import numpy as np

device_info = sd.query_devices('default')
sample_rate = int(device_info['default_samplerate'])
block_size = 2048

stream = sd.InputStream(device=device_info['name'], channels=1,
                         blocksize=block_size, samplerate=sample_rate)

stream.start()

while True:
    block = stream.read(block_size)
    print(block)

stream.stop()
stream.close()