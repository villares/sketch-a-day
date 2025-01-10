import numpy as np

cols = 100
filas = 100
matrix = np.zeros((100, 100), dtype=int) #[[0] * cols for _ in range(filas)]
# to implement and idea stolen from Carlos @vamoss
c_matrix =  np.zeros((100, 100), dtype=int) 

geracao = 0
regras_legais = [    # Algumas regras de que gostamos
    [1, 0, 1, 1, 1, 1, 1, 0],  # Regra 125
    [1, 0, 0, 1, 0, 1, 0, 1],  # Regra 169
    [0, 1, 1, 1, 1, 0, 0, 0],  # Regra 30
    [0, 1, 1, 1, 0, 1, 1, 0],  # Regra 110
]
ruleset = regras_legais[3]


def setup():
    size(800, 800)
    no_smooth()
    no_stroke()

    matrix[cols // 2][0] = 1 # Começa com "1" no meio da 1ª linha
    frame_rate(10)



def draw():
    background(200)
    scale(8)
    offset = geracao % filas
    for i in range(cols):
        for j in range(filas):
            y = j - offset
            if y <= 0:
                y = filas + y
            if matrix[i][j] == 1:  # Se a célula i, está viva/ativa/1
               stroke(c_matrix[i][j])# stroke(c_matrix[i][j])
            else:
                stroke(200)
            point(i, y - 1)
            
    nova_geracao()

def nova_geracao():
    global geracao
    for i in range(cols):
        esq = matrix[(i + cols - 1) % cols][geracao % filas]
        centro = matrix[i][geracao % filas]
        dir = matrix[(i + 1) % cols][geracao % filas]
        result = ruleset[esq  * 4 +  centro * 2 +  dir * 1]
        cor = color(55 + esq * 100, 55 + centro * 100, 55 + dir * 100)
        matrix[i][(geracao + 1) % filas] =  result 
        c_matrix[i][(geracao + 1) % filas] =  cor             
    geracao += 1
    

