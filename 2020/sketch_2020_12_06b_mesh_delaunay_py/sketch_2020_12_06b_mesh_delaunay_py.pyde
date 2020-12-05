add_library('mesh')

def setup():
    size(400, 400)

def draw():
    points = []
    points.append((mouseX, mouseY))  # first point
    points.append((150, 105))  # second point
    points.append((320, 113))  # third point

    myVoronoi = Voronoi(points)
    # getRegions() returns an array of MPolygons,
    # the order of which correspond to the order of
    # the points entered. MPolygon contains the points
    # of the polygon, and can be drawn to the stage.)
    myRegions = myVoronoi.getRegions()
    for i, region in enumerate(myRegions):
    # an array of points
        regionCoordinates = region.getCoords()
        fill(64 + i * 64, 0, 0)
        region.draw(this)  # draw this shape
