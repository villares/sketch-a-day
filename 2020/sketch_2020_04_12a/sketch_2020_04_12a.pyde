def setup():  
    size(400, 400)
    colorMode(HSB)

def draw():
    background(0)
    noStroke()
    colunas, filas = 10, 10    
    tam_coluna, tam_fila = width / colunas, height / filas
    offset_x, offset_y = tam_coluna / 2., tam_fila / 2. 
    for x, y in grid(colunas, filas, tam_coluna, tam_fila):
        # desenho do elemento em x, y
        s = 25 + 15 * cos(radians(x + y))
        h = 128 + 128 * sin(x - y)
        c = color(h, 255, 200)
        fill(c)
        ellipse(x + offset_x, y + offset_y, s, s)

def grid(colunas, filas, tam_col=1, tam_fil=1):
    """
    Devolve um iterator tuplas das coordenadas.
    Exemplo de uso:
    #    for x, y in grid(10, 10, 12, 12):
    #        rect(x, y, 10, 10)
    """
    range_filas = range(int(filas))
    range_colunas = range(int(colunas))
    for y in range_filas:
        for x in range_colunas:
            yield (x * tam_col, y * tam_fil)

            
