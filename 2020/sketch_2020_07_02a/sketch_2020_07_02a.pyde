n,s,t=64,5,0
def setup():
 noStroke()
 frameRate(2)
 size(320, 320)
 colorMode(HSB)
def draw():
 clear()
 for x in range(n):
  for y in range(n):
   c=frameCount**y
   bv='{:064b}'.format(c)
   fill(c%255,255,255)
   if bv[x]=='1':rect(x*s,y*s,s,s)

    
