
W = 5
H = W * (3 ** 0.5) * 0.5


def setup():
    global w, h
    size(600, 600)
    w, h = int(width / 2 / W - 1), int(height / 2 / W - 1)
    start()
    
def start():
    global polys
    polys = [[]]
    for _ in range(4):
        polys[-1].append(ij_to_xy(random_int(-2,2), random_int(-2,2)))
        
        
def draw():
    background(240)
    translate(width / 2, height / 2)
    for i, pts in enumerate(polys):
        stroke(255, 100, 108)
        stroke_weight(4)
        points([ij_to_xy(i, j) for i, j in pts])
        stroke_weight(1)
        no_fill()
        begin_shape()
#         curve_vertex(*pts[-1])
        curve_vertex(*pts[0])
        for i, (ia, ja) in enumerate(pts[:]):
            if is_mouse_pressed: text(i, *ij_to_xy(ia, ja))
            curve_vertex(*ij_to_xy(ia, ja))
        curve_vertex(*pts[-1])
#         curve_vertex(*pts[0])
        end_shape()
        stroke(0)
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


def visible(i, j):
    x, y = ij_to_xy(i, j)
    return (abs(x) < width / 2 - W * 5 and
            abs(y) < height / 2 - W * 5)


def key_pressed(e):
    global s
    if key == 's':
        save_png_with_src()
    elif key == ' ':
        start()
                
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
