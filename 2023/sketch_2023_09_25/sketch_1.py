from multiprocessing import shared_memory

import py5

# This does not let you set the name...
# smm = shared_memory.SharedMemoryManager()
# smm.start()
# sl = smm.ShareableList([0, 0, 0, 0, True])

smd_config = shared_memory.ShareableList([0, 0, 0, 0, True], name='09-26')

def setup():
    py5.size(300, 300)
    py5.window_title('1')
    smd_config[-1] = True

def draw():
    if smd_config[-1]:
        py5.background(100, 100, 0)    
    py5.fill(0, 0, 100)
    x = smd_config[2]
    y = smd_config[3]
    py5.circle(x, y, 10)
    if py5.is_mouse_pressed:
        smd_config[0] = int(py5.mouse_x)
        smd_config[1] = int(py5.mouse_y)
            
def mouse_clicked():
    smd_config[-1] = not smd_config[-1]

def exiting():
    smd_config.shm.close()
#     smd_config.shm.unlink()
    

py5.run_sketch()
# the other one will unlink