def n(x,y=0):
 return 34*noise(x*0.03,y*0.03,frame_count*0.002)
def setup():
 size(600,600)
 color_mode(HSB)
def draw():
 x,W,H=0,width,height
 while x<W:
  w=n(x)
  y=0
  while y<H:
   h=n(x,y)
   fill(w*8,256-h*6,200);rect(x,y,w,h);y+=h
  x+=w #つぶやきProcessing #py5