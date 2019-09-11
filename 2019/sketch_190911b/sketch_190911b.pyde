#つぶやきProcessing
a,b,c=512,256,128
def setup():size(a,a);rectMode(3);frameRate(1);colorMode(3)
def draw():r(b,b,2,a)
def r(x,y,n,t):
 w=t/n
 m=(w-t)/2
 for i in range(n):
  for j in range(n):
   u,v=w*i+m+x,w*j+m+y
   if w>2 and random(10)<8:r(u,v,2,w)
   else:fill(b-w,b,b,c);square(u,v,w)
