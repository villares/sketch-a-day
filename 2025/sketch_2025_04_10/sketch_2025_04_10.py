import py5
import shapely

def setup():
    py5.size(400, 400)
    py5.color_mode(py5.HSB)
    s = 10
    lines = []
    for i in range(30):
        x = i * s
        y = 100 - i * s
        ls = shapely.LineString(((x * 0.8, y * 1.3),
                                 (x * 1.4 + 100, y * 0.5 + 100)))
        lines.append(ls)
    collection = shapely.GeometryCollection(lines).buffer(5)
    clipped = clip_rect(collection, 50, 50, 80, 80)
    py5.no_stroke()
    shp = py5.convert_shape(clipped)
    shp.disable_style()
    for x in range(40, py5.width, 80):
        for y in range(40, py5.height, 80):
            with py5.push_matrix():
                py5.translate(x, y)
                py5.rotate(py5.radians(py5.random_choice((
                    0, 90, 180, 270
                    ))))
                for i, sub in enumerate(shp.get_children()):
                    py5.fill(i * 25, 200, 200)
                    py5.shape(sub, 0, 0)
    py5.save_frame('out.png')

def clip_rect(shp, x, y, w, h):
    global rect
    rect = shapely.Polygon(((x, y), (x + w, y), (x + w, y + h), (x, y + h)))
    intersection = rect.intersection(shp)
    return shapely.affinity.translate(intersection,
                                      -x - w / 2, -y - h / 2) 
    
py5.run_sketch(block=False)
