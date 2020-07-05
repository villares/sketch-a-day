n,s=64,8 #つぶやきProcessing
def setup():
 frameRate(2);size(n*s,n*s);colorMode(3)
def draw():
 clear();f=frameCount
 for x in range(n):
  c=long(abs(-2*f%n+x^4*f%n-x)**7.5)
  for y in range(n):
   b='{:064b}'.format(c);fill((c+y)%256,255,255)
   if b[y]=='1':rect(x*s,y*s,s,s)

# print(f)
#;l=long(2**n)
# n,s=64,5;l=2**n
# def setup():

    
