r=radians #つぶやきProcessing #Python
def setup():size(600,600,P3D)
def draw():
 clear();translate(300,300);f=frameCount/10.
 for b in range(0,180,10):
  for a in range(0,360,10):push();rotateY(r(b+f));rotateX(r(a+b*f));translate(0,0,-200);fill(a%255,b,200);circle(0,0,10);pop()
