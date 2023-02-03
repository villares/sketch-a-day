from shapely.geometry import Polygon, MultiPolygon, GeometryCollection, LineString, Point

def setup():
    global shapes
    size(1200, 400)
    color_mode(HSB)
    stroke(255)
    f = create_font('Inconsolata Bold', 100)
    shapes = polys_from_text('Oi B008!\né o gnumundo®...\nviva a ciberlândia!', f)


def polys_from_text(words, f=None):
    f = f or create_font('Courier', 100)
    results = []
    x_offset = y_offset = 0
    for c in words:
        if c == '\n':
            y_offset += f.get_size()
            x_offset = 0  # assuming left aligned text...
            continue
        glyph_pt_lists = [[]]
        c_shp = f.get_shape(c, 1)
        vs3 = [c_shp.get_vertex(i) for i in range(c_shp.get_vertex_count())]
        vs = set() 
        for vx, vy, _  in vs3:
            x = vx + x_offset
            y = vy + y_offset
            glyph_pt_lists[-1].append((x, y))
            if (x, y) not in vs:
                vs.add((x, y))
            else:
                glyph_pt_lists.append([])
        w = c_shp.get_width() if vs3 else f.get_size() / 3
        x_offset += w
        glyph_polys = [Polygon(p) for p in glyph_pt_lists[:-1] if len(p) > 2]
        if glyph_polys:  # yeah, ugly, but there are empty glyphs at this point.
            glyph_shapes = process_glyphs(glyph_polys)
            results.extend(glyph_shapes)
    return results
    
def process_glyphs(polys):
    polys = sorted(polys, key=lambda p: p.area, reverse=True)
    results = [polys[0]]
    for p in polys[1:]:
        # this is a bit ugly but seems to work on some edge cases like 'â'  and ®
        for i, earlier in enumerate(results):
            if earlier.contains(p):
                results[i] = results[i].difference(p)
                break
        else:   # the for-loop's else only executes after unbroken loops
            results.append(p)
    return  results

def draw():
    background(100)
    translate(100, 100)
    fill(255, 100)
    for i, shp in enumerate(shapes):
        fill((i * 8)% 256, 255, 255, 100)
        draw_shapely_objs(shp)
    
def draw_shapely_objs(element, i=0):
    if isinstance(element, (MultiPolygon, GeometryCollection)):
        for p in element.geoms:
            draw_shapely_objs(p)
    elif isinstance(element, Polygon):
#         # debug
#         push_style()
#         fill(255, 0, 0)
#         text(i, *element.exterior.coords[0])
#         pop_style()
        with begin_closed_shape():
            if element.exterior.coords:
                vertices(element.exterior.coords)
            for hole in element.interiors:
                with begin_contour():
                    vertices(hole.coords)        
    elif isinstance(element, list):
        for i, p in enumerate(element):
            draw_shapely_objs(p, i=i)
    elif isinstance(element, LineString):
        stroke(255, 0, 0)
        (xa, ya), (xb, yb) = element.coords
        line(xa, ya, xb, yb)
        no_stroke()
    elif isinstance(element, Point):
        with push_style():
            fill(255, 0, 0)
            x, y = element.coords[0]
            circle(x, y, 15)
    else:
        print(f"I can't draw {element}.")
