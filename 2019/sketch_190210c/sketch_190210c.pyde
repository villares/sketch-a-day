def setup():
  size(500, 500)

def draw():
  background(200)
  p1 = PVector(100, 400)
  p0 = PVector(300, 100)
  p2 = PVector(mouseX, mouseY)
  r1 = 50
  r2 = 40
  r0 = 30
  stroke(0)
  roundedCorner(p0, p2, p1, r0)
  stroke(255)
  roundedCorner(p1, p2, p1, r1)
  stroke(128)
  roundedCorner(p2, p1, p0, r2)

def roundedCorner(angularPoint, p1, p2, radius):
    """
    Based on Stackoverflow C# rounded corner post 
    https://stackoverflow.com/questions/24771828/algorithm-for-creating-rounded-corners-in-a-polygon
    """
    #Vector 1
    dx1 = angularPoint.x - p1.x
    dy1 = angularPoint.y - p1.y

    #Vector 2
    dx2 = angularPoint.x - p2.x
    dy2 = angularPoint.y - p2.y

    #Angle between vector 1 and vector 2 divided by 2
    angle = (atan2(dy1, dx1) - atan2(dy2, dx2)) / 2

    # The length of segment between angular poand the
    # points of intersection with the circle of a given radius
    t = abs(tan(angle))
    if t != 0:
        segment = radius / t
    else:
        segment = 1

    #Check the segment
    length1 = GetLength(dx1, dy1)
    length2 = GetLength(dx2, dy2)

    length = min(length1, length2)

    if segment > length:
        segment = length
        radius = length * t
    

    # Points of intersection are calculated by the proportion between 
    # the coordinates of the vector, length of vector and the length of the segment.
    p1Cross = GetProportionPoint(angularPoint, segment, length1, dx1, dy1)
    p2Cross = GetProportionPoint(angularPoint, segment, length2, dx2, dy2)

    # Calculation of the coordinates of the circle 
    # center by the addition of angular vectors.
    dx = angularPoint.x * 2 - p1Cross.x - p2Cross.x
    dy = angularPoint.y * 2 - p1Cross.y - p2Cross.y

    L = GetLength(dx, dy)
    d = GetLength(segment, radius)

    circlePoint = GetProportionPoint(angularPoint, d, L, dx, dy)

    #StartAngle and EndAngle of arc
    startAngle = atan2(p1Cross.y - circlePoint.y,
                       p1Cross.x - circlePoint.x)
    endAngle = atan2(p2Cross.y - circlePoint.y,
                     p2Cross.x - circlePoint.x)

    #Sweep angle
    sweepAngle = endAngle - startAngle

    #Some additional checks
    if sweepAngle < 0:
        startAngle = endAngle
        sweepAngle = -sweepAngle
    
    if sweepAngle > PI:
        sweepAngle = PI - sweepAngle

    #Draw result using graphics
    noFill()
    strokeWeight(3)
    # return ((p1.x, p1.y, p1Cross.x, p1Cross.y),
    #        (p2.x, p2.y, p2Cross.x, p2Cross.y),
    #        (circlePoint.x, circlePoint.y, 2 * radius, 2 * radius, 
    #        startAngle, startAngle + sweepAngle)
           # )
    line(p1.x, p1.y, p1Cross.x, p1Cross.y)
    line(p2.x, p2.y, p2Cross.x, p2Cross.y)
    arc(circlePoint.x, circlePoint.y, 2 * radius, 2 * radius, 
        startAngle, startAngle + sweepAngle)

def GetLength(dx, dy):
    return sqrt(dx * dx + dy * dy)

def GetProportionPoint(pt, segment, L, dx, dy):
    if L != 0:
        factor = segment / L
    else:
        factor = 0
    
    return PVector(
        (pt.x - dx * factor), 
        (pt.y - dy * factor))
