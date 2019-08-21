# based on https://twitter.com/Hau_kun/status/1163867191252410368?s=20

p,s=[[0]*4 for _ in range(99)],720
def setup():size(s,s);colorMode(HSB)
def draw():
 clear()
 for f in p:
  x,y,z,w=f   
  a,d,r=atan2(w-y,z-x),dist(*f)/100,random
  f[2:4]=[r(s)if d<1 else z,r(s)if d<1 else w]
  f[0]+=cos(a)*d
  f[1]+=sin(a)*d
  fill(d*50,s,s)
  circle(x,y,10)
