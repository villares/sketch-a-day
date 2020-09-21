"""
Polycube Searching
"""

from p5 import *
from polycube import Polycube

w = 20
N = 5  # 8:6922 in 23s 40s


def setup():
    size(500, 500)
    background(204)
    polycubes = generate_polycubes(N)
    global sorted_polycubes
    sorted_polycubes = sorted(polycubes, key=lambda x: x.squares)

    print("Found {} polycubes of order {}".format(len(polycubes), N))
    # print(Polycube.hash_count) # debug
    # strokeWeight(.5)
    # print(millis())


def draw():
    background(0)
    # lights()
    x = y = 0
    for p in sorted_polycubes:
        push_matrix()
        z = 100  # -20 * w
        translate(x - width/2, y - height/2, z)
        rotate_y(frame_count * 5)
        p.draw(w)
        x += len(p) * w + 2
        pop_matrix()
        if x > width:
            x = 0
            y += len(p) * w


def generate_polycubes(target):
    global polycubes
    print('calculating...')
    # a = millis()
    order = 1
    polycubes = set((Polycube(((0, 0, 0),)),))

    while order < target:
        order += 1
        next_order_polycubes = set()
        for p in polycubes:
            next_order_polycubes.update(p.raise_order(d=3))
        polycubes = next_order_polycubes

    # print("Aprox. time: {}".format(millis()-a))
    return polycubes


run(mode="P3D")
