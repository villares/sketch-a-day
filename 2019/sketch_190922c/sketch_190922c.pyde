#つぶやきProcessing
w,h=500,250
def setup():size(w,w)
def draw():
 background(h/2,h/2,h);translate(h,h)
 a,k=0,sin(frameCount/30.)
 while a<TWO_PI:
  i,j=sin(a),cos(a)
  n=noise((abs(i)+i+j),(abs(j)+j+i),k)
  x,y=n*h*sin(a),n*h*cos(a)
  line(0,0,x,y)
  a+=.004
 # if frameCount/30. < TWO_PI:
 #      saveFrame("####.png")
