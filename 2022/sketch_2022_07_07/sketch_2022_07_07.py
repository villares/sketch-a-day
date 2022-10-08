"""
sketch_2022_07_07 - d'aprés Antonio Maluf 1926—2005
Alexandre B A Villares - abav.lugaragum.com/sketch-a-day
Rewritten 2022_07_10, requires py5coding.org 'static mode'
"""

size(800, 1000) #, PDF, 'output.pdf')
no_stroke()
step = 40
speed = 1 / 150
for y in range(0, height, step): 
    for x in range(0, width, step):
        w = (step + step * cos(x * speed) * 0.75) / 2
        h = (step + step * sin(y * speed) * 0.75) / 2
        fill(0)
        rect(x, y, w, h)
        fill(255, 100, 0)
        rect(x + w, y + h, step - w, step - h)
