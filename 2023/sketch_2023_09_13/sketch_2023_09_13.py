# from py5_tools import animated_gif

def setup():
    global pg, mascara, surface
    size(800, 400)
    pg = create_graphics(800, 400)
    mascara = create_graphics(800, 400)
    mascara.begin_draw()
    mascara.rect(70, 100, 200, 200, 30)
    mascara.rect(300, 100, 200, 200, 30)
    mascara.rect(530, 100, 200, 200, 30)
    mascara.end_draw()
    surface = get_surface()
#     animated_gif('out.gif', 60, 1/30, 1/30) 

def draw():
    background(0, 0, 100)
    pg.begin_draw()
    pg.background(0)
    n = 200 + 200 * sin(radians(frame_count * 2))  # -100 até 100
    pg.circle(200, 200, n)
    pg.circle(630, frame_count * 2 % height, 50)
    pg.end_draw()
    pg.mask(mascara)
    image(pg, 0, 0)
    surface.set_title(f"{get_frame_rate():.2f}")
    
#     if frame_count % 2 == 1:
#         save_frame('s###.png')
#     if frame_count >= 180:
#         exit_sketch()
