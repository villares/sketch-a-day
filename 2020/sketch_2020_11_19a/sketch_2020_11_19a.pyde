from villares.line_geometry import inter_lines, draw_poly, Line

def setup():
    size(400, 400)

def draw():
    background(230, 200, 200)
    r = rect_points(50, 50, 300, 300)    
    draw_poly(r)
    num = 50
    for i in range(num):
        H, W = mouseX, mouseY
        diag = Line(r[1], r[3]) #.draw()
        dp = diag.line_point(i / float(num) + EPSILON)
        print(dp)
        hli = Line(dp.x + W, dp.y + H, dp.x - W, dp.y - H) #.draw()
        inters = inter_lines(hli, r)
        for li in inters:
            li.draw()
        
def rect_points(x, y, w, h):
    return [(x, y), (x, y + h), (x + w, y + h), (x + w, y)]
