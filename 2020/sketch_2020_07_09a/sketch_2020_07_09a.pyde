n,m,s=128,255,4 #つぶやきProcessing
def setup():size(n*s,n*s);frameRate(10);colorMode(3)
def draw():
 clear();f=32+frameCount%m;noStroke()
 for x in range(n):
  for y in range(n):
   c=long(abs((f-y-x)^(y-x))**(f/3.));fill(c%m,m,m);format(c,'0256b')[y]=='1'and square(x*s,y*s,s)

# print(f, c)   

# c=long(abs((f-y-x)^(f+y-x))**f)
