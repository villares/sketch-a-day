import py5
import shapely

def setup():
    py5.size(400, 400)
    s = 3
    lines = []
    for i in range(30):
        x = i * s
        y = 100 - i * s
        lines.append(shapely.LineString(((x * 0.8, y * 1.3),
                                         (x * 1.4 + 100, y * 0.5 + 100))))
    clipped = clip_rect(lines, 50, 50, 80, 80)
    shp = py5.convert_shape(clipped)
    for x in range(0, py5.width, 80):
        for y in range(0, py5.height, 80):
            py5.shape(shp, x, y)
    py5.save_frame('out.png')


def clip_rect(shapes, x, y, w, h):
    global rect
    collection = shapely.GeometryCollection(shapes)
    rect = shapely.Polygon(((x, y), (x + w, y), (x + w, y + h), (x, y + h)))
    intersection = rect.intersection(collection)
    return shapely.affinity.translate(intersection, -x, -y) 
    
py5.run_sketch(block=False)
