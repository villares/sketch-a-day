def setup():
    global pg, tam_quad
    size(800, 800)
    tam_quad = 175
    pg = create_graphics(tam_quad, tam_quad) # canvas dos quadros

def draw():
    background(255)  # branco entre os quadros
    f = frame_count  # avanço geral da animação
    step = TWO_PI / 16  # avanço da animação entre quadros
    i = 0  # índice do quadro (vai influenciar o desenho)
    for y in range(20, 800, 195):   
        for x in range(20, 800, 195):         
            s = cos(radians(f * 2) + i * step)  # valor senoidal
            d = 55 + 50 * s  # diâmetro dos circulos
            yc = remap(s, -1, 1, 0, tam_quad)
            pg.begin_draw()
            pg.background(100, 200, 0) # fundo do quadro
            pg.fill(0, 0, 200)  # preenchimento do círculo
            pg.circle(175 / 2, yc, d)  
            pg.end_draw()
            image(pg, x, y) # desenha o quadro
            i += 1  # avança em um o índice do quadro
#     # para salvar 90 frames de animação
#     if f <= 180 and f % 2:
#         save_frame('###.png')
#     elif f == 181:
#         exit_sketch()
