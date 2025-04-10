# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190318a", ".png"

W = 50
H = 50
S = 50

def setup():
    size(500, 500)

def draw():
    for x in range(W):
        for y in range(H):
            if (x + y) % 2 == 0:
                if y % 2:
                    fill(0)
                else:
                    fill(200, 0, 0)
                rect(x * S, y * S, S, S)
            else:
                fill(255)
                rect(x * S, y * S, S, S)
                fill(0, 0, 200)
                rect(x * S + S / 2, y * S + S / 2, S, S)
