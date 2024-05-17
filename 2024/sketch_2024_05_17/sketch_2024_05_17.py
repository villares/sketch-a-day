# done during the PyCon US 2024 tutorial :)

def setup():
    size(500, 500)

def draw():
    v = sin(frame_count/10)  # -1 to 1
    fill(128 + 128 * v, 0, 128 - 128 * v)
    circle(mouse_x, mouse_y, 50 + 50 * v)