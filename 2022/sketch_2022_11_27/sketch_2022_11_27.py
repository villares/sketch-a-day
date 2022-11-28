from random import choice

boxes = []
H = 100
MAX_W = 800

def setup():
    size(1600, 800)
    for _ in range(80):
        boxes.append((
            choice((1, 1.333)) * H,
            choice((1, 0.666)) * H
            ))  
    
def draw():
    background(0)
    
    x = y = n = 0
    for b in boxes:
        w, h = b
        fill(w % 255, h % 255, n * 8)
        if x + w > MAX_W:
            x = 0
            y += H
        rect(x, y, w, h)
        n += 1
        x += w
        if x == MAX_W:
            x = 0
            y += H
        if y >= height:
            break
        
    translate(800, 0)        
    x = y = n = 0
    for b in boxes:
        w, h = b
        fill(w % 255, h % 255, n * 8)
        w = scale_width_by_height(w, h, H)
        h = H
        if x + w > MAX_W:
            x = 0
            y += H
        rect(x, y, w, h)
        n += 1
        x += w
        if x == MAX_W:
            x = 0
            y += H
        if y >= height:
            break
        
        
def scale_width_by_height(w, h, target_h):    
    ratio = w / h
    return target_h * ratio

    