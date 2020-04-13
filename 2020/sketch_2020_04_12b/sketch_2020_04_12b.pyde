# Vamos começar imaginando uma coluna de retângulos

def setup():  
    size(400, 400)
    colorMode(HSB)

def draw():
    background(0)
    noStroke()
    colunas, filas = 10, 10    
    tam_coluna, tam_fila = width / colunas, height / filas
    offset_x, offset_y = tam_coluna / 2., tam_fila / 2. 
    for i in range(colunas):
        x = i * tam_coluna + offset_x
        for j in range(filas):
            y = j * tam_coluna + offset_y
            # desenho do elemento em x, y
            s = 10 + i + j
            h = (x + y) % 256
            c = color(h, 255, 200)
            fill(c)
            ellipse(x, y, s, s)

def keyPressed():
    saveFrame('sketch_2020_04_12b.png')
