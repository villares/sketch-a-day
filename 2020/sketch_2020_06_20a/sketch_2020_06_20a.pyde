t=0;w=690#つぶやきProcessing d'aprés@ntsutae
def setup():
 global i
 i = loadImage("convite.png")
 size(w,w)
def draw():
 global t;t+=1;scale(3);background(0);stroke(-1)
 for y in range(240):
  for x in range(240):
   (t+abs((x+y-t)^(x-y+t))**3)%1023<109 and point(x,y)
 image(i, 0, 0, 690/3, 690/3)
