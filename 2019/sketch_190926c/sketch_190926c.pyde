add_library('gifAnimation')
from gif_animation_helper import gif_export

#つぶやきProcessing
w,h=500,250
def setup():size(w,w);noFill()#;stroke(0,64)
def draw():
 background(h,h,h/2);translate(h,h)
 a,z=0,sin(frameCount/30.)
 while a<TWO_PI:
  x,y=sin(a),cos(a)
  n=h*noise((abs(x)+x+y),(abs(y)+y+x),z)
  ellipse(n*x,n*y,n*x/3,n*y/3)
  a+=.02

 if frameCount/30. < TWO_PI:
    gif_export(GifMaker, filename="c")
 else:
    gif_export(GifMaker, finish=True)
