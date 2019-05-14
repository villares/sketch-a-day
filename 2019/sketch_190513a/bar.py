def bar(x1, y1, z1, x2, y2, z2, weight=10):
    """
    from code by James Carruthers found on
    https://forum.processing.org/two/discussion/21400/how-to-rotate-a-3d-line-like-a-2d-line
    """
    p1 = PVector(x1, y1, z1)
    p2 = PVector(x2, y2, z2)
    v1 = PVector(x2 - x1, y2 - y1, z2 - z1)
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi = acos(v1.z / rho)
    the = atan2(v1.y, v1.x)
    v1.mult(0.5)
    with pushMatrix():
        translate(x1, y1, z1)
        translate(v1.x, v1.y, v1.z)
        rotateZ(the)
        rotateY(phi)
        # box(weight,weight,p1.dist(p2)*1.2)
        box(weight, weight, p1.dist(p2) * 1.0)
  
