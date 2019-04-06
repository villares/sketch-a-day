"""
Code From 
https://stackoverflow.com/questions/4001948/drawing-a-triangle-in-a-coordinate-plane-given-its-three-sides
"""

class CirclesSeparate(BaseException):
    pass

class CircleContained(BaseException):
    pass

def third_point(PVector_a, PVector_b, ac_length, bc_length):
    """
    Find PVector_c given:
        PVector_a
        PVector_b
        ac_length
        bc_length

    PVector_d == PVector at which the right-angle to c is formed.
    """
    ab_length = PVector_a.dist(PVector_b)    
    if ab_length > (ac_length + bc_length):
        raise CirclesSeparate("Given sides do not intersect!")    
    elif ab_length < abs(ac_length - bc_length):
        raise CircleContained("The circles around the points do not intersect")    

    # get the length to the vertex of the right triangle formed,
    # by the intersection formed by circles a and b
    ad_length = (ab_length**2 + ac_length**2 - bc_length**2)/(2.0 * ab_length)    

    # get the height of the line at a right angle from a_length
    h  = sqrt(abs(ac_length**2 - ad_length**2))

    # Calculate the mid PVector (PVector_d), needed to calculate PVector_c(1|2)
    d_x = PVector_a.x + ad_length * (PVector_b.x - PVector_a.x)/ab_length
    d_y = PVector_a.y + ad_length * (PVector_b.y - PVector_a.y)/ab_length
    PVector_d = PVector(d_x, d_y)    

    # get PVector_c location
    # --> get x
    c_x1 = PVector_d.x + h * (PVector_b.y - PVector_a.y)/ab_length
    c_x2 = PVector_d.x - h * (PVector_b.y - PVector_a.y)/ab_length

    # --> get y
    c_y1 = PVector_d.y - h * (PVector_b.x - PVector_a.x)/ab_length
    c_y2 = PVector_d.y + h * (PVector_b.x - PVector_a.x)/ab_length    

    PVector_c1 = PVector(c_x1, c_y1)
    PVector_c2 = PVector(c_x2, c_y2)    
    return PVector_c1 #, PVector_c2 
