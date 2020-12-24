# https://twitter.com/ntsutae/status/1337921503552102400?s=20
# x=y=0
t,w,i=0,512,int#つぶやきProcessing
def setup():size(w,w);noStroke()
def draw():
 clear()
 for y in range(0,w,8):
  for x in range(0,w,8):
   a=frameCount/120.-float(x+y)/w/1.4;T=tan(a)**2;R=0|i(tan(i(x/6.)&i(y/6.)|i(a))*8);fill("#"+hex(R*2**6,6));rect(x+cos(R)*T,y+sin(R)*T,8,8)



# # https://twitter.com/ntsutae/status/1337921503552102400?s=20
# t,w,i=0,640,int#つぶやきProcessing
# def setup():size(w,w);noStroke()
# def draw():
#  clear()
#  for y in range(0,w,16):
#   for x in range(0,w,16):
#    a=frameCount/120.0-float(x+y)/w/1.4;T=tan(a)**3;R=0|i(tan(i(x/12.0)&i(y/12.0)|i(a))*8);fill("#"+hex(R*2**12,6));rect(x+cos(R*11)*T,y+sin(R)*T,16,16)
