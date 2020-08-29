s=sqrt(5)/2+.5#つぶやきProcessing
w,h=400,200
def setup():size(w,w); noStroke();colorMode(3)
def draw():
 clear()    
 r = 1
 for i in range(3000):
  fill(int(i*.1+frameCount)%256,255,255,100)
  a=i*s
  x=h+r*cos(a)
  y=h+r*sin(a)
  square(x,y,r/10)
  r+=0.1
