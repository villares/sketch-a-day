from random import choice

boxes = []
H = 100 * 3 / 4
MAX_W = 600

def setup():
    size(1800, 600)
    for _ in range(80):
        boxes.append((
            choice((1, 1.333, 1.5, 2)) * H,
            1 * H#choice((1, 0.666)) * H
            ))  
    
def draw():
    background(0)       
    x = y = n = 0
    rows = [[]]
    for b in boxes:
        w, h = b
        w = scale_width_by_height(w, h, H)
        h = H
        if x + w > MAX_W:
            x = 0
            y += H
            rows.append([])
        rows[-1].append((y, w, h))
        n += 1
        x += w
        if x == MAX_W:
            x = 0
            y += H
            rows.append([])
        if y >= height:
            break
    # spaced
    n = 0
    for row in rows:
        tw = sum(w for y, w, h in row)
        spacing = (MAX_W - tw) / (len(row) + 1) if len(row) > 1 else 0
        x = spacing
        for y, w, h in row:
            fill(w % 255, h % 255, n * 8)
            rect(x, y, w, h)
            x += w + spacing
            n += 1
    translate(MAX_W, 0)
    with push_style(): stroke(255); line(0, 0, 0, height)
    n = 0
    for row in rows:
        tw = sum(w for y, w, h in row)
        x = (MAX_W - tw) / 2
        for y, w, h in row:
            fill(w % 255, h % 255, n * 8)
            rect(x, y, w, h)
            x += w
            n += 1
    translate(MAX_W, 0)
    with push_style(): stroke(255); line(-1, 0, -1, height)
    n = 0
    for row in rows:
        tw = sum(w for y, w, h in row)
        spacing = (MAX_W - tw) / (len(row) - 1) if len(row) > 1 else 0
        x = 0
        for y, w, h in row:
            fill(w % 255, h % 255, n * 8)
            rect(x, y, w, h)
            x += w + spacing
            n += 1
        
        
def scale_width_by_height(w, h, target_h):    
    ratio = w / h
    return target_h * ratio

    