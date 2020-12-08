add_library('mesh')

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
    
    
    myDelaunay = Delaunay(points)

    edges = myDelaunay.getEdges()
    for i, edge in enumerate(edges):
        stroke(255, 255, 8 + i * 8)
        startX, startY, endX, endY = edge
        line(startX, startY, endX, endY)
