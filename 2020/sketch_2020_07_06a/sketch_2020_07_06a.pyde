n,s=64,8#;l=long(2**n) #つぶやきProcessing
def setup():noStroke();frameRate(2);size(n*s,n*s);colorMode(3)
def draw():
 clear();f=frameCount
 for x in range(n):
  c=long(abs(-2*f%s+x^s*f%s-x)**7)
  #c=long(abs(-2*f**3%128+x^128*f**2%64-x)**3.5)
  #c=long(abs(-2*f%128+x^4*f%n-x)**7.9)
  for y in range(n):
   b='0'*64+bin(c);fill((c+y)%256,255,255)
   if b[::-1][n-y]=='1':rect(x*s,y*s,s,s)

  print(f, c) 
   


# n,s=64,5;l=2**n
# def setup():

    
