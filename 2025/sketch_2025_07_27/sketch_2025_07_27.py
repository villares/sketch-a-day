import py5
import shapely

from villares.arc_helpers import var_bar_pts


PAGES = 10

def setup():
    global out
    py5.size(800, 800)
    out = py5.create_graphics(
        py5.width,
        py5.height,
        py5.PDF, 'multipage_out.pdf')
    py5.begin_record(out)
    py5.text_font(py5.create_font('Tomorrow Bold', 100))
    py5.color_mode(py5.HSB)
    for page_number in range(1, PAGES + 1):
        py5.background(page_number * 20, 200, 200) # not seen on the window
        for _ in range(300):
            x, y = py5.random(py5.width), py5.random(py5.height)
            pts = var_bar_pts(x, y, x, y - 100, 25, 0)
            cc = shapely.Polygon(pts)
            py5.fill(255 - page_number * 20, 200, py5.random(128, 255))
            py5.shape(cc)
        py5.fill(0)
        #py5.text(page_number, 20, 100)
        if page_number != PAGES:
            out.next_page()
    py5.end_record()
    
py5.run_sketch()