from shared_memory_dict import SharedMemoryDict

import py5

smd_config = SharedMemoryDict(name='config', size=1024)

def setup():
    py5.size(300, 300)
    py5.window_title('1')
    smd_config["status"] = True

def draw():
    if smd_config["status"]:
        py5.background(0, 100, 0)    
    py5.fill(0, 0, 100)
    x = smd_config.get('mouse_x2', 0)
    y = smd_config.get('mouse_y2', 0)
    py5.circle(x, y, 10)
    if py5.is_mouse_pressed:
        smd_config['mouse_x1'] = py5.mouse_x
        smd_config['mouse_y1'] = py5.mouse_y
            
def mouse_clicked():
    smd_config["status"] = not smd_config["status"]

def exiting():
    smd_config.shm.close()
    smd_config.shm.unlink()
    

py5.run_sketch(block=False)
# the other one will unlink