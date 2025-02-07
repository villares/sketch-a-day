from itertools import combinations

def setup():
    size(600, 600)
    start()
    
def start():
    global i, equipos, combos
    i = 0
    equipos = {mock_name(): (random(100, 500),
                           random(100, 500))
                for _ in range(10)}
    nomes = list(equipos)
    combos = list(combinations(nomes, 2))
    
def draw():
    global i
    background(200)
    for nome, (x, y) in equipos.items():
        fill(0)
        stroke(0)
        circle(x, y, 5)
        text(nome, x + 5, y)
        
    for a, b in combos:
        xa, ya = equipos[a]
        xb, yb = equipos[b]
        d = dist(xa, ya, xb, yb)
        if d < i * 20:
            line(xa, ya, xb, yb)
    if i < 10:
        save_frame(f'{nome}-{i}.png')
    else:
        i = 9
    i += 1
 
def key_pressed():
    start()
    
def mock_name():
    numeros = '0123456789ABCDEF'
    prefixo = random_choice('ABCDEF')
    nome = random_choice(numeros) + random_choice(numeros)
    return prefixo + nome 
