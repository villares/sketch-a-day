S=600
def n(f,x,y):
 return 18*noise(x*.01,y*.01,f*.01)
def setup():
 size(S,S)
 color_mode(2)
def draw():
 clear()
 x,f=0,frame_count
 while x<S:
  y=0
  while y<S+8:
   h=n(f,x,y+f)
   fill(h*16,255,255);ellipse(x,y,min(8,h),min(8,h));y+=h
  x+=8 #つぶやきProcessing #py5