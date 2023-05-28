from itertools import product

quad_pts = [(250, 250), (650, 250), (650, 650), (250, 650)]
margin = 250
step = 200

def setup():
    size(900, 900)
    image_mode(CENTER)
    
#def draw():
    images = []
    background(255)
    fill(200, 0, 0)
    circle(250, 250, 400)
    
    for x, y in product(range(margin//2, width , step), repeat= 2):
            clipped_image = clipped_frame(randomize(quad_pts))
            images.append((x, y, clipped_image))
            
    background(0, 0, 100)
    for x, y, img in images:
        image(img, x, y, width / 2, height / 2)
   
def randomize(pts):
    return [(x + random(-margin/6, margin/6),
             y + random(-margin/6, margin/6))
            for x, y in pts]
   
def clipped_frame(pts, img=None, border=5):
    img = g.copy() if img is None else img
    mask_shape = create_shape()
    with mask_shape.begin_closed_shape():
        for x, y in pts:
            mask_shape.vertex(x, y)
    mask_shape.disable_style()      
    mask_img = create_graphics(img.width, img.height)
    mask_img.begin_draw()
    mask_img.background(0)
    mask_img.no_stroke()
    mask_img.fill(255)
    mask_img.shape(mask_shape)
    img.mask(mask_img)
    if border:
        b = create_graphics(img.width, img.height)
        b.begin_draw()
        b.background(img)
        b.stroke(0)
        b.stroke_weight(border)
        b.no_fill()
        b.shape(mask_shape) 
        b.end_draw()
        return b
    return img
    