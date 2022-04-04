H = 15
W = 100

def setup():
    size(900, 900)
    no_stroke()
    fill(0)
    
def draw():
    background(240)
    cols = width // W
    rows = height // H
    n = 0
    v = 0.03
    for col in range(cols):
        for row in range(rows):
#             x0, y0 = col * W, row * H
#             third_x = x0 + W * n
#             triangle(x0, y0, x0 + W, y0, third_x, y0 + H)
#             n += v
#             if not (0 <= n <= 1):
#                 v = -v
#     for row in range(rows):
#         for col in range(cols):
            x0, y0 = col * W, row * H
            third_x = x0 + W * n
            triangle(x0, y0, x0 + W, y0, third_x, y0 + H)
            n += v
            if not (0 <= n <= 1):
                v = -v