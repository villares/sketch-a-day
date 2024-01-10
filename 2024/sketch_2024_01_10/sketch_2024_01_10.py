def setup():
    size(900, 900)
    color_mode(HSB)

def draw():
    background(0, 100, 0)
    f = (frame_count / 100) % 255
    ff = frame_count / 60
    r = 100 + 100 * sin(frame_count / 60)

    poly(700, 700, 200, r, [r, 255, 255] * 2, ff)
    poly(700, 700, r, 0, [r, r, 255] * 2, ff)


def poly(x, y, raio_a, raio_b, cores, offset):
    num_lados = len(cores)
    passo = TWO_PI / num_lados
    for i in range(num_lados):
        fill(cores[round(i + offset) % num_lados], 200, 200)
        ang = passo * i
        x0 = x + cos(ang) * raio_a
        y0 = y + sin(ang) * raio_a
        x1 = x + cos(ang + passo) * raio_a
        y1 = y + sin(ang + passo) * raio_a
        x2 = x + cos(ang + passo) * raio_b
        y2 = y + sin(ang + passo) * raio_b
        x3 = x + cos(ang) * raio_b
        y3 = y + sin(ang) * raio_b
        quad(x0, y0, x1, y1, x2, y2, x3, y3)
