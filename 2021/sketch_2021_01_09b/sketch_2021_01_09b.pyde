from villares import ubuntu_jogl_fix
step = 10

def setup():
    size(628, 314 + 157, P2D)  
    
def draw():
    background(0)
    translate(0, height / 2) 
    strokeWeight(2)
  
    for y in range(-height, height, step):
        for x in range(0, width):
            a = x / 100.0 
            y_sin = sin(a) * 100
            stroke(200, 200, 0)
            point(x, y + y_sin)
        for x in range(-width, width):
            a = x / 100.0 
            y_sin = sin(a) * 100
            stroke(0, 200, 200)
            point(x + frameCount % width, y + y_sin )
