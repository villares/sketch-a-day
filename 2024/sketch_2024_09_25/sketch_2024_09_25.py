from py5_tools import animated_gif

FPS = 30
back_easing = True
cor_b = color(255, 0, 255)
cor_a = color(0, 255, 255)

def setup():
    size(500, 500)
    frame_rate(FPS)
    no_stroke()
    animated_gif('out.gif',
                frame_numbers=range(1, 256, 2), # inicio, parada, passo
                duration=2 * 1/FPS)   
def draw():
    background(cor_a)
    f = frame_count % 256
    t = f / 255 # f:0 -> t:0  f:255 -> t:1
    a = TWO_PI * t  # em radianos t:0 -> a:0  t:1 -> a: 360 graus
    cor_c = lerp_color(cor_b, cor_a, t)
    fill(cor_c)
    circle(200, 200, f * 5)
    e = back_ease_in_out if back_easing else cubic_ease_in_out
    for i, y in enumerate(range(50, height, 50)):
        ty = (t + i / 9) % 1
        if ty < 0.5:
            x = lerp(50, width - 50, e(ty * 2))
            fill(lerp_color('red', 'yellow', 1 + sin(a + i/10)))
            circle(x, y, 50)
        else:
            x = lerp(width - 50, 50, e((ty * 2)-1))
            fill(lerp_color('red', 'yellow', 1 + sin(a + i/10)))
            circle(x, y, 50)
    #print(f)
    window_title(f'{get_frame_rate():.1f}')


def key_pressed():
    global back_easing
    back_easing = not back_easing

def cubic_ease_in_out(p):
    if p < 0.5:
        return 4 * p ** 3
    else:
        f = ((2 * p) - 2)
        return 0.5 * f ** 3 + 1
    

def back_ease_in_out(p):
    c1 = 1.70158
    c2 = c1 * 1.8 #1.525
    p2 = p * 2
    if p < 0.5:
        return (p2 ** 2 * ((c2 + 1) * p2 - c2)) / 2
    else:
        return ((p2 - 2) ** 2 * ((c2 + 1) * (p2 - 2) + c2) + 2) / 2