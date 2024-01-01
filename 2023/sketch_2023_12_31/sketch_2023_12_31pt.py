estado = 0
mascara = 11000

def setup():
    global mask, years, tf
    size(800, 800)
    color_mode(HSB)
    tf = create_font('GaroaHackerClube-Bold', 200)
    text_font(tf)
    mask = create_graphics(800, 800)
    years = create_graphics(800, 800)
    
def draw():
    global estado, mascara
    if estado == 0:
        mascara -= mascara // 200 #35
        if mascara < 300:
            print(frame_count)
            estado = 1
    elif estado == 1 and frame_count == 850:
        estado = 2
    elif estado == 2 and mascara < 11000:
        mascara += mascara // 50
    elif mascara > 12000:
        no_loop()
    
    mask.begin_draw()
    mask.background(0)
    mask.text_font(tf)
    mask.text_size(mascara)
    mask.text_align(CENTER, CENTER)
    mask.fill(255)
    mask.text('2023 ', 440, 400)
    mask.end_draw()
    background(240)
    text_align(CENTER, CENTER)
    f = frame_count
    years.begin_draw()
    years.text_align(CENTER, CENTER)
    years.text_font(tf)
    years.text_size(120)
    years.background(200)
    years.color_mode(HSB)
    random_seed(f // 30)
    for n in range(1999, (2024 if estado == 0 else 2100)):
#        for _ in range(2):
            x = random(width)
            y = random(width)
            years.fill((n * 10) % 256, 255, 255, 100)
            years.text(str(n), x, y)
    years.text_size(240)
    if estado == 2:
        years.fill(255, mascara / 20)
        years.text('feliz\n2024', 400, 400)    
    years.end_draw()
    years.mask(mask)
    fill(100, 255, 255, 100)
    text_size(200)
    text('adeus', 400, 150)
    image(years, 0, 0)
    
    if frame_count % 5 == 0:
        save_frame('####.png')