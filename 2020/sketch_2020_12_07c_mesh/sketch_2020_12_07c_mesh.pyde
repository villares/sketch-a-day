add_library('mesh')

# HORRIBLY SLOW

from villares.line_geometry import draw_poly, hatch_poly
from villares.helpers import memoize

points = []

def setup():
    size(400, 400)
    for _ in range(30):
        points.append((random(width), random(height)))

def draw():
    background(200)
    points[0] = (mouseX, mouseY)  # first point
    myVoronoi = Voronoi(points)
    myRegions = myVoronoi.getRegions()
    for i, region in enumerate(myRegions):
    # an array of points
        regionCoordinates = region.getCoords()
        fill(32 + i * 8, 0, 64)
        stroke(0)
        region.draw(this)  # draw this shape
        # draw_poly(region.getCoords())    
        coords = (tuple(c) for c in region.getCoords())
        ps = hp(tuple(coords), i, spacing=10, ps=True)
        shape(ps)    
    
@memoize
def hp(*args, **kwargs):
    return hatch_poly(*args, **kwargs)        
    
    # myDelaunay = Delaunay(points)

    # edges = myDelaunay.getEdges()
    # for i, edge in enumerate(edges):
    #     stroke(255, 255, 8 + i * 8)
    #     startX, startY, endX, endY = edge
    #     line(startX, startY, endX, endY)
