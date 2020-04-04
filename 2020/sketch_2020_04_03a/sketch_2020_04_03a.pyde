"""
Bézier Curves Cubic (Interactive)
https://rosettacode.org/wiki/Bitmap/B%C3%A9zier_curves/Cubic#Processing
Processing 3.4
2020-04 Alexandre Villares

Task:

Using the data storage type for raster images and a draw_line function,
draw a cubic bezier curve.
"""

# A working sketch with movable anchor and control points.
# It can be run online :
# https://www.openprocessing.org/sketch/846556/

x = [0] * 4
y = [0] * 4
permitDrag = [False] * 4
 
def setup() :
    size(300, 300)
    smooth()
    # startpoint coordinates
    x[0] = x[1] = 50
    y[0] = 50
    y[1] = y[2] = 150
    x[2] = x[3] = 250
    y[3] = 250
  
def draw() :
    background(255)
    noFill()
    stroke(0, 0, 255)
    bezier(x[1], y[1], x[0], y[0], x[3], y[3], x[2], y[2])
    # the bezier handles
    strokeWeight(1)
    stroke(100)
    line(x[0], y[0], x[1], y[1])
    line(x[2], y[2], x[3], y[3])
    # the anchor and control points
    stroke(0)
    fill(0)
    for i in range(4):
        if i == 0 or i == 3:
            fill(255, 100, 10)
            rectMode(CENTER)
            rect(x[i], y[i], 5, 5)
        else:
            fill(0)
            ellipse(x[i], y[i], 5, 5)
    # permit dragging 
    for i in range(4):
        if permitDrag[i]:
            x[i] = mouseX
            y[i] = mouseY    
 
def mouseReleased () :
    for i in range(4):
        permitDrag[i] = False
    
def mousePressed () :
    for i in range(4):
        if (x[i]-5 <= mouseX <= x[i]+10 and 
            y[i]-5 <= mouseY <= y[i]+10):
            permitDrag[i] = True
        
# hand cursor when over dragging over points
def mouseMoved () :
    cursor(ARROW)
    for i in range(4):
        if (x[i]-5 <= mouseX <= x[i]+10 and 
            y[i]-5 <= mouseY <= y[i]+10):
            cursor(HAND)
