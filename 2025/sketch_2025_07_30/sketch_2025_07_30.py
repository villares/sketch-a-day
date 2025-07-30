from shapely import Polygon, Point, LineString
import py5

def setup():
    py5.size(800, 400)
    py5.background(0, 150, 150)
    # Dois polígonos, um triângulo e um retângulo
    p = Polygon([(50, 50), (150, 50), (50, 150)])
    py5.shape(p)
    q = Polygon([(70, 70), (150, 70), (150, 150), (70, 150)])
    py5.shape(q)
    py5.translate(150, 0)  # empurra o próximo desenho mais para a direita
    # Podemos pedir para que shapely calcule um recorte, subtração
    L = p - q  # isto equivale  `p.difference(q)`
    py5.shape(L)
    py5.translate(150, 0)  # empurra o próximo desenho mais para a direita
    # Podemos pedir para que shapely calcule um "offset", uma forma expandida
    L_aumentado = L.buffer(10)
    py5.shape(L_aumentado)
    py5.translate(150, 0)  # empurra o próximo desenho mais para a direita
    # Podemos fazer a fusão, união entre formas (mas o operador + não funciona)
    forma_unida = p.union(q)  # `p + q` não funciona! 
    py5.shape(forma_unida)
    py5.translate(150, 0)  # empurra o próximo desenho mais para a direita
    # Podemos fazer um furo, subtraindo uma versão encolhida da própria forma
    forma_reduzida = forma_unida.buffer(-10)  # offset negativo, para dentro
    forma_com_furo = forma_unida.difference(forma_reduzida)
    py5.shape(forma_com_furo)    
    py5.reset_matrix()  # volta sistema de coordenadas para a origem no canto
    py5.translate(0, 200)  # empurra os próximos desenhos para baixo
    # Para fazer um círculo podemos fazer um offset de um ponto.
    c = Point(100, 100).buffer(50)  # o valor buffer é o raio
    py5.shape(c)
    # Um exemplo de uma linha e uma linha com buffer
    ls = LineString([(200, 50), (450, 50)])
    lsb = LineString([(200, 100), (450, 100)]).buffer(10)
    py5.shape(ls)
    py5.shape(lsb)
    # Podemos calcular a intersecção entre duas formas
    ca = Point(550, 100).buffer(50)
    py5.shape(ca)
    cb = Point(600, 100).buffer(50)
    py5.shape(cb)
    py5.translate(150, 0)
    ci = ca.intersection(cb)
    py5.shape(ci)
    # exportando
    py5.save_frame('shapely_demo.png')
    
py5.run_sketch()