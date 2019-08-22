# based on https://twitter.com/Hau_kun/status/1163867191252410368?s=20

s,p,r=720,[[360]*4 for _ in range(99)],random
def setup():size(s,s);colorMode(HSB)
def draw():
 clear()
 for f in p:
  x,y,z,w=f   
  a,d=atan2(w-y,z-x),dist(*f)/100
  f[2:4]=r(s)if d<1 else z,r(s)if d<1 else w
  f[0:2]=x+cos(a)*d,y+sin(a)*d
  fill(d*50,s,s)
  circle(x,y,10)
 # if frameCount % 3 == 0:
 #  saveFrame("#####.png")
