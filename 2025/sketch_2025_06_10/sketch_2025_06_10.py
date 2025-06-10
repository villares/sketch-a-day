# py5 imported mode code: learn about it at py5coding.org 

from shapely import Point, Polygon, LineString
import trimesh

pontos = [(100, 100), (200, 100), (100, 200)]

def setup():
    size(400, 400)
    background(0, 200, 0)
    
    triangulo = Polygon(pontos)
    fill(255, 100)
    shape(triangulo)
    
    circulo = Point(100, 200).buffer(50)
    fill(0, 0, 200, 100) # R, G, B, opacidade/alpha
    shape(circulo)
    
    translate(150, 0)
    fatia = circulo.intersection(triangulo)
    fill(0, 0, 200)
    shape(fatia)
    
    translate(0, -10)
    #mordido = triangulo.difference(circulo)
    mordido = triangulo - circulo
    fill(255)
    shape(mordido)


def xyz_box(x, y, z, w, h=None, d=None):
    h = w or h
    d = d or h
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c
  
def apply_rotation(obj, angle, direction=[1, 0, 0], center=[0, 0, 0]):
    rot_matrix = trimesh.transformations.rotation_matrix(angle, direction, center)
    obj.apply_transform(rot_matrix)

def draw_mesh(m):
    py5.push_style()
    py5.no_stroke()
    with py5.begin_closed_shape(py5.TRIANGLES):
        py5.vertices(m.vertices[v]
                     for face in m.faces
                     for v in face)   
    py5.pop_style()
    vs = m.vertices
    bs = m.facets_boundary
    for facet in bs:
        for a, b in facet:
            py5.line(*vs[a], *vs[b])
    