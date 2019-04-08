"""
Code adapted from code by Monkut https://stackoverflow.com/users/24718/monkut
found at https://stackoverflow.com/questions/4001948/drawing-a-triangle-in-a-coordinate-plane-given-its-three-sides
"""

class NoTrianglePossible(BaseException):
    pass

def third_point(point_a, point_b, ac_length, bc_length):
    """
    Returns two point_c options given: point_a, point_b, ac_length, bc_length    
    """
    # To allow use of tuples, creates or recreates PVectors
    point_a, point_b = PVector(*point_a), PVector(*point_b)

    # check if a triangle is possible
    ab_length = point_a.dist(point_b)
    if ab_length > (ac_length + bc_length) or ab_length < abs(ac_length - bc_length):
        raise NoTrianglePossible("The sides do not form a triangle")

    # get the length to the vertex of the right triangle formed,
    # by the intersection formed by circles a and b
    ad_length = (ab_length ** 2
                 + ac_length ** 2
                 - bc_length ** 2) / (2.0 * ab_length)

    # get the height of the line at a right angle from a_length
    h = sqrt(abs(ac_length ** 2 - ad_length ** 2))

    # Calculate the mid PVector (point_d), needed to calculate point_c(1|2)
    d_x = point_a.x + ad_length * (point_b.x - point_a.x) / ab_length
    d_y = point_a.y + ad_length * (point_b.y - point_a.y) / ab_length
    point_d = PVector(d_x, d_y)

    # get point_c locations
    c_x1 = point_d.x + h * (point_b.y - point_a.y) / ab_length
    c_x2 = point_d.x - h * (point_b.y - point_a.y) / ab_length
    c_y1 = point_d.y - h * (point_b.x - point_a.x) / ab_length
    c_y2 = point_d.y + h * (point_b.x - point_a.x) / ab_length

    return PVector(c_x1, c_y1), PVector(c_x2, c_y2)
