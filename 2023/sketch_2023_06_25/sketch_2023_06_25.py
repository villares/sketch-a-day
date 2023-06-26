
import numpy as np
import py5

def setup():
    global striped_circle
    py5.size(800, 800)
    py5.image_mode(py5.CENTER) # draw images from center
    striped_circle = make_circle()
    
def make_circle():
    global m
    # circle
    c = py5.create_graphics(py5.width, py5.height)
    c.begin_draw()
    c.stroke_weight(5)
    c.stroke(150, 150, 0)
    c.fill(0, 0, 100, 20) # check ou this translucent fill!
    c.rect_mode(py5.CENTER)
    for shrink in range(10):
        c.circle(c.width / 2, c.height / 2, c.width * (0.95 - shrink / 10))
    c.end_draw()
    # mask with stripes
    m = py5.create_graphics(py5.width, py5.height)
    m.begin_draw()
    m.fill(255)  # visible stripes
    for x in range(0, m.width, 80):
        m.rect(x, 0, 40, m.height)
    m.end_draw()
    # apply mask and return image
    c.load_np_pixels()
    m.load_np_pixels()
    c.np_pixels[:, :, 0] = np.where(m.np_pixels[:, :, 0] < c.np_pixels[:, :, 0],
                                    m.np_pixels[:, :, 0], c.np_pixels[:, :, 0])
    c.update_np_pixels()
    return c

def draw():
     py5.background(0, 100 , 100)
     #py5.image(m, 0, 0)
     py5.stroke_weight(5)
     py5.stroke(150, 150, 0)
     for y in range(0, py5.height + 1, 40):
         py5.line(0, y, py5.width, y)
     py5.translate(py5.width / 2, py5.height / 2)
     py5.rotate(py5.radians(py5.frame_count))
     py5.image(striped_circle, 0, 0)
     py5.rotate(-2 * py5.radians(py5.frame_count))
     py5.image(striped_circle, 0, 0)
     f = py5.frame_count
     if f < 361 and f % 2 == 0:
         py5.save_frame('###.png')

py5.run_sketch()
