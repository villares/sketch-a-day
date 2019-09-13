#つぶやきProcessing
a,b,c=512,256,128
def setup():size(a,a);rectMode(3);frameRate(.5);colorMode(3);noFill()
def draw():clear();r(b,b,a)
def r(x,y,t):
 w,h=t/2,t/4
 for i in range(2):
  for j in range(2):
   u,v=w*i-h+x,w*j-h+y
   if w>8 and random(10)<8:r(u,v,w)
   else:stroke(random(b),b,b);line(u-h,v-h,u+h,v+h)
def keyPressed():
    saveFrame("a.png")
