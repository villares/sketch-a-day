SKETCH_NAME = "s080"
"""
sketch 80 180321 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Based on Recursive Tree by Daniel Shiffman.    
"""

add_library('gifAnimation')
from gif_exporter import gif_export
from slider import Slider

A = Slider(0, HALF_PI, QUARTER_PI)
B = Slider(0, 10, 0)
C = Slider(-2, 2, 0)
D = Slider(2, 10, 10)

def setup():
    size(600, 600, P2D)
    colorMode(HSB)
    noFill()
    A.position(20, height - 60)
    B.position(20, height - 30)
    C.position(width - 180, height - 60)
    D.position(width - 180, height - 30)

def draw():
    global b, c, d
    background(200)
    frameRate(30)

    a = A.value()  # Angle
    b = B.value()  # branch size randomization
    c = C.value()  # angle randomization
    d = D.value()  # recursion depth

    randomSeed(int(d*10))
    translate(width / 2, height / 2)
    branch(int(d), a, width/20 + (width/75)*b)

    # #uncomment next lines to export GIF
    if not frameCount % 10: gif_export(GifMaker,
                                       frames=2000,
                                       filename=SKETCH_NAME)

def branch(gen, theta, branch_size):
    strokeWeight(2)
    # All recursive functions must have an exit condition!!!!
    if gen > 1:# and branch_size > 1:
        with pushMatrix():
            stroke(255 * (gen % 2))
            h = branch_size  * (1 - random(b/3,b) / 15)
            rotate(theta + c * random(1))  # Rotate by theta
            arrow(0, 0, 0, -h, tail_func=ellipse)  # Draw the branch
            translate(0, -h)  # Move to the end of the branch
            # Ok, now call myself to draw two branches!!
            with pushStyle():
                branch(gen - 1, theta, h)
        with pushMatrix():
            stroke(255 * (gen % 2))
            h = branch_size  * (1 - random(b/3, b) / 15)
            rotate(-theta + c * random(1))
            arrow(0, 0, 0, -h, tail_func=ellipse)
            translate(0, -h)
            with pushStyle():
                branch(gen - 1, theta, h)
                
                
def arrow(x1, y1, x2, y2,
          shorter=10,
          head=None,
          tail_func=None,
          tail_size=None):
    """
    O código para fazer as setas, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    """
    rectMode(CENTER)
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 10, 5)
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
