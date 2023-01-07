import fontforge

from partial_ordering import PartialOrdering

def get_polygons(font_path, characters):
  polygons = []
  font = fontforge.open(font_path)
  for k in characters:
    glyph = font[k]
    contours = glyph.layers['Fore']
    po = PartialOrdering(contours)
    for pid, spe in po.bfs():
      coords = spe.coords
      if not spe.is_ccw:
        coords = coords[::-1]
      polygons.append(coords)
  return polygons

polygons = get_polygons('Inconsolata-ExtraBold.ttf', ['A', 'b', 'c', 'd', 'e'])

def setup():
    size(720, 720)
    color_mode(HSB)
    translate(0, 700)
    scale(1, -1)
    no_fill()
    stroke_weight(3)
    for i, p in enumerate(polygons):
        stroke(i * 16, 255, 200)
        with begin_closed_shape():
            vertices(p)
            