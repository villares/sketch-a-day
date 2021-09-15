
import tkinter as tk
from ptk import *
from random import randint

size(600, 600)
background(0, 0, 100)

def grid(xo, yo, w):
    qw = w / 4
    for i in range(4):
        x = xo + i * qw
        for j in range(4):
            y = yo + j * qw
            r = randint(1, 3)
            if qw > 10 and r == 1:
                grid(x, y, qw)
            elif r == 2:
                rect(x, y, qw, qw, fill='blue')
            else:
                poly(((x, y),
                      (x + qw, y),
                      (x, y + qw)),
                       fill='red')
grid(0, 0, width)

ptk_run()

