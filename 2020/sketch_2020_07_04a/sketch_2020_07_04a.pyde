n,s=64,5 #つぶやきProcessing
def setup():
 noStroke();frameRate(2);size(n*s,n*s);colorMode(3)
def draw():
 clear();f=frameCount
 for x in range(n):
  c=long(-2*f+x^8*f-x)**5
  for y in range(n):
   b='{:064b}'.format(c);fill(c%256,255,255)
   if b[y]=='1':rect(x*s,y*s,s,s)


# n,s=64,5;l=2**n
# def setup():

    
