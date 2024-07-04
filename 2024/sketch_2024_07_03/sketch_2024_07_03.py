import py5
import py5_tools
import numpy as np

movements = []

def setup():
    py5.size(600, 600)
    start()
    py5_tools.animated_gif('out.gif', frame_numbers=range(0, 1200, 10), duration=0.15)

def start():
    global px, w, h
    w, h = py5.width, py5.height
    py5.background(0)
    vlwf = py5.create_font('Inconsolata Black', 100)
    py5.text_font(vlwf)
    py5.text_size(100)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_leading(80)
    py5.text('sketch-mail\nis back\nsubscribe\nlink in bio\nlinks page', 300, 300)
    px = py5.get_np_pixels(bands='RGB')
    for i in range(10):
        direction = py5.random_choice((-1, 1))
        channel = py5.random_choice((0, 1, 2))
        x = py5.random_int(w // 100 - 1) * 100
        y = py5.random_int(h // 100 - 1) * 100
        for _ in range(100):
            px[y-100:y, :, channel] = np.roll(px[y-100:y, :, channel], direction , axis=1)
            px[:, x-100:x, channel] = np.roll(px[:, x-100:x, channel], direction, axis=0)
        movements.append((x, y, direction, channel))
    py5.set_np_pixels(px, bands='RGB')
    movements[:] = ((x, y, -d, c) for x, y, d, c in reversed(movements))  # undo
    movements.extend([(0, 0, 0, 0)] * 2) # pause

    
def draw():
    f = (py5.frame_count - 1) // 100
    #print(py5.frame_count)
    x, y, direction, channel = movements[f % len(movements)]       
    px[y-100:y, :, channel] = np.roll(px[y-100:y, :, channel], direction , axis=1)
    px[:, x-100:x, channel] = np.roll(px[:, x-100:x, channel], direction, axis=0)
    py5.set_np_pixels(px, bands='RGB')

def key_pressed():
    py5.save_frame('###.png')
    start()

py5.run_sketch(block=False)
