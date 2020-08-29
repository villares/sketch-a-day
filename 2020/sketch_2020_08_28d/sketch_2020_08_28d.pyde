#つぶやきProcessing
s,w,h=0.1,400,200
def setup():size(w,w);noStroke();colorMode(HSB);strokeWeight(3);blendMode(2)
def draw():
 global s;clear();r=1
 for i in range(7*w):
  fill(int(r*100)%256,255,255,100);a=i*s;x=h+r*cos(a);y=h+r*sin(a);circle(x,y,r/10);r+=0.1
 s+=0.0001

# s = 0.1
# def setup():
#     size(400, 400)
#     noStroke()
#     colorMode(HSB)
#     blendMode(ADD)

# def draw():
#     global s
#     clear()
#     xo, yo = 200, 200
#     r = 1
#     for i in range(2800):
#         fill(int(r * 100) % 256, 255, 255, 100)
#         a = i * s
#         x = xo + r * cos(a)
#         y = yo + r * sin(a)
#         circle(x, y, r / 10)
#         r += 0.1
#     s += 0.0001
