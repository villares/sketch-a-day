add_library('GifAnimation')
from gif_animation_helper import gif_export

sketch_name = 'sketch_2020_05_06a'

def setup():
    size(400, 400)
    # strokeWeight(2)
    
def draw():
    translate(10, 10)
    z = frameCount
    background(0, 0, 200)
    s = 0.003
        
    for x in range(width):
        for y in range(0, height, 20):
            nz = 20 * noise((10 * mouseX + x) * s,
                            (10 * mouseY + y) * s, z * s)
            if x % 20 == 0:
               noStroke()
               ellipse(x, y, nz, nz)

    for x in range(-10, width):
        n = noise((10 * mouseX + x) * s, 10 * mouseY * s, z * s)
        ny = height - n * height
        stroke(0)
        strokeWeight(5)
        point(x, ny)    
        
    if frameCount % 2:
        gif_export(GifMaker, sketch_name)

def keyPressed():
    if key == 'q':
        gif_export(GifMaker, "animation", finish=True)
