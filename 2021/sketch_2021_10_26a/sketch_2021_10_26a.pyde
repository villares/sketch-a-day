
D = 500
H = 250

def setup():
    size(D, D, P3D)
    smooth(4)
    strokeWeight(1.5)

def draw():
    background(200)
    randomSeed(1)
    translate(250, 250, -D)
    rotateX(frameCount / 12.0)
    translate(-250, -250, 0)
    stroke(0)    
    for x in range(width):
        for y in range(height):
            if y > random(D * 50):
                stroke(y / 2)
                line(x, y, -250, x, y, sqrt(x * y) - 250)    

#つぶやきProcessing
D,H=500,250
def setup():size(D,D,P3D);smooth(4);strokeWeight(1.5)
def draw():background(200); randomSeed(1);translate(H,H,-D);rotateX(frameCount/12.0);translate(-H,-H,0);[stroke(y/2)or line(x,y,-H,x,y,sqrt(x*y)-H)for x in range(D)for y in range(D)if y>random(D*50)]
