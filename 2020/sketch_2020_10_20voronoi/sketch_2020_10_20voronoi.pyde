
def setup():
    size(500, 500)
    generate_voronoi_diagram(width, height, 25)
    saveFrame("VoronoiDiagram.png")

def generate_voronoi_diagram(w, h, num_cells):
    nx, ny, nr, ng, nb = [], [], [], [], []
    for i in range(num_cells):
        nx.append(int(random(w)))
        ny.append(int(random(h)))
        nr.append(int(random(256)))
        ng.append(int(random(256)))
        nb.append(int(random(256)))
    for y in range(h):
        for x in range(w):
            dmin = dist(0, 0, w - 1, h - 1)
            j = -1
            for i in range(num_cells):
                d = dist(x, y, nx[i], ny[i])
                # d = minkowski_3(x, y, nx[i], ny[i])
                # d = manhattan(x, y, nx[i], ny[i])
                if d < dmin:
                    dmin = d
                    j = i
            set(x, y, color(nr[j], ng[j], nb[j]))

def manhattan(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def minkowski_3(x1, y1, x2, y2):
    return (abs(x2 - x1) ** 3 + abs(y2 - y1) ** 3) ** 0.33
