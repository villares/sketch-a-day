pontos = set() # with a list it is *much* slower!
        
def setup():
    size(500, 500)
    background(0, 0, 100)
    stroke(255)        
    
def draw():
    noLoop()
    while len(pontos) < 25000:
        x = int(random(width))
        y = int(random(height))
        if (x, y) not in pontos:
             pontos.add((x, y)) # note add() not append
             point(x, y)
    print(len(pontos))
    
