"""
ImageNoise
https://rosettacode.org/wiki/Image_noise#Processing
Processing 3.4
2019-08 Jeremy Douglass
2020-03-15 Alexandre Villares (Python Mode)

Task: Generate a random black and white 320x240 image continuously, showing FPS
(frames per second).
"""

black = color(0)
white = color(255)

def setup():
    size(320, 240)
    # frameRate(30) # 60 by default


def draw():
    loadPixels()
    for i in range(len(pixels)):
        if random(1) < 0.5:
            pixels[i] = black
        else:
            pixels[i] = white

    updatePixels()
    fill(0, 128)
    rect(0, 0, 60, 20)
    fill(255)
    text(frameRate, 5, 15)
    
def keyPressed():
    from os import path
    sketch = sketchPath()
    name = path.basename(sketch)
    print(name)
    saveFrame(name + '.png')
