class Cube :
  ax = 0
  ay = 0

  def __init__(self, id,  size_,  x,  y, c) :
    self.id = id
    self.size = size_
    self.x = x
    self.y = y
    self.c = c
  

  def rotate(self, x,  y) :
    self.ax += x
    self.ay += y
  

  def draw(self) :
    fill(self.c)
    pushMatrix()
    translate(self.x, self.y)
    rotateX(self.ay)
    rotateY(-self.ax)
    box(self.size)
    popMatrix()
  
