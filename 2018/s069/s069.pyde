"""
sketch 69 180310 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
from __future__ import division
from slider import Slider

# slider_object = Slider(lowest, highest, initial value)
i = Slider(PI / 6, TWO_PI / 3, QUARTER_PI) # angle, changes number of sides
j = Slider(1, 4, 2) # depth, changes number of recursions (fiddled afterwards)
k = Slider(10, 50, 25) # offset, changes scale
l = Slider(0, TWO_PI, 0) # rotation

I, J, K, L = 1, 1, 1, 1 # dummy initial slider global values
# ^ I need these globals because I want to read/draw sliders 
#   at the end of the draw loop so they draw on top
#   I should 'decouple' reading and drawing the sliders... 

def setup():
    size(600, 600)
    colorMode(HSB) # makes it easy to cycle colors through Hues...
    noFill()
    # Position Sliders (x, y)
    i.position(20, 20)
    j.position(20, 60)
    k.position(20, 100)
    l.position(20, 140)

def draw():
    global I, J, K, L
    background(0)
    poly_shape(width / 2, height/2, I, J, K, L)
    # Read and update sliders
    I = i.value()  # from PI/6 to TWO_PI/3
    j.high = 3 + I * 1.5 # change J's upper limit...
    J = j.value()  # 1 to 3 + I * 1.5 
    K = k.value()  # 10 to 50
    L = l.value()  # 0 to TWO_PI
    # uncomment the next line to save frames!
    #if not frameCount % 100: saveFrame("s####.tga") 

def poly_shape(x, y, angle, D, offset, rotation):
    stroke((frameCount / 2 * D) % 256, 255, 255, 255)
    strokeWeight(D)
    with pushMatrix():
        translate(x, y)
        rotate(rotation) 
        radius = D * offset
        # create a polygon on a ps PShape object
        ps = createShape()
        ps.beginShape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx, sy)
            a += angle
        ps.endShape(CLOSE)  # end of PShape creation
        shape(ps, 0, 0) # Draw the PShape
        if D > 1:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.getVertexCount()):
                # for each vertex
                pv = ps.getVertex(i)  # gets vertex as a PVector
                # recusively call poly_shape with a smaller D
                poly_shape(pv.x, pv.y, angle, D - 1, offset, rotation)