
from functools import cache

passo = 10
stats = set()

cor_a = color(150, 150, 250)
cor_b = color(250, 150, 100)

def setup():
    global img
    size(1440, 720)
    img = load_image('1.jpg')
    print(img.width, img.height)
    no_loop()
    no_stroke()
    #color_mode(HSB)
    rect_mode(CENTER)
    text_font(create_font('Inconsolata Bold', 10))
    text_align(CENTER, CENTER)
    
def draw():
    background(cor_a)
    #image(img, 0, 0)
    xi, yi, wi, hi = 0, 0, img.width, img.height
    for x in range(0, width, passo):
        for y in range(0, height, passo):
            xa = int(remap(x, 0, width, xi, xi + wi))
            ya = int(remap(y, 0, height, yi, yi + hi))
            c = img.get_pixels(xa , ya)
            elemento(passo / 2 + x,
                     passo / 2 + y, b(c))
            
    save_frame(__file__[:-3] + '.png')
    print(len(stats), stats)

         
@cache
def b(c):
    return brightness(c)
         
def elemento(x, y, b):
    rect_mode(CENTER)
    fill(cor_b if b < 128 else 255)
    d = 12 * b / 255 + 1.5
    stats.add(int(d) // 2)
    t = '*+-.1X0'[int(d) // 2]
    text_size(14)
    text(t, x, y)
#     rect(x, y, w, w / 3)
#     rect(x, y, w / 3, w)

def key_pressed():
    save_stamp()
    redraw()

def save_stamp():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('.', '')    
    save(p / stamp / (stamp + '.png')) 
    shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    