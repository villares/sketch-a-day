

def setup():
    size(400, 400)
    stroke_weight(5)
    no_cursor()
    
def draw():
    background(200)
    seta(100, 100, mouse_x, mouse_y)
    
def seta(xa, ya, xb, yb):
    tam_seta = dist(xa, ya, xb, yb)
    ang = atan2(yb - ya, xb - xa)    
    xai, yai = lerp_tuple((xa, ya), (xb, yb), 1 / 3.0)
    xaf, yaf = lerp_tuple((xa, ya), (xb, yb), 2 / 3.0)
#     line(xa, ya, xai, yai)
#     line(xaf, yaf, xb, yb)
    amp = 20 * sin(frame_count / 10.0)
    xout = cos(ang + HALF_PI) * amp
    yout = sin(ang + HALF_PI) * amp
#     line(xai, yai, xai + xout, yai + yout)
#     line(xai + xout, yai + yout, xaf + xout, yaf + yout)
#     line(xaf + xout, yaf + yout, xaf, yaf)
    no_fill()
    begin_shape()
    vertex(xa, ya)
    vertex(xai, yai)
    vertex(xai + xout, yai + yout)
    vertex(xaf + xout, yaf + yout)
    vertex(xaf, yaf)    
    vertex(xb, yb)
    end_shape()
    tam_ponta = tam_seta / 10 * sqrt(2)
    xpe = xb + cos(ang + QUARTER_PI + PI) * tam_ponta
    ype = yb + sin(ang + QUARTER_PI + PI) * tam_ponta
    line(xb, yb, xpe, ype) # parte esquerda da ponta
    xpd = xb + cos(ang - QUARTER_PI + PI) * tam_ponta
    ypd = yb + sin(ang - QUARTER_PI + PI) * tam_ponta
    line(xb, yb, xpd, ypd) # parte direita da ponta
    
    
def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))