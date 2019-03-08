"""
sketch 73 180314 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

from __future__ import division
from slider import Slider
add_library('gifAnimation')
from gif_exporter import gif_export

I = HALF_PI  # initial angle
J = 2  # initial depth
K = 50  # initial scale
L = 0  # initial rotation
# slider_object = Slider(lowest, highest, initial value)
i = Slider(PI / 6, TWO_PI / 3, I)  # angle, changes number of sides
j = Slider(1, 4, J)  # depth, changes number of recursions
k = Slider(10, 100, K)  # scale
l = Slider(0, TWO_PI, L)  # rotation

def setup():
    size(600, 600)
    colorMode(HSB)  # makes it easy to cycle colors through Hues...
    noFill()
    # Position Sliders (x, y)
    i.position(20, 20)
    j.position(20, 60)
    k.position(20, 100)
    l.position(20, 140)
    frameRate(10)

def draw():
    global I, J, K, L
    background(200)
    poly_shape(width / 2, height / 2, J)
    # Read and update sliders
    I = i.value()  # angle: from PI/6 to TWO_PI/3.
    J = j.value()  # D: 1 to 3
    K = k.value()  # Scale: 10 to 50
    L = l.value()  # rotation: 0 to TWO_PI
    # uncomment the next line to save frames!
    if not frameCount % 10: gif_export(GifMaker, frames=3000)


def poly_shape(x, y, D):
    with pushMatrix():
        translate(x, y)
        rotate(L)
        radius = D * K  # D * scale
        # create a polygon on a ps PShape object
        ps = createShape()
        ps.beginShape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx, sy)
            a += I  # angle
            ps.strokeWeight(D * 5)
            ps.stroke(int(D * 255) % 256, 255, 255)
        ps.endShape(CLOSE)  # end of PShape creation
        shape(ps, 0, 0, D * 10, D * 10)  # Draw the PShape, but scaled down
        if D > 1:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.getVertexCount()):
                # for each vertex
                pv = ps.getVertex(i)  # gets vertex as a PVector
                if int(D * 255) % 2:
                    stroke(0)
                else:
                    stroke(255)
                strokeWeight(D)
                arrow(0, 0, pv.x, pv.y,
                      shorter=D * 10)
                # recusively call poly_shape with a smaller D
                poly_shape(pv.x, pv.y, D * .66)


def arrow(x1, y1, x2, y2, shorter=0, head=None,
          tail_func=None, tail_size=None):
    """
    O código para fazer as setas, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    """
    rectMode(CENTER)
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 10, 10)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        strokeCap(ROUND)
        line(0, L - offset, -head / 3, L - offset - head)
        line(0, L - offset, head / 3, L - offset - head)
        strokeCap(SQUARE)
        line(0, offset, 0, L - offset)

        if tail_func:
            if not tail_size:
                tail_size = head
            tail_func(0, 0, tail_size, tail_size)
