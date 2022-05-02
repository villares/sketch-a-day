
import tkinter as tk
from ptk import *
from random import randint

size(512 + 128, 512 + 128)
print(globals()['width'])
background(200)

def grid(xo, yo, w):
    qw = int(w / 4)
    for i in range(4):
        x = xo + i * qw
        for j in range(4):
            y = yo + j * qw
            r = randint(1, 3)
            if qw > 10 and r == 1:
                grid(x, y, qw)
            elif r == 2:
                esp = max(randint(2, 4), int(qw / randint(8, 10)))
                line_grid(x, y, qw, qw, esp, fill='blue')
            else:
                poly(((x, y),
                      (x + qw, y),
                      (x, y + qw)),
                       fill='black')
grid(0, 0, width)

ptk_run()


