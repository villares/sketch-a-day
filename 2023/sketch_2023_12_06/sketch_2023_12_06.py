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
        tw = width / 2
        image(img, 0, 0, tw, tw / f)
        x, y, w, h = s['x'], s['y'], s['w'], s['h']
        no_fill()
        stroke(255)
        rect(x, y, w, h)
        xi = int(remap(x, 0, tw, 0, img.width))
        yi = int(remap(y, 0, tw, 0, img.width))
        wi = int(remap(w, 0, tw, 0, img.width))
        hi = int(remap(h, 0, tw, 0, img.width))
        img.load_np_pixels()
        img_region = create_image_from_numpy(img.np_pixels[yi:yi+hi,xi:xi+wi])
        image(img_region, tw, 0)    
    
    
        
def get_image(selection):
    global img
    if selection:
        img = load_image(selection)

def key_pressed():
    if key == 'o':
        select_input('imagem', get_image)
    elif key == 's':
        save_frame('out.png')


def mouse_dragged():
    dx = mouse_x - pmouse_x
    dy = mouse_y - pmouse_y
    if mouse_button == LEFT:
        s['x'] += dx
        s['y'] += dy
    elif mouse_button == RIGHT:   
        s['w'] += dx
        s['h'] += dy
    

