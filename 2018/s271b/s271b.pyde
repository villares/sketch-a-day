
def setup():
    size(200, 101)
    colorMode(HSB)
    noStroke()

    palette(y=00, s=1, e=10, step=24)
    palette(y=20, s=1, e=8, step=32)
    palette(y=40, s=1, e=5, step=48)
    palette(y=60, s=1, e=5, step=51)
    palette(y=80, s=0.5, e=5, step=60)

def palette(y, s, e, step):
    for i in range(e):
       fill(s * step + i  * step, 255, 255)
       rect(i * 20, y, 20, 20)
