from itertools import chain

import py5
from shapely.geometry import Polygon, MultiPolygon, MultiPoint

# Experiment to extract poly shapes from a text rendered in a specific font
# Demo sketch for poly_from_text() and draw_shapely_objs()

TEXT = 'Py5Font'


def setup():
    global d_font
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
    py5.stroke(255)
    d_font = py5.create_font('Open Sans', 100)
    py5.no_loop()
    
def draw():
    global shapes
    py5.background(100)
    py5.translate(50, 100)    
        
    shapes = polys_from_text(
        TEXT, d_font, alternate_spacing=py5.is_mouse_pressed)
    
#     for s in shapes:
#         print(type(s))
    multipoly = MultiPolygon(shapes)
    py5.no_stroke()
    pshape = py5.convert_shape(multipoly)
    py5.shape(pshape, 0, 0)
    py5.stroke(0)
    py5.stroke_weight(3)
    multipoints = MultiPoint(list(chain(list(p.exterior.coords) for p in multipoly.geoms)))
    pshape = py5.convert_shape(multipoints)
    py5.shape(pshape, 0, 0)
    
    


def polys_from_text(words, font, alternate_spacing=False):
    """
    Produce a list of shapely Polygons (with holes!) from a string.
    New-line chars will try to move text to a new line.
    
    The alternate_spacing option will pick the glyph
    spacing from py5.text_width() for each glyph, it can be
    too spaced, but good for monospaced font alignment.
    """
    py5.text_font(font)
    space_width = py5.text_width(' ')
    results = []
    x_offset = y_offset = 0
    for c in words:
        if c == '\n':
            y_offset += font.get_size()
            x_offset = 0  # assuming left aligned text...
            continue
        glyph_pt_lists = [[]]  # começa com uma "lista atual" vazia
        c_shp = font.get_shape(c, 1) #py5.mouse_x / 10)
#         if c == 'a':
#             print(py5.mouse_x / 10, c_shp.get_vertex_count())
        vs3 = [c_shp.get_vertex(i) for i in range(c_shp.get_vertex_count())]
        #if c == 'a': print(c_shp.get_vertex(0))
        
        vs = set()
        for vx, vy, _ in vs3:
            x = vx + x_offset
            y = vy + y_offset
            lista_atual = glyph_pt_lists[-1] # sempre a última lista 
            lista_atual.append((x, y))
            if (x, y) not in vs:
                vs.add((x, y))
            else:
                glyph_pt_lists.append([])  # will leave a trailling empty list
                # [[(...,...)...], [(...,...)...], []]
              
        if not vs3 or alternate_spacing:
            w = py5.text_width(c)
        else:
            w = c_shp.get_width() 
        x_offset += w
        # filter out elements with less than 3 points 
        # and stop before the trailling empty list
        glyph_polys = [Polygon(p) for p in glyph_pt_lists[:-1] if len(p) > 2]
        if glyph_polys:  # there are still empty glyphs at this point
            glyph_shapes = process_glyphs(glyph_polys)
            results.extend(glyph_shapes)
    return results


def process_glyphs(polys):
    """
    Try to subtract the shapely Polygons representing a glyph
    in order to produce appropriate looking glyphs!
    """
    polys = sorted(polys, key=lambda p: p.area, reverse=True)
    results = [polys[0]]
    for p in polys[1:]:
        # works on edge cases like â and ®
        for i, earlier in enumerate(results):
            if earlier.contains(p):
                results[i] = results[i].difference(p)
                break
        else:   # the for-loop's else only executes after unbroken loops
            results.append(p)
    return results



if __name__ == '__main__':
    py5.run_sketch(block=False)
