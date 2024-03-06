# Exemplo usando py5 no "imported mode" requer Thonny+plugin ou ferramenta CLI run_sketch

from collections import deque

gesto = deque(maxlen=300)

def setup():
    size(800, 800)
    color_mode(HSB) # Hue, Sat, Brightness
    
def draw():
    background(0) # r, g, b
    for i, (x, y) in enumerate(gesto):
        d = 50 + 40 * sin((i + frame_count) / 20)
        no_fill()
        stroke((d + frame_count) % 255, 255, 255)
        circle(x, y, d)
        
def mouse_dragged():
    gesto.append((mouse_x, mouse_y))
