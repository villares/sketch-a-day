# w,q=512,128
# p=[PVector.random3D()*q for _ in range(w*2)]
# def setup():size(w,w,P3D)#つぶやきProcessing
# def draw():#Python
#  background(q);strokeWeight(5);translate(w/2,w/2,q);scale(-1)
#  for x,y,z in p:push();c=q+x,q+y,q+z;stroke(*c);rotateY(frameCount/(sum(c)/3));point(x,y,z);pop()
 
points = [] #つぶやきProcessing #Python

def setup():
    size(512, 512, P3D)
    points[:] = [PVector.random3D() * 128
                 for _ in range(1024)]
     
def draw():
    background(128)
    strokeWeight(5)
    translate(width / 2, height / 2, 128)
    scale(-1)
    for x, y, z in points:
        pushMatrix()
        c = color(128 + x, 128 + y, 128 + z)
        stroke(c)
        rotateY(frameCount / brightness(c))
        point(x, y, z)
        popMatrix()
        
        
