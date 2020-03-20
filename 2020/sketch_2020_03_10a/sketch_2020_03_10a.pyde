"""
 * Dragon Curve https://www.rosettacode.org/wiki/Dragon_curve#Processing
 2020-02 Noel
 * Task: Create and display a dragon curve fractal.
 * https://en.wikipedia.org/wiki/Dragon_curve
 * (You may either display the curve directly or write it to an image file.)
 * For some brief notes the algorithms used and how they might suit various languages,
 * see the Rosetta Code task page.
"""

l = 3
ints = 13

def setup():
  size(700, 600)
  background(0, 0, 255)
  translate(150, 100)
  stroke(255)
  turn_left(l, ints)
  turn_right(l, ints)
  save_image()

def turn_right(l, ints):
    if ints == 0:
        line(0, 0, 0, -l)
        translate(0, -l)
    else:
        turn_left(l, ints - 1)
        rotate(radians(90))
        turn_right(l, ints - 1)
  
def turn_left(l, ints):
    if ints == 0:
        line(0, 0, 0, -l)
        translate(0, -l)
    else:
        turn_left(l, ints - 1)
        rotate(radians(-90))
        turn_right(l, ints - 1)
        
        
def save_image():
    from os import path
    sketch = sketchPath()
    name = path.basename(sketch)
    print(name)
    saveFrame(name + '.png')
