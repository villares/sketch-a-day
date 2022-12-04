from random import sample, seed, randint
from villares.helpers import save_png_with_src

nodes = {}
unvisited_nodes = []

polys = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))

#EVN_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2, -2), (2, -2))
#ODD_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2,  2), (2,  2))
W = 6
H = W * (3 ** 0.5) * 0.5


def setup():
    global w, h
    size(600, 600)
    w, h = int(width / 2 / W - 1), int(height / 2 / W - 1)
    start(1)

    
def start(rnd_seed):
    global s
    s = rnd_seed
    seed(rnd_seed)
    nodes.clear()
    polys[:]=[]
    unvisited_nodes[:] = []
    for i in range(3):
        x, y = randint(-20, 20) * 1, randint(-20, 20) * 1
        unvisited_nodes.append((x, y))
        nodes[(x, y)] = (x, y, i, 1)
    

def tentar():
    todos = [(k, (v[0], v[1])) for k, v in nodes.items()]
    polys[:] = find_polygons(todos)
    
#     if nodes:
#         todos = list(nodes.items())
#         k, v = todos.pop()
#         ps = []
#         print(k, v)
#         ps.append(k)
#         while k in nodes:
#             ib, jb, c, gen = nodes.pop(k)
#             k = ib, jb
#             ps.append(k)
#         polys.append(ps)
        
def draw():
    background(240)
    translate(width / 2, height / 2)
#     for n, v in nodes.items():
#         ia, ja = n
#         ib, jb, c, gen = v
#         if visible(ia, ja) and visible(ib, jb):
#             xa, ya = ij_to_xy(ia, ja)
#             xb, yb = ij_to_xy(ib, jb)
#             stroke(0)
#             stroke_weight(1.5 + 1 * sin((gen - PI/2) * 0.1))
#             line(xa, ya, xb, yb)
    if frame_count < 50: unvisited_nodes[:] = grow()
    tentar()
    for i, pts in enumerate(polys):
        stroke(i * 64 % 255, 100, 108)
        if pts:
            begin_shape()
            curve_vertex(*pts[0])
            for i, (ia, ja) in enumerate(pts[:]):
                if is_mouse_pressed: text(i, *ij_to_xy(ia, ja))
                curve_vertex(*ij_to_xy(ia, ja))
            curve_vertex(*pts[-1])
            end_shape()
        
def ij_to_xy(i, j):
    if i % 2 == 0:
        y = j * H * 2 + H
    else:
        y = j * H * 2 + H * 2
    x = i * W * 1.5 + W
    return x, y


def grow():
    for i, j in unvisited_nodes:
        if not visible(i, j):
            continue
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        #nbs = [(n[0] * 2, n[1] * 2) for n in nbs]
        _, _, c, gen = nodes[(i, j)]
        seed(gen // 2 + c)
        xnbs = sample(nbs, 3)
        for ni, nj in xnbs:
            ini, jnj = i + ni, j + nj
            if (ini, jnj) not in nodes:
                nodes[(ini, jnj)] = (i, j, c, gen + 1)
                yield ini, jnj


def visible(i, j):
    x, y = ij_to_xy(i, j)
    return (abs(x) < width / 2 - W * 5 and
            abs(y) < height / 2 - W * 5)


def key_pressed(e):
    global s
    if key == 's':
        save_png_with_src()
    elif key == ' ':
        s += 1 
        start(s)
            
from collections import defaultdict

def find_polygons(segments):
  connections = defaultdict(list)
  for segment in segments:
    connections[segment[0]].append(segment[1])
    connections[segment[1]].append(segment[0])
  # find connecting
  polygons = []
  for start_point, end_points in connections.items():
    for end_point in end_points:
      if end_point in connections:
        polygon = [start_point, end_point]
        current_point = end_point
        while connections[current_point]:
          next_point = connections[current_point].pop()
          polygon.append(next_point)
          current_point = next_point
        polygons.append(polygon)
  #print(len(polygons))
  return polygons
