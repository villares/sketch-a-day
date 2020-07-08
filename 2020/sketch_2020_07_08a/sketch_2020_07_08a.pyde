

n,m,s=64,255,8 #つぶやきProcessing
def setup():size(n*s,n*s);frameRate(1);colorMode(3)
def draw():
 clear();f=frameCount
 for x in range(n):
  c=long(abs(-4*f%n+x^n*f%n-x)**9.9)
  for y in range(n):
   if format(c,'064b')[y]=='1':fill((y+c)%m,m,m);square(x*s,y*s,s*2)
 # print(f, c)   
