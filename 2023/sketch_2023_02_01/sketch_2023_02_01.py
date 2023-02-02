import trimesh
import shapely
# https://iamkate.com/data/12-bit-rainbow/
palette = (
    '#817', '#a35', '#c66', '#e94',
    '#ed0', '#9d5', '#4d8', '#2cb',
    '#0bc', '#09c', '#36b', '#639'
    )

def setup():
    global m
    size(400, 400, P3D)
    no_stroke()
    polygon = shapely.geometry.Polygon([(-100, -100), (0, -100),
                                        (0, 0), (-50, -50), (-100, 0)])
    m = trimesh.creation.extrude_polygon(polygon, 30)
      
def draw():
    background(0)
    translate(width /2, height / 2)
    rotate_x(QUARTER_PI)
    rotate_y(radians(mouse_x))
    for i, face in enumerate(m.faces):
        fill(palette[i % 12])
        with begin_closed_shape():
            vertices([m.vertices[v] for v in face])
  
