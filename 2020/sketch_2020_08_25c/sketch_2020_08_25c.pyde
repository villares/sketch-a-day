#つぶやきProcessing #Python
w,h = 500,250
def setup():size(w,w)
def draw():
 fill(0,0,200,8)
 rect(0,0,w,w)
 translate(h,h)
 a,k=0,frameCount/12.
 while a<TWO_PI:
  i,j=w+sin(a),h+cos(a)
  n=noise(i,j,k)
  x,y=n*h*sin(a),n*h*cos(a)
  point(x,y)
  a+=.01


# w,h = 500,250
# def setup():
#     size(w,w)
# def draw():
#     fill(0,0,200,8)
#     rect(0,0,w,w)
#     translate(h,h)
#     a,k = 0,sin(frameCount / 12.)
#     while a < TWO_PI:
#         i,j = w + sin(a),h + cos(a)
#         n = noise(i,j,k)
#         x,y = n * h * sin(a),n * h * cos(a)
#         point(x,y)
#         a += .01
