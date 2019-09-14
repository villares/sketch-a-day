#つぶやきProcessing
a,b,c=512,256,128
def setup():size(a,a);rectMode(3);frameRate(1);colorMode(3)
def draw():clear();r(b,b,a)
def r(x,y,t):
 w=t/2
 m=(w-t)/2
 for i in range(2):
  for j in range(2):
   u,v=w*i+m+x,w*j+m+y
   if w>2 and random(10)<8:r(u,v,w)
   else:fill(b-w,b,b);circle(u,v,w)
