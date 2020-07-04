n,s=64,5;l=2**n
def setup():
 noStroke();frameRate(2);size(n*s,n*s);colorMode(3)
def draw():
 clear()
 for i in range(n):
  c=long(-2*frameCount+i^8*frameCount-i)**5%l
  for j in range(n):
   bv='{:064b}'.format(c)
   fill(c%256,255,255)
   if bv[j]=='1':rect(i*s,j*s,s,s)


# n,s=64,5;l=2**n
# def setup():

    
