# Desenhos simétricos - 2019 Alexandre Villares
# Para Processing modo Python
# Como instalar o Processing em casa:
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/   
# Sob licença GPL v3.0

from functools import reduce

add_library('geomerative')
add_library('pdf')

segments = []
next_seg_preview = []
seg_limit = 8

start_w = 10 # segment width
end_w = 10
divisions = 5      # Use "+" and "-" to change
save_pdf = False   # Use "p" to save a PDF
mirror = True      # Use "m" to toggle

def setup():
    size(500, 500)
    global mh, mv
    mh, mv = width / 2, height / 2
    RG.init(this)

def draw():
    global save_pdf
    if save_pdf:
        beginRecord(PDF, "####.pdf")
   
    translate(mh, mv)
    background(0, 128, 32)  # verde (mude a sua cor!)
    bars = []
    for num in range(divisions):
        angle = radians(360.0 / divisions) * num
        fill(255)
        for segment in segments:
            x1, y1, x2, y2 = segment
            points = bar_points(x1, y1, x2, y2, start_w, end_w)
            rotated_points = [rot((x, y), angle) for x, y in points]
            bars.append(RPolygon([RPoint(x, y) for x, y in rotated_points]))
            if mirror:
                bars.append(RPolygon([RPoint(x, - y) for x, y in rotated_points]))
    if len(bars) > 1:
        union = reduce(lambda polya, polyb : polya.union(polyb), bars)
        RG.shape(union.toShape())
        
    if save_pdf:
        endRecord()
        save_pdf = False

    if next_seg_preview and len(segments) < seg_limit:
        push()
        px, py = next_seg_preview
        for num in range(divisions):
            rotate(radians(360 / divisions))
            fill(255, 100)
            preview_bars(px, py, mouseX - mh, mouseY - mv, start_w, end_w, mirror)
        pop()
        
def mousePressed(): 
    if len(segments) < seg_limit:
        if next_seg_preview:
            px, py = next_seg_preview
            segments.append((px, py, mouseX - mh, mouseY - mv))
        if mouseButton == LEFT:
            next_seg_preview[:] = mouseX - mh, mouseY - mv
        elif mouseButton == RIGHT:
            next_seg_preview[:] = []
    
def keyPressed():
    global save_pdf, divisions, mirror
    if key == "m":
        mirror = not mirror
    if key == "a":
        segments[:] = []  #    erase all segmens
        next_seg_preview[:] = []
    if key == "g":
        saveFrame("#####.png")
        print("saving PNG")
    if key == "p":
        save_pdf = True
        print("saving PDF")
    if key == BACKSPACE and segments: 
        segments.pop()
    if key == "-" and divisions > 2:
        divisions -= 1
    if key == "+" or key == "=" and divisions < 12:
        divisions += 1        
   
def preview_bars(p1x, p1y, p2x, p2y, w1, w2, mirror):
    draw_poly(bar_points(p1x, p1y, p2x, p2y, w1, w2))
    if mirror:
        draw_poly(bar_points(p1x, -p1y, p2x, -p2y, w1, w2))    
    
def draw_poly(points):
    beginShape()  
    for x, y in points:
        vertex(x, y)
    endShape(CLOSE)        
        
def bar_points(p1x, p1y, p2x, p2y, w1, w2=None, o=0):
    """ 
    trapezoid, draws a rotated quad with axis
    starting at (p1x, p1y) ending at (p2x, p2y) where
    w1 and w2 are the starting and ending side widths.
    """
    if w2 is None:
        w2 = w1
    d = dist(p1x, p1y, p2x, p2y)
    angle = atan2(p1x - p2x, p2y - p1y)  + HALF_PI
    unrotated_points = (
        (p1x - o, p1y - w1 / 2),
        (p1x - o, p1y + w1 / 2),
        (p1x + d + o, p1y + w2 / 2),
        (p1x + d + o, p1y - w2 / 2)
        )
    return [rot(pt, angle, center=(p1x, p1y)) 
              for pt in unrotated_points]
    
def rot(pt, angle, center=None):
    xp, yp = pt
    x0, y0 = center or (0, 0)
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)
