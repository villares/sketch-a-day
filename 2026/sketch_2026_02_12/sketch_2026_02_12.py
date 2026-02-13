from py5_tools import animated_gif

def setup():
    size(400, 400)
    no_stroke() # desliga o traço de contorno
    animated_gif(
        'anima.gif',
        frame_numbers=range(1, 361, 10), # 1, 11, 21 ... 351
        duration=0.1667  
    )
    
def draw():
    background(200)
    ang = radians(frame_count)  # o número do quadro, como ângulo em radianos
    v = sin(ang)  # seno do número do quadro, se ele fosse um ângulo
    u = cos(ang)  # cosseno...
    da = 100 + 100 * v  # diâmetro do primeiro círculo (a)
    fill(128 + 128 * u, 255, 128 + 128 * v)  # cor R, G, B (o verde é fixo)
    circle(100, 200, da)
    db = 100 + 100 * u  # diâmetro do segundo círculo (b)
    fill(255, 128 + 128 * v, 128 + 128 * u)  # o vermelho é fixo no máximo
    circle(300, 200, db)
