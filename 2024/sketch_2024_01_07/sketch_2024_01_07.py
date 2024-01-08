

sectors = set()
k = 0
N = 180
step = TWO_PI / N

def setup():
    size(600, 600)
    color_mode(HSB)
 
def draw():
    global k
    background(0)
    no_stroke()
    translate(width /2, height / 2)
    rotate(radians(frame_count))
    ra, rb = 100, 200 + 50 * sin(radians(frame_count))

    for i, p in enumerate(sectors):
        cosab = cos(p * step)
        sinab = sin(p * step)
        xa, ya = cosab * ra, sinab * ra
        xb, yb = cosab * rb, sinab * rb
        coscd = cos(p * step + step)
        sincd = sin(p * step + step)
        xc, yc = coscd * ra, sincd * ra
        xd, yd = coscd * rb, sincd * rb
        fill(p * 255 / N, 255, 255)
        quad(xa, ya, xb, yb, xd, yd, xc, yc)
        
    if k in sectors:
        k +=1        
    if len(sectors) == N:
        no_loop()
    if frame_count % 10 == 0:
        print(len(sectors))
        sectors.add(k)
        k = (k + 10) % N
         
         