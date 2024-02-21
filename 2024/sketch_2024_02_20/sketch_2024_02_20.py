
D = 0.5

gestures = [[]]


def setup():
    size(600, 600)
    no_fill()
    
def draw():
    background(200)
    
    for gesture in gestures:
        for i, (x, y) in enumerate(gesture):
            circle(x, y, 1 + D * (i - frame_count) % 20)
            
def mouse_dragged():
    gestures[-1].append((mouse_x, mouse_y))
    
def mouse_released():
    gestures.append([])