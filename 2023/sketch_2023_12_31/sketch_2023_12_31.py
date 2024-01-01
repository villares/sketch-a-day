import py5_tools

anim_state = 0
mask_size = 11000

def setup():
    global mask, years, tf
    size(800, 800)
    color_mode(HSB)
    tf = create_font('GaroaHackerClube-Bold', 200)  # The official font from Brazil's first hackerspace
    text_font(tf)
    mask = create_graphics(800, 800)
    years = create_graphics(800, 800)
    #py5_tools.animated_gif('out.gif', frame_numbers=range(0, 1400, 10), duration=0.1)

def draw():
    global anim_state, mask_size
    
    if anim_state == 0:
        mask_size -= mask_size // 200 
        if mask_size < 300:
            print(frame_count)
            anim_state = 1
    elif anim_state == 1 and frame_count == 850:
        anim_state = 2
    elif anim_state == 2 and mask_size < 11000:
        mask_size += mask_size // 50
    elif mask_size > 12000:
        no_loop()
    
    mask.begin_draw()
    mask.background(0)
    mask.text_font(tf)
    mask.text_size(mask_size)
    mask.text_align(CENTER, CENTER)
    mask.fill(255)
    mask.text('2023 ', 440, 400)
    mask.end_draw()

    years.begin_draw()
    years.text_align(CENTER, CENTER)
    years.text_font(tf)
    years.text_size(120)
    years.background(200)
    years.color_mode(HSB)
    random_seed(frame_count // 30)
    for n in range(1999, (2024 if anim_state == 0 else 2100)):
        x = random(width)
        y = random(width)
        years.fill((n * 10) % 256, 255, 255, 100)
        years.text(str(n), x, y)
    years.text_size(240)
    if anim_state == 2:
        years.fill(255, mask_size / 20)
        years.text('happy\n2024', 400, 400)    
    years.end_draw()
    years.mask(mask)
   
    background(240)
    text_align(CENTER, CENTER)
    fill(100, 255, 255, 100)
    text_size(200)
    text('bye bye', 400, 150)
    image(years, 0, 0)