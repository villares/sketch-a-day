from villares import ubuntu_jogl_fix
step = 10

def setup():
    size(628, 314 + 157, P2D)  
    
def draw():
    background(0)
    translate(0, height / 2) 
    strokeWeight(2)
    for x in range(width):
        a = x / 100.0   
        for y in range(-height, height, step):
            y_cos = cos(a) * 100
            stroke(200, 200, 0)
            point(x, y + y_cos)
            y_sin = sin(a) * 100
            stroke(0, 200, 200)
            point(x, y + y_sin + frameCount % step)
