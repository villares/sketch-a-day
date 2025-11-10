def setup():
    size(400, 400)
    
def draw():
    background(100, 200, 0)
    ovo(150, 150, 50, 62.5)
    ovo(250, 250, 100, 125)
    
def ovo(cx, cy, diam, alt):
    rad = diam * 0.5
    ct = rad * 0.58
    tt = rad * 0.5
    with begin_closed_shape():
        vertex(cx, cy - (alt - rad))
        bezier_vertex(cx + tt,  cy - (alt - rad),
                      cx + rad, cy - ct,
                      cx + rad, cy)
        bezier_vertex(cx + rad, cy + ct,
                      cx + ct,  cy + rad,
                      cx,       cy + rad)
        bezier_vertex(cx - ct,  cy + rad,
                      cx - rad, cy + ct,
                      cx - rad, cy)
        bezier_vertex(cx - rad, cy - ct,
                      cx - tt,  cy - (alt - rad),
                      cx,       cy - (alt - rad))
