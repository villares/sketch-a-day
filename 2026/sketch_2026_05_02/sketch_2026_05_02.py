from shapely import Point, Polygon, MultiPolygon, make_valid
import py5

d = 600
n = 20
s = 11

def setup():
    py5.size(600, 600)
    #py5.no_stroke()
    
def draw():
    py5.background('gray')
    estrela_cruzando(300, 300, d, n, s)
    
def estrela_cruzando(x, y, d, n, skip, rot=0):
    global shp
    r = d / 2
    base_pts = []
    passo = py5.TWO_PI / n
    for i in range(n): # i=0, 1, 2... n-1
        xv = x + r * py5.cos(i * passo + rot)
        yv = y + r * py5.sin(i * passo + rot)
        base_pts.append((xv, yv))
    i = None
    base = Polygon(base_pts)
    vs = []
    while i != 0:
        if i is None:
            i = 0
        vs.append(base_pts[i])
        i = (i + skip) % n
    try:
        shp = make_valid(Polygon(vs))
        space = base - shp
        if hasattr(shp, 'geoms'):
            max_area = max(p.area for p in
                           list(shp.geoms) + list(space.geoms))
            py5.color_mode(py5.CMAP, 'viridis', max_area)
            for p in shp.geoms:        
                py5.fill(p.area)
                py5.shape(p)
            #py5.translate(5, 5)
            for p in space.geoms:        
                py5.fill(p.area)
                py5.shape(p)
    except:
        pass
    py5.fill(255)
    py5.text_size(40)
    py5.text(f'{n=} {s=}', 20, 40)
            
def key_pressed():
    global n, s
    if py5.key == 'a':
        n += 1
    elif py5.key == 'z':
        n -= 1
    elif py5.key == 's':
        s += 1
    elif py5.key == 'x':
        s -= 1
    elif py5.key == 'p':
        py5.save_frame('out###.png')
    

def mouse_wheel(evento):
    global d
    c = evento.get_count()
    d = d + c * 5
       
py5.run_sketch(block=False)


