
import skgeom as sg  # conda install scikit-geometry -c conda-forge
import py5

def setup():
    py5.size(600, 600)
    py5.translate(300, 300)
    py5.scale(500)
    py5.stroke_weight(1/500)
    
    poly = sg.random_polygon(seed=1)
    skel = sg.skeleton.create_interior_straight_skeleton(poly)
    draw_skeleton(poly, skel)


def draw_skeleton(polygon, skeleton, show_time=True):
    with py5.begin_closed_shape():
        py5.vertices(polygon.coords)

    for h in skeleton.halfedges:
        if h.is_bisector:
            p1 = h.vertex.point
            p2 = h.opposite.vertex.point
            py5.stroke(200, 0, 0)
            py5.line(p1.x(), p1.y(), p2.x(), p2.y())

    if show_time:
        for v in skeleton.vertices:
            py5.no_fill()
            py5.stroke(0, 0, 200)
            py5.circle(v.point.x(), v.point.y(), v.time)

py5.run_sketch()
