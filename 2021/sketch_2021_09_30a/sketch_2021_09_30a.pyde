from helpers import line_intersect, point_inside_poly, ccw

def setup():
    size(500, 500)
    noCursor()
    
def draw():
    background(200)
    scale(2)
    noFill()
    stroke(0)
    t1 = [(100, 100), (200, 100), (150, 150)]; draw_t(t1)
    t2 = [(mouseX, mouseY), (mouseX +50, mouseY), (mouseX + 25, mouseY + 100)]; draw_t(t2)
    edges1 = t_edges(t1)
    edges2 = t_edges(t2)
    for i, edge_i in  r_enumerate(edges1):
        for j, edge_j in r_enumerate(edges2):
            ip = line_intersect(edge_i, edge_j)
            if ip:
                eia, eib = split_edge(edge_i, ip)
                edges1[i] = eia
                edges1.insert(i + 1, eib)
                eja, ejb = split_edge(edge_j, ip)
                edges2[j] = eja
                edges2.insert(j + 1, ejb)
                circle(ip[0], ip[1], 5)
    edges1_in_t2 = [edge for edge in edges1 if edge_in_poly(edge, t2)]
    stroke(255, 0, 0)
    draw_edges(edges1_in_t2)
    edges2_in_t1 = [edge for edge in edges2 if edge_in_poly(edge, t1)]
    stroke(0, 0, 200)
    draw_edges(edges2_in_t1)
    
def draw_edges(edges):
    push()
    translate(2, 2)
    for (xa, ya), (xb, yb) in edges:
        line(xa, ya, xb, yb)
    pop()

def edge_in_poly(edge, poly):
    x, y = midpoint(edge)
    return point_inside_poly(x, y, poly)

def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0

def split_edge(edge, p):
    return (edge[0], p), (edge[1], p)
    
def r_enumerate(iterable):
    return reversed(tuple(enumerate(iterable)))

def draw_t(t):
    triangle(*(t[0] + t[1] + t[2]))

def t_edges(t):
    a, b, c = t if not ccw(t) else t[::-1]
    return [(a, b), (b, c), (c, a)]
