import villares.ubuntu_jogl_fix

"""
From a talk by Hamish Campbell
https://pyvideo.org/kiwi-pycon-2013/polycubes-an-exploration-in-problem-solving-w.html
"""

from polycube import Polycube

w = 4
N = 8  # 8:6922 in 23s 40s

def setup():
    global sorted_polycubes
    size(1200, 650, P3D)
    pixelDensity(2)
    
    polycubes = generate_polycubes(N)
    sorted_polycubes = sorted(polycubes, key=lambda x:x.squares)

    print("Found {} polycubes of order {}".format(len(polycubes), N))
    # print(Polycube.hash_count) # debug
    strokeWeight(.5)

def draw():
    background(0)
    lights()
    x = y = 0
    for p in sorted_polycubes:
        push()
        z = -20 * w 
        if dist(mouseX,
                mouseY,
                screenX(x, y, z),
                screenY(x, y, z)) < 2 * w:
            translate(width / 2, height /2 , 50)
            scale(10)
        else:
            translate(x - w, y - w, z)
        rotateY(frameCount/100.)
        p.draw(w)
        x += len(p) * w + 2
        pop()
        if x > width:
            x = 0
            y += len(p) * w
            
def generate_polycubes(target):
    global polycubes
    print('calculating...')
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
