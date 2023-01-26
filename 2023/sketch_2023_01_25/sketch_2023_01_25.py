
S = 600
ns = 1

def setup():
    size(S, S)
    no_stroke()
    
def draw():
    noise_seed(ns)
    background(255, 255, 0)
    x, f = 8, frame_count
    while x < S * 2:
        y = 8
        while y < S:
            M = 16 + 4 * sin(x * 0.05)
            h = M * noise(x * 0.01, y * 0.01, f * 0.01) #+ sin(y * 0.005)
            fill(0)
            #fill(h * 24, 255 - h * 16, 0)
            circle(x, y, min(M * 0.45, h))
            y += min(M * 0.5, h)
        x += M * 0.5  
    fill(255, 255, 0)
    rect(0, S - 4, width, 4)
        
def key_pressed():
    global  ns
    ns += 1
    save_frame('####.png')