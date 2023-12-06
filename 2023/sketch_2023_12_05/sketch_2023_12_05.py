img = None
s = {'x':100, 'y':100, 'w':100, 'h':50}

def setup():
    global img
    size(1200, 600)
    img = load_image('a.jpg')


def draw():
    background(200)
    if img:
        f = img.width / img.height 
        image(img, 0, 0, height, height / f)
    x, y, w, h = s['x'], s['y'], s['w'], s['h']
    no_fill()
    stroke(255)
    rect(x, y, w, h)
    xi = int(remap(x, 0, width, 0, img.width))
    yi = int(remap(y, 0, width, 0, img.width))
    wi = int(remap(w, 0, width, 0, img.width))
    hi = int(remap(h, 0, width, 0, img.width))
    img_region = img.get_pixels(xi, yi, wi, hi)
#    image(img_region, width / w, 0, img_region.width * 2, img_region.height * 2)    

def key_pressed():
    save_frame('out.png')
    if key == 'o':
        select_input('imagem', get_image)
    
        
def get_image(selection):
    global img
    if selection:
        img = load_image(selection)
        
        

