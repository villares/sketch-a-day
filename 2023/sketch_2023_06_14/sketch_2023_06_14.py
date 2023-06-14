
from shapely.geometry import Polygon, MultiPolygon, GeometryCollection, LineString, Point
from shapely.ops import unary_union

polilinhas = [[]]   # lista com uma lista vazia dentro

LINE_THICKNESS = 10
GAP = LINE_THICKNESS * 2 # tamanho da interrupção da linha

def setup():
    size(600, 600)
    
def draw():
    background(0, 0, 200)  # R G B 0-255 (azul)
    #stroke_weight(LINE_THICKNESS)
    stroke('#FFFFFF')   # cor hexadecimal #RRGGBB
    no_fill()
    poligonos = []
    
    
    for polilinha in polilinhas:
        for i, pt in enumerate(polilinha[:-1]):
            x, y = pt
            px, py = polilinha[i + 1]
            poligonos.extend(linha_interrompida(x, y, px, py))
    
    
    draw_shapely_objs(unary_union(poligonos))
    
    if polilinhas[-1]:
        x, y = polilinhas[-1][-1]
        stroke(0)
        line(x, y, mouse_x, mouse_y)

def mouse_pressed():
    if mouse_button == LEFT:
        polilinhas[-1].append((mouse_x, mouse_y))
    elif mouse_button == RIGHT:
        polilinhas[-1].append((mouse_x, mouse_y))
        polilinhas.append([])
        
def key_pressed():
    if key == BACKSPACE:
      #print('Backspace')
      if polilinhas[-1]:
          polilinhas[-1].pop()
      elif len(polilinhas) > 1:
          polilinhas.pop()
          
   
def linha_interrompida(x1, y1, x2, y2):
    resultado = []
    d = dist(x1, y1, x2, y2)
    if d < 2 * GAP:
        resultado.append(LineString([(x1, y1), (x2, y2)]))
    elif d < 5 * GAP:  # else if 
        ux, uy = (x2 - x1) / d, (y2 - y1) / d  # vetor unitario
        mx, my = (x2 - x1) / 2, (y2 - y1) / 2  # vetor de 1 terço
        x1g = x1 + mx - ux * GAP / 2
        y1g = y1 + my - uy * GAP / 2
        x2g = x1 + mx + ux * GAP / 2
        y2g = y1 + my + uy * GAP / 2
        resultado.append(LineString([(x1, y1), (x1g, y1g)]))
        resultado.append(LineString([(x2g, y2g), (x2, y2)]))
    else:
        ux, uy = (x2 - x1) / d, (y2 - y1) / d  # vetor unitario
        tx, ty = (x2 - x1) / 3, (y2 - y1) / 3  # vetor de 1 terço
        x1g = x1 + tx - ux * GAP / 2
        y1g = y1 + ty - uy * GAP / 2
        x2g = x1 + tx + ux * GAP / 2
        y2g = y1 + ty + uy * GAP / 2
        x3g = x1 + 2 * tx - ux * GAP / 2
        y3g = y1 + 2 * ty - uy * GAP / 2
        x4g = x1 + 2 * tx + ux * GAP / 2
        y4g = y1 + 2 * ty + uy * GAP / 2
        
        resultado.append(LineString([(x1, y1), (x1g, y1g)]))
        resultado.append(LineString([(x2g, y2g), (x3g, y3g)]))
        resultado.append(LineString([(x4g, y4g), (x2, y2)]))
    
    resultado_final = [lin.buffer(LINE_THICKNESS / 2) for lin in resultado]
    return resultado_final

def draw_shapely_objs(element):
    """
    With py5, draw some shapely object (or a list of objects).
    """
    if isinstance(element, (MultiPolygon, GeometryCollection)):
        for p in element.geoms:
            draw_shapely_objs(p)
    elif isinstance(element, Polygon):
        with begin_closed_shape():
            if element.exterior.coords:
                vertices(element.exterior.coords)
            for hole in element.interiors:
                with begin_contour():
                    vertices(hole.coords)
    elif isinstance(element, list):
        for i, p in enumerate(element):
            draw_shapely_objs(p)
    elif isinstance(element, LineString):
        (xa, ya), (xb, yb) = element.coords
        line(xa, ya, xb, yb)
    elif isinstance(element, Point):
        with push_style():
            x, y = element.coords[0]
            point(x, y)
    else:
        print(f"I can't draw {element}.")