def n(f,x,y=0):
 return 18*noise(x*.01,y*.01,f*.01)
def setup():
 size(600,600)
 color_mode(HSB)
def draw():
 x,W,H,f=0,width,height,frame_count
 while x<W:
  w=n(f,x-f)
  y=0
  while y<H:
   h=n(f,x+f,y+f)
   fill(h*16,255,w*18);rect(x,y,w,h);y+=h
  x+=w #つぶやきProcessing #py5