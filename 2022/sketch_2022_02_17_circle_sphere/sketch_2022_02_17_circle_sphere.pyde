r=radians #つぶやきProcessing #Python
def setup():
 size(600,600,P3D)
def draw():
 clear();translate(300,300,0)
 for b in range(0,180,10):
  for a in range(0,360,10):
   push();rotateX(r(b+(a-180)*frameCount/100.));rotateY(r(a+b/10.));translate(0,0,-200);circle(0,0,10);pop()
