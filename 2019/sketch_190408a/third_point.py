"""
Code adapted from code by Monkut https://stackoverflow.com/users/24718/monkut
found at https://stackoverflow.com/questions/4001948/drawing-a-triangle-in-a-coordinate-plane-given-its-three-sides
"""

class NoTrianglePossible(BaseException):
    pass

def third_point(a, b, ac_len, bc_len):
    """
    Returns two point c options given:
    point a, point b, ac length, bc length    
    """
    # To allow use of tuples, creates or recreates PVectors
    a, b = PVector(*a), PVector(*b)

    # check if a triangle is possible
    ab_len = a.dist(b)
    if ab_len > (ac_len + bc_len) or ab_len < abs(ac_len - bc_len):
        raise NoTrianglePossible("The sides do not form a triangle")

    # get the length to the vertex of the right triangle formed,
    # by the intersection formed by circles a and b
    ad_len = (ab_len ** 2 + ac_len ** 2 - bc_len ** 2) / (2.0 * ab_len)

    # get the height of the line at a right angle from a_len
    h = sqrt(abs(ac_len ** 2 - ad_len ** 2))

    # Calculate the mid PVector (point d), needed to calculate point c(1|2)
    d_x = a.x + ad_len * (b.x - a.x) / ab_len
    d_y = a.y + ad_len * (b.y - a.y) / ab_len
    d = PVector(d_x, d_y)

    # get point_c locations
    c_x1 = d.x + h * (b.y - a.y) / ab_len
    c_x2 = d.x - h * (b.y - a.y) / ab_len
    c_y1 = d.y - h * (b.x - a.x) / ab_len
    c_y2 = d.y + h * (b.x - a.x) / ab_len

    return PVector(c_x1, c_y1), PVector(c_x2, c_y2)
