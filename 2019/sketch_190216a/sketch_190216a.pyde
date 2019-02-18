p_list = [PVector(100, 400, 50),
          PVector(300, 100, 100),]
radius = 30

def setup():
  size(500, 500)

def draw():
    background(200)
    p_list.append(PVector(mouseX, mouseY, radius))   
    for p0, p1, p2 in zip(p_list,
                          [p_list[-1]]+ p_list[:-1],
                          [p_list[-2]]+ [p_list[-1]]+ p_list[:-2]):
        m1 = (p0 + p1)/2
        m2 = (p1+ p2)/2
        strokeWeight(1)
        stroke(0)
        line(p1.x, p1.y, m1.x, m1.y)
        line(p1.x, p1.y, m2.x, m2.y)
        stroke(255)
        strokeWeight(3)
        roundedCorner(p1, m1, m2, p1.z)    
    p_list.pop()

    
def roundedCorner(pc, p1, p2, r):
    """
    Based on Stackoverflow C# rounded corner post 
    https://stackoverflow.com/questions/24771828/algorithm-for-creating-rounded-corners-in-a-polygon
    """
     #Vector 1
    dx1 = pc.x - p1.x
    dy1 = pc.y - p1.y

    #Vector 2
    dx2 = pc.x - p2.x
    dy2 = pc.y - p2.y

    #Angle between vector 1 and vector 2 divided by 2
    angle = (atan2(dy1, dx1) - atan2(dy2, dx2)) / 2

    # The length of segment between angular point and the
    # points of intersection with the circle of a given radius
    tng = abs(tan(angle))
    segment = r / tng if tng !=0 else r

    #Check the segment
    length1 = GetLength(dx1, dy1)
    length2 = GetLength(dx2, dy2)

    min_len = min(length1, length2)

    if segment > min_len:
        segment = min_len
        r = min_len * abs(tan(angle))
    

    # Points of intersection are calculated by the proportion between 
    # the coordinates of the vector, length of vector and the length of the segment.
    p1Cross = GetProportionPoint(pc, segment, length1, dx1, dy1)
    p2Cross = GetProportionPoint(pc, segment, length2, dx2, dy2)

    # Calculation of the coordinates of the circle 
    # center by the addition of angular vectors.
    dx = pc.x * 2 - p1Cross.x - p2Cross.x
    dy = pc.y * 2 - p1Cross.y - p2Cross.y

    L = GetLength(dx, dy)
    d = GetLength(segment, r)

    circlePoint = GetProportionPoint(pc, d, L, dx, dy)

    #StartAngle and EndAngle of arc
    startAngle = atan2(p1Cross.y - circlePoint.y, p1Cross.x - circlePoint.x)
    endAngle = atan2(p2Cross.y - circlePoint.y, p2Cross.x - circlePoint.x)

    #Sweep angle
    sweepAngle = endAngle - startAngle

    #Some additional checks
    if sweepAngle < 0:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle
    
    if sweepAngle > PI:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = TWO_PI - sweepAngle

    #Draw result using graphics
    noFill()
    line(p1.x, p1.y, p1Cross.x, p1Cross.y)
    line(p2.x, p2.y, p2Cross.x, p2Cross.y)
    arc(circlePoint.x, circlePoint.y, 2 * r, 2 * r, 
        startAngle, startAngle + sweepAngle)
    fill(0, 0, 100)
    text(str(int(r))+"  "+str(int(pc.z))
         , circlePoint.x, circlePoint.y )

def GetLength(dx, dy):
    return sqrt(dx * dx + dy * dy)


def GetProportionPoint(pt, segment, L, dx, dy):
    # factor = segment / L if L != 0 else 0
    factor = float(segment) / L if L != 0 else segment
    return PVector(
        (pt.x - dx * factor), 
        (pt.y - dy * factor))
    
def mousePressed():
    if mouseButton == LEFT:
        p_list.append(PVector(mouseX, mouseY, radius))
    elif len(p_list) > 2:
        p_list.pop()
        
def mouseWheel(e):
    global radius
    radius += int(e.getAmount())
