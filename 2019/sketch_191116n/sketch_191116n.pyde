#つぶやきProcessing
d,s,m=12,512,255
def setup():size(s,s);clear();stroke(m)
def draw():
 f=frameCount
 for _ in range(d):
  translate(m,m)
  rotate(TWO_PI/d)
  translate(-m,-m)
  n = noise(f*0.01)
  point(f%s,n*s)

def keyPressed():
 if key == ' ':
  clear()
 if key == 's':
  saveFrame("###.png")
