import py5

img = None
s = {'x':100, 'y':100, 'w':100, 'h':50}
save_pdf = False



def setup():
    global img
    py5.size(1200, 600)
    img = py5.load_image('a.jpg')


def draw():
    global save_pdf
    py5.background(200)
    if img:
        f = img.width / img.height
        tw = py5.width / 2
        py5.image(img, 0, 0, tw, tw / f)
        x, y, w, h = s['x'], s['y'], s['w'], s['h']
        py5.no_fill()
        py5.stroke(255)
        py5.rect(x, y, w, h)
        xi = int(py5.remap(x, 0, tw, 0, img.width))
        yi = int(py5.remap(y, 0, tw, 0, img.width))
        wi = int(py5.remap(w, 0, tw, 0, img.width))
        hi = int(py5.remap(h, 0, tw, 0, img.width))
        img.load_np_pixels()
        img_region = py5.create_image_from_numpy(img.np_pixels[yi:yi+hi,xi:xi+wi])
        py5.translate(tw, 0)
        if save_pdf:
            out = py5.create_graphics(int(py5.width / 2), py5.height, py5.PDF, 'out.pdf')
            py5.begin_record(out)
            
        py5.image(img_region, 0, 0)                
        
        if save_pdf:
            py5.end_record()
            save_pdf = False
            
def get_region(img, x, y, w, h):
        img.load_np_pixels()
        return py5.create_image_from_numpy(img.np_pixels[y:y+h, x:x+w])
                
def get_image(selection):
    global img
    if selection:
        img = py5.load_image(selection)

def key_pressed():
    if py5.key == 'o':
        py5.select_input('imagem', get_image)
    elif py5.key == 'p':
        global save_pdf
        save_pdf = True
    elif py5.key == 's':
        py5.save_frame('out.png')


def mouse_dragged():
    dx = py5.mouse_x - py5.pmouse_x
    dy = py5.mouse_y - py5.pmouse_y
    if py5.mouse_button == py5.LEFT:
        s['x'] += dx
        s['y'] += dy
    elif py5.mouse_button == py5.RIGHT:   
        s['w'] += dx
        s['h'] += dy
    
py5.run_sketch()

