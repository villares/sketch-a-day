def setup():
    size(500, 500)
    text_align(CENTER, CENTER)  # alinhamento horiz e vertical do texto
    text_size(14)
    num_circulos = 10
    espacamento = width / num_circulos
    filas = colunas = num_circulos
    i = 1  # contador de círculos
    for fila in range(filas): # fila = 0, 1, ... filas - 1
        y = espacamento * fila + espacamento / 2 
        for coluna in range(colunas):  # coluna = 0, 1, ... colunas - 1
            x_original = espacamento * coluna + espacamento / 2
            if fila % 2 == 0:  # fila par
                x = x_original
                fill(200, 0, 0) # preenchimento vermelho
            else:  # fila impar
                x = width - x_original
                fill(0)  # preenchimento preto
            circle(x, y, espacamento * 0.9)
            fill(255)
            text(str(i), x, y)
            i += 1  # i = i + 1  # aumenta em 1 o contador
 
    save('out.png')