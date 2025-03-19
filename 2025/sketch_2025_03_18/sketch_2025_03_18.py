import py5
import py5_tools

R = 52
ROWS = 11
COLS = 10

def setup():
    global img, mask
    py5.size(800, 800)
    img = py5.create_graphics(R * 2, R * 2)
    py5.image_mode(py5.CENTER)
    mask = make_mask(R * 2, R * 2)
    py5_tools.animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 31))
    
def draw():
    py5.background(0)
    w = R * py5.sqrt(3)
    h = R * 1.5
    i = 0 
    for row in range(ROWS):
        y = row * h
        for col in range(COLS):
            x = col * w
            if row % 2 == 1:
                x += w / 2
            py5.random_seed(0)
            update_img(90 + i + py5.frame_count * 12)
            i += 1
            clipped = clip_with_mask(
                    img, mask, img.width / 2, img.height / 2)
            with py5.push_matrix():
                py5.translate(x, y)
#                 py5.rotate((row + col % 2) * py5.TWO_PI / 6)
                py5.image(clipped, 0, 0)
    #py5.image(img, 400, 400) # test/debug!
    #py5.save_frame('###.png')



def update_img(ang):
    ra = py5.radians(ang)
    w =  R / 2 + R / 3 * py5.sin(ra)
    h =  R / 2 + R / 3 * py5.cos(ra)
    img.begin_draw()
    img.background(0)
    img.no_stroke()
    img.fill(w * 5, h * 5, 128)
    img.ellipse(R * 1.5, R * 1.5, w, h)
    img.end_draw()

    
def make_mask(w, h):
    m = py5.create_graphics(int(w), int(h))
    m.begin_draw()
    m.fill(255)
    m.no_stroke()
    with m.begin_shape():
        for n in range(6):
            ang = (n + 0.5) * py5.TWO_PI / 6 
            x = w / 2 * py5.cos(ang) + w / 2
            y = h / 2 * py5.sin(ang) + h / 2
            m.vertex(x, y)
    m.end_draw()
    return m
         
def clip_with_mask(img, mask, x, y):    
    """Clip an image using a mask, its dimensions, and a position."""
    w, h = mask.width, mask.height
    result = py5.create_image(mask.width, mask.height, py5.ARGB)
    result.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    result.mask(mask)
    return result

def key_pressed():
    py5.redraw()

py5.run_sketch(block=False)
