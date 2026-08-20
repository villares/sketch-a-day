
import numpy as np
import py5

N = 1000
WIDTH, HEIGHT = 600, 600
step = 0.2         
friction_factor = 1 - 0.001 

pos = np.random.uniform([0, 0], [WIDTH, HEIGHT], size=(N, 2)) #.astype(np.float32)
# vel = np.random.uniform(-5, 5, size=(N, 2)) #.astype(np.float32)
headings = np.random.uniform(0, 2*np.pi, size=N)
vel = np.column_stack([np.cos(headings), np.sin(headings)]) * np.random.uniform(-5, 5, size=N)[:, None]

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.stroke_weight(5)

def draw():
    global pos, vel
    #py5.background(240)
    py5.fill(200, py5.random(0, 16))
    py5.rect(0, 0, py5.width, py5.height)
    #v_mouse = np.array([py5.mouse_x, py5.mouse_y]) - pos  # vector towards mouse
    v_mouse = np.array([200, 200]) - pos
    squared_mouse_dist = np.sum(v_mouse * v_mouse, axis=1) + 1 # avoiding 0s and higher speeds
    acc = 10 * v_mouse / squared_mouse_dist[:, None]  
    vel = vel + acc * step
    vel *= friction_factor
    pos = pos + vel * step
    #pos %= (WIDTH, HEIGHT) # wrap edges
    py5.points(pos)  # draw

    py5.window_title(f'{py5.get_frame_rate():f}')

def key_pressed():
    if py5.key == 's':
        py5.save_frame('out.png')

py5.run_sketch()