

n,m,s=64,255,8 #つぶやきProcessing
def setup():size(n*s,n*s);frameRate(1);colorMode(3);clear()
def draw():
 for x in range(n):
  f=frameCount;c=long(abs(-s*f%n+x^2*f%n-x)**7)
  for y in range(n):fill((c+y)%m,m,m)if format(c,'064b')[y]=='1'else fill(c%m,m,n);circle(x*s,y*s,s)
 # print(f, c)   
