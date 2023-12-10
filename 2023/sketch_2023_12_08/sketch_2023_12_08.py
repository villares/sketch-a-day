import py5
from pathlib import Path

img = None
s = {
    'x':400,
    'y':150,
    'w':120,
    'h':180,
    'source_step': 10,
    'target_step':15,
    'cor_a': '#145814FF',
    'cor_b': '#E95E5E',
    'texto1': 'oito de \ndezembro'
}
save_pdf = False
modules = []

def setup():
    global img, f1
    py5.size(1200, 960)
    img = py5.load_image('a.jpg')
    load_modules(py5.sketch_path('modules'))
    f1 = py5.create_font('Open Sans Bold', 50)
    
def load_modules(modules_folder):
    modules[:] = []
    for item in sorted(modules_folder.iterdir()):
        if item.suffix == '.svg':
            modules.append(py5.load_shape(item))
        
def draw():
    global save_pdf
    py5.background(200)
    py5.scale(0.60)
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
        py5.translate(tw, 0)  # draw on the right side of the screen

        if save_pdf:
            out = py5.create_graphics(int(py5.width / 2), py5.height, py5.PDF, 'out.pdf')
            py5.begin_record(out)
        
        ss, ts = s['source_step'], s['target_step']
        for i in range(0, img_region.width, ss):
            for j in range(0, img_region.height, ss):
                px = img_region.get_pixels(i, j)
                x, y = i / ss * ts, j / ss * ts
                b = 1 - py5.brightness(px) / 255
                k = int(b * (len(modules) - 1))
                m = modules[k]
                m.disable_style()
                py5.no_stroke()
                py5.fill(s['cor_a'])
                py5.square(x, y, ts)
                py5.fill(s['cor_b'])
                py5.shape(m, x, y, ts, ts)
        py5.text_font(f1)
        py5.text_leading(43)
        py5.fill(255, 255, 240)
        py5.text(s['texto1'], 100, 200)

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

