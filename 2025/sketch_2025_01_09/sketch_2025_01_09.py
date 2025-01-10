import numpy as np

cols = 100
rows = 100
matrix = np.zeros((100, 100), dtype=int) 
c_matrix =  np.zeros((100, 100), dtype=int) # to implement and idea stolen from Carlos @vamoss
gen = 0
nice_rules = [    # Some rules we like
    [1, 0, 1, 1, 1, 1, 1, 0],  # rule 125
    [1, 0, 0, 1, 0, 1, 0, 1],  # rule 169
    [0, 1, 1, 1, 1, 0, 0, 0],  # rule 30
    [0, 1, 1, 1, 0, 1, 1, 0],  # rule 110
]
ruleset = nice_rules[2]

def setup():
    size(800, 800)
    no_smooth()
    no_stroke()

    matrix[cols // 2, 0] = 1 # Começa com "1" no meio da 1ª linha
    frame_rate(10)



def draw():
    background(200)
    scale(8)
    offset = gen % rows
    for i in range(cols):
        for j in range(rows):
            y = j - offset
            if y <= 0:
                y = rows + y
            if matrix[i, j] == 1:  # Se a célula i, está viva/ativa/1
               stroke(c_matrix[i, j])# stroke(c_matrix[i, j])
            else:
                stroke(200)
            point(i, y - 1)
            
    new_gen()

def new_gen():
    global gen
    for i in range(cols):
        left = matrix[(i + cols - 1) % cols, gen % rows]
        centre = matrix[i, gen % rows]
        right = matrix[(i + 1) % cols, gen % rows]
        result = ruleset[left  * 4 +  centre * 2 +  right * 1]
        cor = color(55 + left * 100, 55 + centre * 100, 55 + right * 100)
        matrix[i, (gen + 1) % rows] =  result 
        c_matrix[i, (gen + 1) % rows] =  cor             
    gen += 1
    
def key_pressed():
    save_frame('####.png')
