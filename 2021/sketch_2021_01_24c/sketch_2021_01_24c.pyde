
#genuary prompt: 500 lines

points = [] 

def setup():
    size(512, 512, P3D)
    points.append(PVector.random3D() * 128)
    while len(points) < 500:
        p = PVector.random3D() * 128
        if 127 < PVector.dist(p, points[-1]) < 128:
            points.append(p)
     
def draw():
    background(0)
    strokeWeight(2)
    translate(width / 2, height / 2, 128)
    scale(-1)
    rotateY(frameCount / 100.0)
    for i, (xa, ya, za) in enumerate(points):
        xb, yb, zb = points[i - 1]
        stroke(128 + xa, 128 + ya, 128 + za)
        line(xa, ya, za, xb, yb, zb)
     
        
              
    print(int(degrees(frameCount / 100.0)) % 360)
