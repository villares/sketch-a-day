"""
polys_from_text(words, py5_font) -> list of shapely Polygons
extrude_polys(polys, depth) -> trimesh 3D mesh

TODO: I might want to flip the Y axis...
"""

import py5
import shapely
import trimesh

def polys_from_text(words: str,
                    font: py5.Py5Font,
                    leading: float = 0,
                    alternate_spacing=False) -> list[shapely.Polygon]:
    """
    Produce a list of shapely Polygons (with holes!) from a string.
    New-line chars will try to move text to a new line.
    
    The alternate_spacing option will pick the glyph
    spacing from py5.text_width() for each glyph, it can be
    too spaced, but good for monospaced font alignment.
    """
    leading = leading or font.get_size()
    py5.text_font(font)
    space_width = py5.text_width(' ')
    results = []
    x_offset = y_offset = 0
    for c in words:
        if c == '\n':
            y_offset += leading
            x_offset = 0  # assuming left aligned text...
            continue
        glyph_pt_lists = [[]] # starts with an empty list inside
        # ignore "need to call beginShape() first" warning
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
                glyph_pt_lists.append([]) # leaves trailling empty list
        if alternate_spacing:
            w = py5.text_width(c)
        else:
            w = c_shp.get_width() if vs3 else space_width
        x_offset += w
        # filter out elements with less than 3 points 
        # and stop one item before the trailling empty list
        glyph_polys = [shapely.Polygon(p)
                       for p in glyph_pt_lists[:-1] if len(p) > 2]
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

def extrude_polys(polys: shapely.Polygon | shapely.MultiPolygon,
                  depth: float) -> trimesh.Trimesh:
    """
    Extrude a Polygon or MultiPolygon
    """
    if isinstance(polys, shapely.Polygon):
        return trimesh.creation.extrude_polygon(polys, depth)
    elif isinstance(polys, shapely.MultiPolygon):
        return trimesh.util.concatenate([
            trimesh.creation.extrude_polygon(poly, depth)
            for poly in polys.geoms])

if __name__ == '__main__':
    
    # Download Saira Stencil One Regular from
    # https://fonts.google.com/specimen/Saira+Stencil+One?query=stencil

    def setup():
        global margin, slab

        py5.size(500, 500, py5.P3D)
        py5.color_mode(py5.HSB)

        for font_name in py5.Py5Font.list():
            if 'saira' in font_name.lower():
                print(font_name)
            
        f = py5.create_font('Saira Stencil One Regular', 60)
        
        t = 'py5 &\n' \
            'numpy &\n' \
            'shapely &\n' \
            'trimesh.'

        shapes = shapely.MultiPolygon(
            polys_from_text(t, f, alternate_spacing=True))
        min_x, min_y, max_x, max_y = shapes.bounds
        margin = 20
        slab_rect = shapely.Polygon(
            ((min_x - margin, min_y - margin),
             (max_x + margin, min_y - margin),
             (max_x + margin, max_y + margin),
             (min_x - margin, max_y + margin)))
        clipped_rect = slab_rect - shapes
        slab = extrude_polys(clipped_rect, 10)
        
    def draw():
        py5.background(0, 0, 100)
        py5.translate(100, 200)
        py5.rotate_x(py5.radians(py5.mouse_y))
        py5.stroke(200, 200)
        py5.shape(py5.convert_cached_shape(slab))
       
    def key_pressed():
        if py5.key == 's':
            slab.export('slab.stl')
       
    py5.run_sketch(block=False)



