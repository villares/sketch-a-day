SIN_60 = sqrt(3) * 0.5  # sin(radians(60))
W = 100
H = SIN_60 * W 


def setup():
    size(780, 780, P2D)
    no_stroke()
    color_mode(HSB)

def draw():
    background(0)
    k = 0
    for i in range(-1, int(width / H) + 2):
        for j in range(-1, int(height / H)): 
            x, y = ij_to_xy(i, j)
            hex(x, y, W/2, [0, 255], k + frame_count // 10)
            k += 1
    if frame_count // 10 <= 6 and frame_count % 10 == 0:
        save_frame('###.png')


def ij_to_xy(i, j):
    OX, OY = W / 2, H / 2 
    if i % 2 == 0:
        y = j * H  + OY
    else:
        y = j * H + H / 2 + OY
    x = i * W * 3 / 4 + OX
    return x, y

def hex(x, y, radius, colors, rot=0):
    passo = TWO_PI / 6
    for i in (0, 3):
        ang = passo * i + rot * radians(60)
        x0 = x + cos(ang) * radius
        y0 = y + sin(ang) * radius
        x1 = x + cos(ang + passo) * radius
        y1 = y + sin(ang + passo) * radius
        x2 = x + cos(ang + passo * 2) * radius
        y2 = y + sin(ang + passo * 2) * radius
        x3 = x + cos(ang + passo * 3) * radius
        y3 = y + sin(ang + passo * 3) * radius
        
        with begin_shape():
            fill(colors[i//3])    
            vertex(x0, y0)
            fill(colors[i//3 - 1])    
            vertex(x1, y1)
            fill(colors[i//3 - 1])    
            vertex(x2, y2)
            fill(colors[i//3])    
            vertex(x3, y3)
        #quad(x0, y0, x1, y1, x2, y2, x3, y3)



