
def setup():
    size(200, 101)
    colorMode(HSB)
    noStroke()
    palette(y=0, ran=8, step=32)
    palette(y=20, ran=5, step=42.5)
    palette(y=40, ran=5, step=48)
    palette(y=60, ran=5, step=51)
    palette(y=80, ran=4, step=64)

def palette(y, ran, step):
    for i in range(ran):
       fill(i * step, 255, 255)
       rect(i * 20, y, 20, 20)
