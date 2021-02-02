from __future__ import division

N = 10
modo_teste = True

def setup():
    size(700, 700)
    rectMode(CENTER)
    strokeWeight(3)
    frameRate(10)
    
def draw():
    background(200)
    translate(width / 2, height / 2) 
    if modo_teste:
            t = (frameCount % N) / (N + 1) 
            desenho(t)            
    else:
        scale(.5)
        for i in range(N):
            t = i / N 
            rotate(TWO_PI / N)
            pushMatrix()
            translate(0, -height * .75)
            desenho(t)  
            popMatrix()          
    
def desenho(t):
        noFill()
        circle(0, -5 - t * 125, 5 + t * 15)
        square(0, 0, 10 + t * 250)
        
def keyPressed():
    global modo_teste
    modo_teste = not modo_teste
        
