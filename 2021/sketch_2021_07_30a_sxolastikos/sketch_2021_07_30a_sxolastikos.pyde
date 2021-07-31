# zadgy5534 @sxolastikos https://twitter.com/sxolastikos/status/1421277279456350208
t=0#つぶやきProcessing
w=400
def setup():size(w,w)
def draw():
 global t
 background(220)
 t+=0.01
 i = 0
 while i<TAU:
  beginShape(QUADS)
  n=cos(i*t)*9
  stroke(n,99,99);
  for j in range(8):
   vertex(200+j%w*n,200+j%w*sin(i-t)*19)
  endShape()
  i+=PI/32
