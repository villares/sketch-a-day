from java.lang import System 
System.setProperty("jogl.disable.openglcore", "false") 


"""
From a talk by Hamish Campbell
https://pyvideo.org/kiwi-pycon-2013/polycubes-an-exploration-in-problem-solving-w.html
"""

from polycube import Polycube

w = 10
N = 6

def setup():
    global sorted_polycubes
    size(800, 650, P3D)
    
    polycubes = generate_polycubes(N)
    sorted_polycubes = sorted(polycubes, key=lambda x:x.squares)

    print("Found {} polycubes of order {}".format(len(polycubes), N))
    # print(Polycube.hash_count) # debug

def draw():
    background(0)
    x = y = 0
    for p in sorted_polycubes:
        push()
        translate(x - w, y - w, -20 * w)
        translate(2 * w, 0, 0)
        rotateY(frameCount/100.)
        translate(-2 * w, 0, 0)
        p.draw(w)
        x += len(p) * w + 2
        pop()
        if x > width:
            x = 0
            y += len(p) * w
            
def generate_polycubes(target):
    a = millis()
    order = 1
    polycubes = set((Polycube(((0,0,0),)),))

    while order < target:
        order += 1
        next_order_polycubes = set()
        for p in polycubes:
            next_order_polycubes.update(p.raise_order(d=3))
        polycubes = next_order_polycubes
    
    print("Aprox. time: {}".format(millis()-a))
    return polycubes
