add_library('gifAnimation')
from gif_animation_helper import gif_export

#つぶやきProcessing
w,h=500,250
def setup():size(w,w)
def draw():
 background(h,h/2,h);translate(h,h)
 a,k=0,sin(frameCount/30.)
 while a<TWO_PI:
  i,j=sin(a),cos(a)
  n=h*noise((abs(i)+i+j),(abs(j)+j+i),k)
  line(n*sin(a)-n/6,n*cos(a)-n/6,n*sin(a)+n/6,n*cos(a)+n/6)
  a+=.004

 if frameCount/30. < TWO_PI:
    gif_export(GifMaker, filename="c")
 else:
    gif_export(GifMaker, finish=True)
