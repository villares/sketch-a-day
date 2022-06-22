import py5


def setup():
    py5.size(600, 600)
    py5.no_cursor()
    py5.blend_mode(py5.SUBTRACT)

def draw():
    py5.background(200)
    cols, rows = 13, 11
    W = 30
    H = W * py5.sqrt(3) * 0.5  # W * sin(radians(60))
    px = 300 + py5.cos(py5.frame_count / 20) * py5.mouse_x
    py = 300 + py5.sin(py5.frame_count / 20) * py5.mouse_y
    for i in range(cols):
        for j in range(rows):
            x = i * W * 1.5 + W
            if i % 2 == 0:
                y = j * H * 2 + H
            else:
                y = j * H * 2 + H * 2
            d = (x - px) ** 2 + (y - py) ** 2
            py5.fill(0, 0, 255)
            py5.circle(x, y, 2 * H / (1 + d ** 0.5 / 200))
            d = (x - py5.width + px) ** 2 + (y - py) ** 2
            py5.fill(255, 0, 0)
            py5.circle(x, y, 2 * H / (1 + d ** 0.5 / 200))
            d = (x - px) ** 2 + (y - py5.height + py) ** 2
            py5.fill(0, 255, 0)
            py5.circle(x, y, 2 * H / (1 + d ** 0.5 / 200))


py5.run_sketch()
