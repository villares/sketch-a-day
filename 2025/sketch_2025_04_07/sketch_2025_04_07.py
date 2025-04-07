import py5
import shapely

def setup():
    py5.size(400, 200)
    s = 3
    lines = []
    for i in range(30):
        x = i * s
        y = 100 - i * s
        py5.line(x * 0.8, y * 1.3,
                 x * 1.4 + 100, y * 0.5 + 100)
        lines.append(shapely.LineString(((x * 0.8, y * 1.3),
                                         (x * 1.4 + 100, y * 0.5 + 100))))
    py5.no_fill()
    py5.rect(50, 50, 80, 80)
    clipped = clip_rect(lines, 50, 50, 80, 80)
    py5.translate(200, 0)
    py5.shape(py5.convert_shape(clipped))
        
def clip_rect(shapes, x, y, w, h):
    collection = shapely.GeometryCollection(shapes)
    rect = shapely.Polygon(((x, y), (x + w, y), (x + w, y + h), (x, y + h)))
    return rect.intersection(collection)
    
py5.run_sketch(block=False)

