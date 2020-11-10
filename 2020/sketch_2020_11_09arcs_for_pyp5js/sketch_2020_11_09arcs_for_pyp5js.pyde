from itertools import product
from random import sample

BORDER = 100
SIZE = 50
NUM_POINTS = 5

def setup():
    size(400, 400)
    rect(20, 20, 200, 200)
    radii = [10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40, 40]
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    r_list = sample(radii, NUM_POINTS)
    p_list = sample(grid, NUM_POINTS)
    # print('done')

    background(210, 200, 200)
    # print(arcs.arc_augmented_poly(p_list, r_list, check_intersection=True))
    stroke(128)
    strokeWeight(10)
    noFill()
    translate(4, 10)
    arc_augmented_poly(p_list, r_list, arc_func=p_arc, num_points=16)
    arc_filleted_poly(p_list, r_list, arc_func=p_arc, num_points=16)


from warnings import warn

BOTTOM = 0
DEBUG = False
def triangle_area(a, b, c):
    area = (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))
    return area



def b_arc(cx, cy, w, h, start_angle, end_angle, mode=0):
    """
    Draw a bezier approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc, using beginShape() and endShape()
          1 "middle" used in recursive call of smaller arcs
          2 "naked" like normal, but without beginShape() and
             endShape() for use inside a larger PShape.
    """
    # Based on ideas from Richard DeVeneza via code by Gola Levin:
    # http://www.flong.com/blog/2009/bezier-approximation-of-a-circular-arc-in-processing/
    theta = end_angle - start_angle
    # Compute raw Bezier coordinates.
    if mode != 1 or abs(theta) < HALF_PI:
        x0 = cos(theta / 2.0)
        y0 = sin(theta / 2.0)
        x3 = x0
        y3 = 0 - y0
        x1 = (4.0 - x0) / 3.0
        y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0) if y0 != 0 else 0
        x2 = x1
        y2 = 0 - y1
        # Compute rotationally-offset Bezier coordinates, using:
        # x' = cos(angle) * x - sin(angle) * y
        # y' = sin(angle) * x + cos(angle) * y
        bezAng = start_angle + theta / 2.0
        cBezAng = cos(bezAng)
        sBezAng = sin(bezAng)
        rx0 = cBezAng * x0 - sBezAng * y0
        ry0 = sBezAng * x0 + cBezAng * y0
        rx1 = cBezAng * x1 - sBezAng * y1
        ry1 = sBezAng * x1 + cBezAng * y1
        rx2 = cBezAng * x2 - sBezAng * y2
        ry2 = sBezAng * x2 + cBezAng * y2
        rx3 = cBezAng * x3 - sBezAng * y3
        ry3 = sBezAng * x3 + cBezAng * y3
        # Compute scaled and translated Bezier coordinates.
        rx, ry = w / 2.0, h / 2.0
        px0 = cx + rx * rx0
        py0 = cy + ry * ry0
        px1 = cx + rx * rx1
        py1 = cy + ry * ry1
        px2 = cx + rx * rx2
        py2 = cy + ry * ry2
        px3 = cx + rx * rx3
        py3 = cy + ry * ry3
        if DEBUG:
            ellipse(px3, py3, 3, 3)
            ellipse(px0, py0, 5, 5)
    # Drawing
    if mode == 0:  # 'normal' arc (not 'middle' nor 'naked')
        beginShape()
    if mode != 1:  # if not 'middle'
        vertex(px3, py3)
    if abs(theta) < HALF_PI:
        bezierVertex(px2, py2, px1, py1, px0, py0)
    else:
        # to avoid distortion, break into 2 smaller arcs
        b_arc(cx, cy, w, h, start_angle, end_angle - theta / 2.0, mode=1)
        b_arc(cx, cy, w, h, start_angle + theta / 2.0, end_angle, mode=1)
    if mode == 0:  # end of a 'normal' arc
        endShape()

def p_circle_arc(x, y, radius, start_ang, sweep_ang, mode=0, **kwargs):
    p_arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang,
          mode=mode, **kwargs)

