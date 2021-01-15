from collections import deque
from random import randint

d = deque([0], maxlen=10)
new_n = 0   

def setup():
    size(400, 400)
    frameRate(20)
    
def draw():
    global new_n
    background(0)
    for i, n in enumerate(d):
        x = i * 40
        rect(x, n * 20, 40, 20)

    while new_n in d:
        new_n = randint(0, 19)
    d.append(new_n)
        
