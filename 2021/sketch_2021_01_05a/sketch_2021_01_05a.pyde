w,t,m,r,c=512,360,16,range,lambda i:(m-8*(i%2))*sin(radians(i))
def setup():size(w,w)
def draw():clear();[[(push(),translate(m+x*32,m+y*32),beginShape(),
[vertex(c(i),c(i+90))for i in r(1,t,5*int(1+t*noise(frameCount*.001,x,y)%5))],endShape(2),pop())
for x in r(m)]for y in r(m)]
