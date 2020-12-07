add_library('mesh')

points = []

def setup():
    size(400, 400)
    for _ in range(30):
        points.append((random(width), random(height)))

def draw():
    background(200)
    points[0] = (mouseX, mouseY)  # first point

    myDelaunay = Delaunay(points)

    edges = myDelaunay.getEdges()
    for i, edge in enumerate(edges):
        stroke(8 + i * 8, 0, 0)
        startX, startY, endX, endY = edge
        line(startX, startY, endX, endY)
