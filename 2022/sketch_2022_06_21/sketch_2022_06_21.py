import py5


def setup():
    py5.size(600, 600)
    py5.no_cursor()


def draw():
    py5.background(0, 0, 100)
    cols, rows = 13, 11
    W = 30
    H = W * py5.sqrt(3) * 0.5  # W * sin(radians(60))
    for i in range(cols):
        for j in range(rows):
            x = i * W * 1.5 + W
            if i % 2 == 0:
                y = j * H * 2 + H
            else:
                y = j * H * 2 + H * 2
            d = (x - py5.mouse_x) ** 2 + (y - py5.mouse_y) ** 2
            py5.circle(x, y, 2 * H / (1 + d ** 0.5 / 100))


py5.run_sketch()
