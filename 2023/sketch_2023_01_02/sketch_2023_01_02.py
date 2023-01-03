# Genuary 2 - 10min
# using py5 (py5coding.org) with github.com/tabreturn/thonny-py5mode

def setup():
    size(600, 600)
    color_mode(HSB)
    no_stroke()
    rect_mode(CENTER)
    
def draw():
    background(0)
    m = frame_count #1 + mouse_x // 10
    for x in range(100):
        cx = 50 + x * 5
        for y in range(100):
            cy = 50 + y * 5
            c = (x ^ y) ** 13 % m
            fill(c * (255 / m), 255, 255)
#             print(c, cx, cy)
            square(cx, cy, 5)

    if frame_count % 10 == 0 and frame_count <= 100:
        save_frame('###.png')