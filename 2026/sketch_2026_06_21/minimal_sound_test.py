# py5 module mode, learn more at <py5coding.org>
# check https://py5coding.org/how_tos/use_processing_libraries.html

## Run commented lines once to download Processing Sound library
# from py5_tools.processing import download_library
# print(download_libray('Sound'))

import py5

from processing.sound import SoundFile

def setup():
    global sounds
    py5.size(400, 400)
    this = py5.get_current_sketch()
    # loading 1.aif, 2.aif, etc. up to 5.aif 
    # from /data/ folder next  to the .py sketch 
    sounds = [
        SoundFile(this, f'{i}.aif') for i in range(1, 6)
    ]
    
def key_pressed():
    k = str(py5.key)
    if k in '12345':
        print(k)
        sounds[int(k) - 1].play()    

py5.run_sketch()

