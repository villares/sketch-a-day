D=500
def setup():
 size(D,D,P3D)
 smooth(4)
 strokeWeight(1.5)

def draw():
 background(200)
 randomSeed(1)
 translate(H,H,-D)
 rotateX(frameCount/12.0)
 translate(-H,-H,0)
 stroke(0)    
 for x in range(D):
  for y in range(D):
   if dist(x,y,H,H)>random(D*100):
    line(x,y,-H,x,y,H)
