cols = 100
filas = 100
matrix = [[0] * cols for _ in range(filas)]
c_matrix =  [[0] * cols for _ in range(filas)]  # to implement and idea stolen from Carlos @vamoss

geracao = 0
regras_legais = [    # Algumas regras de que gostamos
    [1, 0, 1, 1, 1, 1, 1, 0],  # Regra 125
    [1, 0, 0, 1, 0, 1, 0, 1],  # Regra 169
    [0, 1, 1, 1, 1, 0, 0, 0],  # Regra 30
    [0, 1, 1, 1, 0, 1, 1, 0],  # Regra 110
]
ruleset = regras_legais[2]

checagem = {
  (1, 1, 1): ruleset[7],
  (1, 1, 0): ruleset[6],
  (1, 0, 1): ruleset[5],
  (1, 0, 0): ruleset[4],
  (0, 1, 1): ruleset[3],
  (0, 1, 0): ruleset[2],
  (0, 0, 1): ruleset[1],
  (0, 0, 0): ruleset[0],
  }

def nova_geracao():
    global geracao
    for i in range(cols):
        esq = matrix[(i + cols - 1) % cols][geracao % filas]
        centro = matrix[i][geracao % filas]
        dir = matrix[(i + 1) % cols][geracao % filas]
        result = checagem[(esq, centro, dir)]
        # cor = color(esq * 200, centro * 200, dir * 200)
        cor = color(55 + esq * 200, 55 + centro * 200, 55 + dir * 200)
        matrix[i][(geracao + 1) % filas] =  result 
        c_matrix[i][(geracao + 1) % filas] =  cor             
    geracao += 1
    
def setup():
    size(400, 400)
    matrix[cols / 2][0] = 1 # Começa com "1" no meio da 1ª linha
    frameRate(10)
    noSmooth()

def draw():
    background(0)
    scale(4)
    offset = geracao % filas
    for i in range(cols):
        for j in range(filas):
            y = j - offset
            if y <= 0:
                y = filas + y
            if matrix[i][j] == 1:  # Se a célula i, está viva/ativa/1
               stroke(c_matrix[i][j])# stroke(c_matrix[i][j])
            else:
                stroke(0)
            point(i, y - 1)
            
    nova_geracao()
