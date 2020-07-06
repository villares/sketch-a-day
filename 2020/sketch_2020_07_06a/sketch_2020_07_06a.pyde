

n,m,s=64,255,8 #つぶやきProcessing
def setup():size(n*s,n*s);frameRate(1);colorMode(3)
def draw():
 clear();f=frameCount;noStroke()
 for x in range(n):
  c=long(abs(-s*f%n+x^4*f%n-x)**7.9)
  
  for y in range(n):fill((c+y)%m,m,m);format(c,'064b')[y]=='1'and square(x*s,y*s,s*2)
  # for y in range(n):fill((c+y)%m,m,m);bin(c)[2:].zfill(n)[y]=='1'and square(x*s,y*s,s*2)
  # for y in range(n):b=bin(c)[2:].zfill(64);fill((c+y)%m,m,m);b[y]=='1'and square(x*s,y*s,s*2)

# n,s=64,8#;l=long(2**n) #つぶやきProcessing
# def setup():frameRate(2);size(n*s,n*s);colorMode(3)
# def draw():
#  clear();f=frameCount
#  for x in range(n):
#   # c=long(abs(-2*f%s+x^s*f%s-x)**7)
#   #c=long(abs(-2*f**3%128+x^128*f**2%64-x)**3.5)
#   c=long(abs(-2*f%n+x^4*f%n-x)**7.9)
#   for y in range(n):
#    b='0'*64+bin(c);fill((c+y)%192,255,255)
#    if b[::-1][n-y]=='1':square(x*s,y*s,s*2)  
#  print(f, c) 
