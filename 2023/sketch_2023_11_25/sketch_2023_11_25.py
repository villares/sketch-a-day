
from functools import cache

passo = 10

cor_b = color(150, 150, 250)
cor_a = color(50, 150, 100)

def setup():
    global img
    size(1440, 720)
    img = load_image('2.jpg')
    print(img.width, img.height)
    no_loop()
    no_stroke()
    #color_mode(HSB)
    rect_mode(CENTER)
    text_font(create_font('Inconsolata Bold', passo + 2))
    text_align(CENTER, CENTER)
    
def draw():
    background(255)
    #image(img, 0, 0)
    xi, yi, wi, hi = 0, 0, img.width, img.height
    for x in range(0, width, passo):
        for y in range(0, height, passo):
            xa = int(remap(x, 0, width, xi, xi + wi))
            ya = int(remap(y, 0, height, yi, yi + hi))
            c = img.get_pixels(xa , ya)
            elemento(passo / 2 + x,
                     passo / 2 + y, b(c))
            
         
@cache
def b(c):
    return brightness(c)
         
def elemento(x, y, b):
    rect_mode(CENTER)
    if b < 200:
        if b < 128:
            fill(cor_a)
        else:
            fill(cor_b)
        square(x, y, passo)

    fill(cor_b if b > 200 else 255)
    d = 12 * (255 - b) / 255 + 1.5
    t = '.-+*0X1'[int(d) // 2]
    #text_size(passo + 2)
    text(t, x, y - 2)

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
    