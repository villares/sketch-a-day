
def setup():
 size(600, 600, P3D)
def draw():
 background(0)
 translate(300,300,0)
 for b in range(-90,90,10):
  for a in range(0,360,10):
   push()
   rotateX(radians(b))
   rotateY(radians(a+frameCount/10.))
   translate(0,0,-200)
   circle(0,0,10)
   pop()
