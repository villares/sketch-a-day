# py5 imported mode code: learn about it at py5coding.org 

from shapely import Point, Polygon, LineString

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
    