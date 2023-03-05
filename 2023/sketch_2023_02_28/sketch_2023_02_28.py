import py5

N = 200
especies_n = 3
color_step = 256.0 / especies_n
leis = [[0] * especies_n for _ in range(especies_n)]
balls = []

def setup():
    global right, left, top, bottom
    py5.size(600, 400)  # displayWidth
    py5.no_smooth()

    right = py5.width + 10
    left = -10
    top = -10
    bottom = py5.height + 10
    py5.color_mode(py5.HSB)
    balls[:] = [Ball() for _ in range(N)]

    for j in range(especies_n):
        for i in range(especies_n):
            leis[i][j] = py5.random(-3, 3)
    print(leis)

def draw():
    py5.background(0)
    py5.no_stroke()
    for ball_i in balls:
        ball_i.tick()
        ball_i.display()
        for ball_j in balls:
            forca = ball_i.pos - ball_j.pos
            dsq = forca.mag_sq
            if ball_i is not ball_j and dsq < 10000:
                if(dsq < 10):
                    m = py5.remap(dsq, 10, 0, 0, 1)
                    if m < 0:
                        forca *= -1
                        m = -m
                    forca.mag = m
                else:
                    m = py5.remap(dsq, 10000, 0, 0, 0.001)
                    lm = leis[ball_i.especie][ball_j.especie] * m
                    if lm < 0:
                        forca *= -1
                        lm = -lm
                    forca.mag = lm
                ball_i.vel += forca
    py5.window_title(f'{py5.get_frame_rate():.1f}')


class Ball:

    def __init__(self):
        self.pos = py5.Py5Vector(py5.random(py5.width), py5.random(py5.height))
        self.vel = py5.Py5Vector(py5.random(-1, 1), py5.random(-1, 1))
        self.especie = int(py5.random(especies_n))

    def tick(self):
        self.pos += self.vel
        self.vel *= 0.999
        if self.pos.x > right:
            self.pos.x = left
        if self.pos.x < left:
            self.pos.x = right
        if self.pos.y > bottom:
            self.pos.y = top
        if self.pos.y < top:
            self.pos.y = bottom

    def display(self):
        py5.fill(self.especie * color_step, 255, 255)
        py5.ellipse(self.pos.x, self.pos.y, 6, 6)

py5.run_sketch()
