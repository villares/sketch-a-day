S=600
def setup():
 size(S,S)
 color_mode(3)
def draw():
 background(0)
 x,f=0,frame_count
 while x<S:
  y=0
  while y<S+8:
   h=18*noise(x*.01,(y+f)*.01,f*.01)
   fill(h*16,255,255);ellipse(x,y,min(8,h),min(8,h));y+=h
  x+=8 #つぶやきProcessing #py5