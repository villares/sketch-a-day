# tinyurl.com/blue-speech

def setup():
    createCanvas(600, 600)

def draw():
    background(200)
    randomSeed(millis() / 10**10)
    
    fill(0, 0, 100, 100)
    for i in range(5):
        tam = sin(frameCount / 60 + i * 1000) * 50 + 150
        x, y = random(200, 400), random(200, 400)
        b = balao(x, y, tam, tam, mode=CENTER)
        draw_poly(b)
    
def draw_poly(pts, closed=True):
    beginShape()
    for x, y in pts:
        vertex(x, y)
    if closed:
        endShape(CLOSE)
    else:
        endShape()
def balao(ox, oy, w, h, ponta=None, mode=CENTER,
          flip_h=False, flip_v=False):
    wbase = w / 4
    offset = w / 4
    if mode == CENTER:
        x, y = ox - w / 2.0, oy - h / 2.0
    else:
        x, y = ox, oy
    px, py = ponta or x + w, y + h * 1.5

    pts = [(x, y), (x + w, y),
              (x + w, y + h),
              (offset + x + w / 2 + wbase / 2, y + h),
              (px, py),  # (x + w / 2, y + h),
              (offset + x + w / 2 - wbase / 2, y + h),
              (x, y + h)]
    # Esses flips tão dando problema / there is maybe a bug here
    if flip_h:
        pts = [(-x, y) for x, y in pts]  
    if flip_v:
        pts = [(x, -y) for x, y in pts]
    return pts