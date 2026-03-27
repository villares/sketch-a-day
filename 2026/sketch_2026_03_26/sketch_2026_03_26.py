# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import py5_tools
import shapely

def setup():
    global polys
    py5.size(500, 500)
    f = py5.create_font('Source Code Pro Bold', 180) 
    polys = polys_from_text('rest!', f)
    py5_tools.animated_gif('out.gif',
                            frame_numbers=range(1, 37),
                            duration=0.03) 
 
def draw():
    py5.background(0)
    w = 24
    gap = 12
    start = py5.frame_count % (w + gap)
    h = -200
    py5.no_stroke()
    for x in range(-start, py5.width, w + gap):
        y = 5 * py5.sin(py5.radians(x + start * 10))
        pontos = ((x, 10), (x + w, 10),
                  (x + w, h), (x, h))
        p = shapely.Polygon(pontos).buffer(-1)
        pi = polys.intersection(p).buffer(5)
        py5.fill(x / 2, 0, 255 - x / 2)
        py5.shape(pi, 0, 300 + y)

def polys_from_text(
    words: str,
    font: py5.Py5Font,
    leading: float = None, 
    alternate_spacing=False
    
    ) -> shapely.GeometryCollection:
    """
    Produce from a string a shapely GeometryCollection containing
    MultiPolygons for each glyph. The MultiPolygon.geoms contains
    one or more shapely.Polygon objects (which can have holes).
    New-line chars will try to move text to a new line.
    
    The alternate_spacing option will pick the glyph
    spacing from py5.text_width() for each glyph, it can be
    too spaced, but good for monospaced font alignment.
    """
    if isinstance(font, tuple):
        name, size = font
        font = py5.create_font(name, size)
    # Use the font size as leading value if none is provided.
    leading = leading or font.get_size()
    py5.text_font(font)
    space_width = py5.text_width(' ')
    results = []
    x_offset = y_offset = 0
    for c in words:
        if c == '\n':
            y_offset += leading
            x_offset = 0  # this assumes left aligned text...
            continue
        glyph_pt_lists = [[]] # starts with an empty list inside
        # font.get_shape(c, 1) will trigger a "Need to call beginShape() first"
        # Processing warning you can safely ignore.
        c_shp = font.get_shape(c, 1)  
        vs3d = [c_shp.get_vertex(i)
                for i in range(c_shp.get_vertex_count())]
        vs = set()
        for vx, vy, _ in vs3d:
            x = vx + x_offset
            y = vy + y_offset
            glyph_pt_lists[-1].append((x, y))
            if (x, y) not in vs:
                vs.add((x, y))
            else:
                glyph_pt_lists.append([]) # note this leaves trailling empty list
        if alternate_spacing:
            w = py5.text_width(c)
        else:
            w = c_shp.get_width() if vs3d else space_width
        x_offset += w
        # filter out elements with less than 3 points 
        # and stop one item before the trailling empty list
        glyph_polys = [shapely.Polygon(p)
                       for p in glyph_pt_lists[:-1] if len(p) > 2]
        if glyph_polys:  # there are still empty glyphs at this point
            glyph_shapes = process_glyphs(glyph_polys)
            results.append(glyph_shapes)
    return shapely.GeometryCollection(results)

def process_glyphs(polys: list[shapely.Polygon]) -> shapely.MultiPolygon:
    """
    Try to subtract the shapely Polygons from glyph contours
    in order to produce appropriate looking glyphs with holes.
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
    return shapely.MultiPolygon(results)


def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)


