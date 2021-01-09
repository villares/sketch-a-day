from villares import ubuntu_jogl_fix
from villares.gif_export import gif_export
add_library('gifAnimation')

step = 10

def setup():
    size(628, 314, P2D)  
    
def draw():
    background(0)
    translate(0, height / 2) 
    strokeWeight(2)
  
    for y in range(-height, height, step):
        for x in range(0, width):
            a = x / 100.0 
            a_sin = sin(a) * 100
            stroke(200, 200, 0)
            point(x, y + a_sin)
            b = (x + frameCount) / 100.0 
            b_sin = sin(b) * 100
            stroke(0, 200, 200)
            point(x, y + b_sin )
            
    if frameCount < width and frameCount % 2:
        gif_export(GifMaker, "output")
    elif frameCount == width:
        gif_export(GifMaker,  finish=True)
            