def p_arc(cx, cy, w, h, start_angle, end_angle, mode=0,
          num_points=24, vertex_func=None):
    """
    A poly approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc, using beginShape() and endShape()
          2 "naked" like normal, but without beginShape() and
             endShape() for use inside a larger PShape.
    """
    vertex_func = vertex_func or vertex
    sweep_angle = end_angle - start_angle
    if mode == 0:
        beginShape()
    if sweep_angle < 0:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
        angle = float(sweep_angle) / abs(num_points)
        a = end_angle
        while a >= start_angle:
            sx = cx + cos(a) * w / 2.0
            sy = cy + sin(a) * h / 2.0
            vertex_func(sx, sy)
            a -= angle
    elif sweep_angle > 0:
        angle = sweep_angle / int(num_points)
        a = start_angle
        while a <= end_angle:
            sx = cx + cos(a) * w / 2.0
            sy = cy + sin(a) * h / 2.0
            vertex_func(sx, sy)
            a += angle
    else:  # sweep_angle == 0
        sx = cx + cos(start_angle) * w / 2.0
        sy = cy + sin(start_angle) * h / 2.0
        vertex_func(sx, sy)
    if mode == 0:
        endShape()


def arc_filleted_poly(p_list, r_list, **kwargs):
    """
    Draws a 'filleted' polygon with variable radius, depends on arc_corner()
    
    2020-09-24 Rewritten from poly_rounded2 to be a continous PShape 
    2020-09-27 Moved default args to kwargs, added kwargs support for custom arc_func
    """
    arc_func = kwargs.pop('arc_func', b_arc)  # draws with bezier aprox. arc by default
    open_poly = kwargs.pop('open_poly', False)  # assumes a closed poly by default

    p_list, r_list = list(p_list), list(r_list)
    beginShape()
    if not open_poly:
        for p0, p1, p2, r in zip(p_list,
                                 [p_list[-1]] + p_list[:-1],
                                 [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                                 [r_list[-1]] + r_list[:-1]
                                 ):
            m1 = (PVector(p0[0], p0[1]) + PVector(p1[0], p1[1])).div(2)
            m2 = (PVector(p2[0], p2[1]) + PVector(p1[0], p1[1])).div(2)
            arc_corner(p1, m1, m2, r, arc_func=arc_func, **kwargs)
        endShape(CLOSE)
    else:
        for p0, p1, p2, r in zip(p_list[:-1],
                                 [p_list[-1]] + p_list[:-2],
                                 [p_list[-2]] + [p_list[-1]] + p_list[:-3],
                                 [r_list[-1]] + r_list[:-2]
                                 ):
            m1 = (PVector(p0[0], p0[1]) + PVector(p1[0], p1[1])) / 2
            m2 = (PVector(p2[0], p2[1]) + PVector(p1[0], p1[1])) / 2
            arc_corner(p1, m1, m2, r, arc_func=arc_func, **kwargs)
        endShape()

def arc_corner(pc, p1, p2, r, **kwargs):
    """
    Draw an arc that 'rounds' the point pc between p1 and p2 using arc_func
    Based on '...rounded corners in a polygon' from https://stackoverflow.com/questions/24771828/
    
    2020-09-27 Added support for custom arc_func & kwargs
    """
    arc_func = kwargs.pop('arc_func', b_arc)  # draws with bezier aprox. arc by default

    def proportion_point(pt, segment, L, dx, dy):
        factor = float(segment) / L if L != 0 else segment
        return PVector((pt[0] - dx * factor), (pt[1] - dy * factor))

    # Vectors 1 and 2
    dx1, dy1 = pc[0] - p1[0], pc[1] - p1[1]
    dx2, dy2 = pc[0] - p2[0], pc[1] - p2[1]
    # Angle between vector 1 and vector 2 divided by 2
    angle = (atan2(dy1, dx1) - atan2(dy2, dx2)) / 2
    # The length of segment between angular point and the
    # points of intersection with the circle of a given radius
    tng = abs(tan(angle))
    segment = r / tng if tng != 0 else r
    # Check the segment
    length1 = sqrt(dx1 * dx1 + dy1 * dy1)
    length2 = sqrt(dx2 * dx2 + dy2 * dy2)
    min_len = min(length1, length2)
    if segment > min_len:
        segment = min_len
        max_r = min_len * abs(tan(angle))
    else:
        max_r = r
    # Points of intersection are calculated by the proportion between
    # length of vector and the length of the segment.
    p1Cross = proportion_point(pc, segment, length1, dx1, dy1)
    p2Cross = proportion_point(pc, segment, length2, dx2, dy2)
    # Calculation of the coordinates of the circle
    # center by the addition of angular vectors.
    dx = pc[0] * 2 - p1Cross.x - p2Cross.x
    dy = pc[1] * 2 - p1Cross.y - p2Cross.y
    L = sqrt(dx * dx + dy * dy)
    d = sqrt(segment * segment + max_r * max_r)
    arc_center = proportion_point(pc, d, L, dx, dy)
    # start_angle and end_angle of arc
    start_angle = atan2(p1Cross.y - arc_center.y, p1Cross.x - arc_center.x)
    end_angle = atan2(p2Cross.y - arc_center.y, p2Cross.x - arc_center.x)
    # Sweep angle
    sweep_angle = end_angle - start_angle
    # Some additional checks
    nsa = False  # negative sweep angle
    if sweep_angle < 0:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
        nsa = True
        if DEBUG:
            circle(arc_center.x, arc_center.y, max_r / 2)
    lsa = False  # large sweep angle
    if sweep_angle > PI:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = TWO_PI - sweep_angle
        lsa = True
        if DEBUG:
            circle(arc_center.x, arc_center.y, max_r)
    if (lsa and nsa) or (not lsa and not nsa):
        # reverse sweep direction
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
    # draw "naked" arc (without beginShape & endShape)
    arc_func(arc_center.x, arc_center.y, 2 * max_r, 2 * max_r,
             start_angle, start_angle + sweep_angle, mode=2, **kwargs)


def arc_augmented_poly(op_list, or_list=None, **kwargs):
    """
    Draw a continous PShape "Polyline" as if around pins of various diameters.
    Has an ugly check_intersection mode that dows not draw and "roughly" checks
    for self intersections using slow polygon aproximations.
    2020-09-22 Renamed from b_poly_arc_augmented 
    2020-09-24 Removed Bezier mode in favour of arc_func + any keyword arguments.
    2020-09-26 Moved arc_func to kwargs, updates exceptions
    """
    assert op_list, 'No points were provided.'
    if or_list == None:
        r2_list = [0] * len(op_list)
    else:
        r2_list = or_list[:]
    assert len(op_list) == len(r2_list),\
        'Number of points and radii provided not the same.'
    check_intersection = kwargs.pop('check_intersection', False)
    arc_func = kwargs.pop('arc_func', None)
    if check_intersection and arc_func:
        warn("check_intersection mode overrides arc_func (arc_func ignored).")
    if check_intersection:
        global _points, vertex_func
        _points = []
        vertex_func = lambda x, y: _points.append((x, y))
        arc_func = p_arc
        kwargs = {"num_points": 4, "vertex_func": vertex_func}
    else:
        vertex_func = vertex
        arc_func = arc_func or b_arc
    # remove overlapping adjacent points
    p_list, r_list = [], []
    for i1, p1 in enumerate(op_list):
        i2 = (i1 - 1)
        p2, r2, r1 = op_list[i2], r2_list[i2], r2_list[i1]
        if dist(p1[0], p1[1], p2[0], p2[1]) > 1:  # or p1 != p2:
            p_list.append(p1)
            r_list.append(r1)
        else:
            r2_list[i2] = min(r1, r2)
    # invert radius
    for i1, p1 in enumerate(p_list):
        i0 = (i1 - 1)
        p0 = p_list[i0]
        i2 = (i1 + 1) % len(p_list)
        p2 = p_list[i2]
        a = triangle_area(p0, p1, p2) / 1000.
        if or_list == None:
            r_list[i1] = a
        else:
            # if abs(a) < 1:
            #     r_list[i1] = r_list[i1] * abs(a)
            if a < 0:
                r_list[i1] = -r_list[i1]
    # reduce radius that won't fit
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 = p_list[i2], r_list[i2], r_list[i1]
        r_list[i1], r_list[i2] = reduce_radius(p1, p2, r1, r2)
    # calculate the tangents
    a_list = []
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 = p_list[i2], r_list[i2], r_list[i1]
        cct = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(cct)
    # check basic "skeleton poly" intersection (whithout the p_arc aprox.)
    if check_intersection:
        skeleton_points = []
        for ang, p1, p2 in a_list:
            skeleton_points.append(p1)
            skeleton_points.append(p2)
        if is_poly_self_intersecting(skeleton_points):
            return True
    # now draw it!
    beginShape()
    for i1, ia in enumerate(a_list):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a1, p11, p12 = ia
        a2, p21, p22 = a_list[i2]
        if DEBUG:
            circle(p1[0], p1[1], 10)
        if a1 != None and a2 != None:
            start = a1 if a1 < a2 else a1 - TWO_PI
            if r2 <= 0:
                a2 = a2 - TWO_PI
            abs_angle = abs(a2 - start)
            if abs_angle > TWO_PI:
                if a2 < 0:
                    a2 += TWO_PI
                else:
                    a2 -= TWO_PI
            if abs(a2 - start) != TWO_PI:
                arc_func(p2[0], p2[1], r2 * 2, r2 * 2, start, a2, mode=2,
                         **kwargs)
            if DEBUG:
                textSize(height / 30)
                text(str(int(degrees(start - a2))), p2[0], p2[1])
        else:
            # when the the segment is smaller than the diference between
            # radius, circ_circ_tangent won't renturn the angle
            if DEBUG:
                ellipse(p2[0], p2[1], r2 * 2, r2 * 2)
            if a1:
                vertex_func(p12[0], p12[1])
            if a2:
                vertex_func(p21[0], p21[1])
    endShape(CLOSE)
    # check augmented poly aproximation instersection
    if check_intersection:
        return is_poly_self_intersecting(_points)

def reduce_radius(p1, p2, r1, r2):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = abs(r1 - r2)
    if d - ri <= 0:
        if abs(r1) > abs(r2):
            r1 = map(d, ri + 1, 0, r1, r2)
        else:
            r2 = map(d, ri + 1, 0, r2, r1)
    return(r1, r2)

def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = r1 - r2
    line_angle = atan2(p1[0] - p2[0], p2[1] - p1[1])
    if d - abs(ri) >= 0:
        theta = asin(ri / float(d))
        x1 = -cos(line_angle + theta) * r1
        y1 = -sin(line_angle + theta) * r1
        x2 = -cos(line_angle + theta) * r2
        y2 = -sin(line_angle + theta) * r2
        return (line_angle + theta,
                (p1[0] - x1, p1[1] - y1),
                (p2[0] - x2, p2[1] - y2))
    else:
        return (None,
                (p1[0], p1[1]),
                (p2[0], p2[1]))

def bar(x1, y1, x2, y2, thickness, **kwargs):
    """
    Draw a thick strip with rounded ends.
    It can be shorter than the supporting (axial) line segment.

    # 2020-9-25 First rewrite attempt based on var_bar + arc_func + **kwargs
    # 2020-9-26 Let's do everything in var_bar()!
    """
    var_bar(x1, y1, x2, y2, thickness / 2, **kwargs)

def var_bar(p1x, p1y, p2x, p2y, r1, r2=None, **kwargs):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius

    # 2020-9-25 Added **kwargs, now one can use arc_func=p_arc & num_points=N   
    # 2020-9-26 Added treatment to shorter=N so as to incorporate bar() use.
                Added a keyword argument, internal=True is the default,
                internal=False disables drawing internal circles.
                Minor cleanups, and removed "with" for pushMatrix().
    """
    r2 = r2 if r2 is not None else r1
    draw_internal_circles = kwargs.pop('internal', True)
    arc_func = kwargs.pop('arc_func', b_arc)
    shorter = kwargs.pop('shorter', 0)
    assert not (shorter and r1 != r2),\
        "Can't draw shorter var_bar with different radii"
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    if d > abs(ri):
        clipped_ri_over_d = min(1, max(-1, ri / d))
        beta = asin(clipped_ri_over_d) + HALF_PI
        pushMatrix()
        translate(p1x, p1y)
        angle = atan2(p1x - p2x, p2y - p1y)
        rotate(angle + HALF_PI)
        x1 = cos(beta) * r1
        y1 = sin(beta) * r1
        x2 = cos(beta) * r2
        y2 = sin(beta) * r2
        beginShape()
        offset = shorter / 2.0 if shorter < d else d / 2.0
        arc_func(offset, 0, r1 * 2, r1 * 2,
                 -beta - PI, beta - PI, mode=2, **kwargs)
        arc_func(d - offset, 0, r2 * 2, r2 * 2,
                 beta - PI, PI - beta, mode=2, **kwargs)
        endShape(CLOSE)
        popMatrix()
    elif draw_internal_circles:
        arc_func(p1x, p1y, r1 * 2, r1 * 2, 0, TWO_PI, **kwargs)
        arc_func(p2x, p2y, r2 * 2, r2 * 2, 0, TWO_PI, **kwargs)
        
# # PVector is a wrapper/helper class for p5.Vector objets
# from numbers import Number

# class PVector:

#     def __init__(self, x=0, y=0, z=0):
#             self.__vector = createVector(x, y, z)
#             self.add = self.__instance_add__
#             self.sub = self.__instance_sub__
#             self.mult = self.__instance_mult__
#             self.div = self.__instance_div__
#             self.cross = self.__instance_cross__
#             self.dist = self.__instance_dist__
#             self.dot = self.__instance_dot__
#             self.lerp = self.__instance_lerp__

#     @property
#     def x(self):
#         return self.__vector.x
#     @x.setter
#     def x(self, x):
#         self.__vector.x = x
#     @property
#     def y(self):
#         return self.__vector.y
#     @y.setter
#     def y(self, y):
#         self.__vector.y = y
#     @property
#     def z(self):
#         return self.__vector.z
#     @z.setter
#     def z(self, z):
#         self.__vector.z = z

#     def mag(self):
#         return self.__vector.mag()        

#     def magSq(self):
#         return self.__vector.magSq()        

#     def __instance_add__(self, *args):
#         if len(args) == 1:
#             return PVector.add(self, args[0], self)
#         else:
#             return PVector.add(self, PVector(*args), self)

#     def __instance_sub__(self, *args):
#         if len(args) == 1:
#             return PVector.sub(self, args[0], self)
#         else:
#             return PVector.sub(self, PVector(*args), self)
            
#     def __instance_mult__(self, o):
#         return PVector.mult(self, o, self)

#     def __instance_div__(self, f):
#         return PVector.div(self, f, self)

#     def __instance_cross__(self, o):
#         return PVector.cross(self, o, self)

#     def __instance_dist__(self, o):
#         return PVector.dist(self, o)

#     def __instance_dot__(self, *args):
#         if len(args) == 1:
#             v = args[0]
#         else:
#             v = args
#         return self.x * v[0] + self.y * v[1] + self.z * v[2]

#     def __instance_lerp__(self, *args):
#         if len(args) == 2:
#             return PVector.lerp(self, args[0], args[1], self)
#         else:
#             vx, vy, vz, f = args
#             return PVector.lerp(self, PVector(vx, vy, vz), f, self)

#     def get(self):
#         return PVector(self.x, self.y, self.z)

#     def copy(self):
#         return PVector(self.x, self.y, self.z)

#     def __getitem__(self, k):
#         return getattr(self, ('x','y','z')[k])

#     def __setitem__(self, k, v):
#         setattr(self, ('x','y','z')[k], v)

#     def __copy__(self):
#         return PVector(self.x, self.y, self.z)

#     def __deepcopy__(self, memo):
#         return PVector(self.x, self.y, self.z)

#     def __repr__(self):  # PROVISÓRIO
#         return str(self) #f'PVector({self.x}, {self.y}, {self.z})'

#     def set(self, *args):
#         """
#         Sets the x, y, and z component of the vector using two or three separate
#         variables, the data from a p5.Vector, or the values from a float array.
#         """
#         self.__vector.set(*args)

#     @classmethod
#     def add(cls, a, b, dest=None):
#         if dest is None:
#             return PVector(a.x + b[0], a.y + b[1], a.z + b[2])
#         dest.__vector.set(a.x + b[0], a.y + b[1], a.z + b[2])
#         return dest
    
#     @classmethod
#     def sub(cls, a, b, dest=None):
#         if dest is None:
#             return PVector(a.x - b[0], a.y - b[1], a.z - b[2])
#         dest.__vector.set(a.x - b[0], a.y - b[1], a.z - b[2])
#         return dest

#     @classmethod
#     def mult(cls, a, b, dest=None):
#         if dest is None:
#             return PVector(a.x * b, a.y * b, a.z * b)
#         dest.__vector.set(a.x * b, a.y * b, a.z * b)
#         return dest

#     @classmethod
#     def div(cls, a, b, dest=None):
#         if dest is None:
#             return PVector(a.x / b, a.y / b, a.z / b)
#         dest.__vector.set(a.x / b, a.y / b, a.z / b)
#         return dest

#     @classmethod
#     def dist(cls, a, b):
#         return a.__vector.dist(b.__vector)

#     @classmethod
#     def dot(cls, a, b):
#         return a.__vector.dot(b.__vector)

#     def __add__(a, b):
#         return PVector.add(a, b, None)

#     def __sub__(a, b):
#         return PVector.sub(a, b, None)
    
#     def __isub__(a, b):
#         a.sub(b)
#         return a
    
#     def __iadd__(a, b):
#         a.add(b)
#         return a
    
#     def __mul__(a, b):
#         # print("mul")
#         if not isinstance(b, Number):
#             raise TypeError("The * operator can only be used to multiply a PVector by a number")
#         return PVector.mult(a, float(b), None)
    
#     def __rmul__(a, b):
#         if not isinstance(b, Number):
#             raise TypeError("The * operator can only be used to multiply a PVector by a number")
#         return PVector.mult(a, float(b), None)
    
#     def __imul__(a, b):
#         # print("imul")
#         if not isinstance(b, Number):
#             raise TypeError("The *= operator can only be used to multiply a PVector by a number")
#         a.__vector.mult(float(b))
#         return a
    
#     # def __div__(a, b):
#     #     print("div")
#     #     if not isinstance(b, Number):
#     #         raise TypeError("The * operator can only be used to multiply a PVector by a number")
#     #     return PVector(a.x / float(b), a.y / float(b), a.z / float(b))

#     # def __idiv__(a, b):
#     #     print("idiv")
#     #     if not isinstance(b, Number):
#     #         raise TypeError("The /= operator can only be used to multiply a PVector by a number")
#     #     a.__vector.set(a.x / float(b), a.y / float(b), a.z / float(b))
#     #     return a
#     def __div__(a, b):
#         if not isinstance(b, Number):
#             raise TypeError("The / operator can only be used to divide a PVector by a number")
#         return PVector.div(a, float(b), None)
    
#     def __idiv__(a, b):
#         if not isinstance(b, Number):
#             raise TypeError("The /= operator can only be used to divide a PVector by a number")
#         a.div(float(b))
#         return a
    
    
#     def __eq__(a, b):
#         return a.x == b[0] and a.y == b[1] and a.z == b[2]
    
#     def __lt__(a, b):
#         return a.magSq() < b.magSq()
    
#     def __le__(a, b):
#         return a.magSq() <= b.magSq()
    
#     def __gt__(a, b):
#         return a.magSq() > b.magSq()
    
#     def __ge__(a, b):
#         return a.magSq() >= b.magSq()   

#     # Problematic class methods, we would rather use p5.Vector...

#     @classmethod
#     def lerp(cls, a, b, f, dest=None):
#         v = createVector(a.x, a.y, a.z)
#         v.lerp(b.__vector, f)
#         if dest is None:
#             return PVector(v.x, v.y, v.z)
#         dest.set(v.x, v.y, v.z)
#         return dest

#     @classmethod
#     def cross(cls, a, b, dest=None):
#         x = a.y * b[2] - b[1] * a.z
#         y = a.z * b[0] - b[2] * a.x
#         z = a.x * b[1] - b[0] * a.y
#         if dest is None:
#             return PVector(x, y, z)
#         dest.set(x, y, z)
#         return dest

#     @classmethod
#     def fromAngle(cls, angle):
#         return PVector(cos(angle), sin(angle))

#     @classmethod
#     def random2D(cls):
#         return PVector.fromAngle(random(TWO_PI))

#     @classmethod
#     def random3D(cls, dest=None):
#         angle = random(TWO_PI)
#         vz = random(2) - 1
#         mult = sqrt(1 - vz * vz)
#         vx = mult * cos(angle)
#         vy = mult * sin(angle)
#         if dest is None:
#             return PVector(vx, vy, vz)
#         dest.set(vx, vy, vz)
#         return dest 
        
#     @classmethod    
#     def angleBetween(cls, a, b):
#         return acos(a.dot(b) / sqrt(a.magSq() * b.magSq()))

#     # other harmless p5js methods
    
#     def setMag(self, mag):
#         self.__vector.setMag(mag)

#     def normalize(self):
#         self.__vector.normalize()

#     def limit(self, max):
#         self.__vector.limit(max)
        
#     def equals(self, v):
#         return self == v

#     def heading(self):
#         return self.__vector.heading()

#     def heading2D(self):
#         return self.__vector.heading()

#     def rotate(self, angle):
#         self.__vector.rotate(angle)
#         return self
