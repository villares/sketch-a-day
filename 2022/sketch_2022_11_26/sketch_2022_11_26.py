boxes = []
H = 100

def setup():
    size(800, 800)
    for _ in range(40):
        boxes.append((random_choice((1, 1.5, 2)) * H, H))  

def draw():
    background(0)
    
    x = y = n = 0
    for b in boxes:
        w, h = b
        fill(w % 255, h % 255, n * 8)
        if x + w > width:
            x = 0
            y += H
        rect(x, y, w, h)
        n += 1
        x += w
        if x == width:
            x = 0
            y += H
        if y >= height:
            break
        