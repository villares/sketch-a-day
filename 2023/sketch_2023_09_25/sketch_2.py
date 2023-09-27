from multiprocessing import shared_memory
from time import sleep
import py5

sleep(2)
smd_config = shared_memory.ShareableList(name='09-26')

def setup():
    py5.size(300, 300)
    py5.window_title('2')
    smd_config[-1] = True

def draw():
    if smd_config[-1]:
        py5.background(0, 0, 100)    
    py5.fill(100, 100, 0)
    x = smd_config[0]
    y = smd_config[1]
    py5.circle(x, y, 10)
    if py5.is_mouse_pressed:
        smd_config[2] = int(py5.mouse_x)
        smd_config[3] = int(py5.mouse_y)
            
def mouse_clicked():
    smd_config[-1] = not smd_config[-1]

def exiting():
    smd_config.shm.close()

py5.run_sketch()
smd_config.shm.unlink()

