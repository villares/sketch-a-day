quad_pts = [50, 100, 400, 50, 450, 400, 100, 400]

def setup():
    size(600, 600)
    
#def draw():
    #background(100)
    fill(255)
    quad(*quad_pts)
    fill(200, 0, 0)
    circle(100, 100, 300)
    img = g.copy()
    
    clipped_image = quad_mask(img, *quad_pts) #, border=5)
    background(0, 0, 100)
    image(clipped_image, 0, 0)
    image(clipped_image, 50, 75)
    image(clipped_image, 100, 150)
    
def quad_mask(img, x0, y0, x1, y1, x2, y2, x3, y3, border=5):
    clip_mask = create_graphics(width, height)
    clip_mask.begin_draw()
    clip_mask.background(0)
    clip_mask.no_stroke()
    clip_mask.fill(255)
    clip_mask.quad(x0, y0, x1, y1, x2, y2, x3, y3)
    clip_mask.end_draw()
    img.mask(clip_mask)
    if border:
        b = create_graphics(width, height)
        b.begin_draw()
        b.background(img)
        b.stroke(0)
        b.stroke_weight(border)
        b.no_fill()
        b.quad(x0, y0, x1, y1, x2, y2, x3, y3)
        b.end_draw()
        return b
    return img
    
# def quad_mask(x0, y0, x1, y1, x2, y2, x3, y3):
#     min_x, min_y = min(x0, x1, x2, x3), min(y0, y1, y2, y3)
#     max_x, max_y = max(x0, x1, x2, x3), max(y0, y1, y2, y3)
#     w, h = max_x - min_x, max_y - min_y
#     clip_mask = create_graphics(w, h)
#     clip_mask.begin_draw()
#     clip_mask.background(0)
#     clip_mask.no_stroke()
#     clip_mask.fill(255)
#     clip_mask.quad(x0 - min_x, y0 - min_y,
#                    x1 - min_x, y1 - min_y,
#                    x2 - min_x, y2 - min_y,
#                    x3 - min_x, y3 - min_y)
#     clip_mask.end_draw()
#     return clip_mask

