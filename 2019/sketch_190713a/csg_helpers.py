


def csgTranslate(csg, x, y, z):
    return csg.transformed(Transform.unity().translate(x, y, z))

def csgRot(csg, x, y, z):
    return csg.transformed(Transform.unity().rot(x, y, z))

def CSGToPShape(mesh, scale):
    """
    Convert a CSG mesh to a Processing PShape
    """
    result = createShape(GROUP)  # allocate a PShape group
    # for each polygon (Note: these can have 3,4 or more vertices)
    for p in mesh.getPolygons():
        # make a child PShape
        polyShape = createShape()
        # begin setting vertices to it
        polyShape.beginShape()
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
