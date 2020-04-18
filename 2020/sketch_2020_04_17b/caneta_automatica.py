from __future__ import division

def inicie_caneta():
    global caneta
    caneta = True
    translate(width / 2, height / 2)
    rotate(HALF_PI)

def suba_caneta():
    global caneta
    caneta = False

def baixe_caneta():
    global caneta
    caneta = True

def ande(n):
    if caneta:
        line(0, -n, 0, 0)
    translate(0, -n)

def vire(a):
    rotate(radians(-a))
    
def esquerda():
    vire(90)

def direita():
    vire(-90)
