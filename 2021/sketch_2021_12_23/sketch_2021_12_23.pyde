R = 300

def setup():
  size(800, 800, P3D)
  strokeWeight(2)
  noFill()
  hint(ENABLE_STROKE_PERSPECTIVE)
  
def draw():
  background(240)
  translate(width / 2, height / 2)
  f = radians(frameCount)
  rotateY(f / 4)
  beginShape()
  for da in range(360 * 10):
    a = radians(da / float(10) )
    db = 90 * cos(a * 20 + f)
    b = radians(db)
    x = R * sin(a) * cos(b)
    y = R * sin(a) * sin(b)
    z = R * cos(a)
    vertex(x, y, z)
  endShape(CLOSE)
  # if frameCount <= 760:
  #     saveFrame('###.tga')
  # else: exit()
