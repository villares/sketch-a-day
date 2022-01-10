
def CSGToPShape(mesh, scale, color_maker=lambda i:255):
    """
    Convert a CSG mesh to a Processing PShape
    """
    result = createShape(GROUP)  # allocate a PShape group
    # for each polygon (Note: these can have 3,4 or more vertices)
    for i, p in enumerate(mesh.getPolygons()):
        # make a child PShape
        polyShape = createShape()
        polyShape.beginShape()
        polyShape.fill(color_maker(i))

        # for each vertex in the polygon
        for v in p.vertices:
            # add each (scaled) polygon vertex
            polyShape.vertex(v.pos.getX() * scale,
                             v.pos.getY() * scale,
                             v.pos.getZ() * scale)

        # finish this polygon
        polyShape.endShape()
        # append the child PShape to the parent
        result.addChild(polyShape)

    return result
