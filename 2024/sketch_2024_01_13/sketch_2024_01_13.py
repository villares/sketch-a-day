# py5coding.org imported mode

curvas = []
n = 3

def setup():
    size(1024, 300)
    no_stroke()
    blend_mode(MULTIPLY)
    stroke_cap(SQUARE)
    print('Press "s" to save frame and any other key to generate curves')
    
def key_pressed():
    if key == "s":
        save_frame("###.png")
    else: 
        curvas[:] = []
        for i in range(n):
            curvas.append((
                  random(-height / 7, height / 7),
                  random(-height / 7, height / 7),
                  random(.33, 3),
                  random(.33, 3),
                  random(.33, 3),
                 ))

def draw():
    background(200)
    f = frame_count
    translate(0, height / 2)
    for i, (h, a, f1, f2, f3) in enumerate(curvas):
        if i % 3 == 0:
            stroke(100, 0, 200)
        elif i % 3 == 1:
            stroke('orange')
        else:
            stroke('red')
        begin_shape()
        stroke_weight(5 + abs(h) / 5)
        for x in range(width):
            ang = (f +  x) / 20
            ang2 = (f * 2 + x) / 20
            s = sin(ang * f1) + sin(ang2 * f2) * sin(ang2 * f3) + cos(ang * f3) 
            vertex(x, h + s * a)
        end_shape()
        