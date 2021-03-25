
tam_tabuleiro = 10
tam_casa = 54
meia_casa = tam_casa / 2
borda = 36
tabuleiro_a = {(1, 1): 1,
               (2, 1): 1,
               (3, 1): 1,
               (6, 6): 3,
               }

def setup():
    size(600, 600)
    textAlign(CENTER, CENTER)
    
def draw():
    background(200)
    for i in range(tam_tabuleiro):
        label(i)
        for j in range(tam_tabuleiro):
            label(j, vertical=True)
            c = tabuleiro_a.get((i, j))
            if not c:
                fill(255)
            else:
                fill(c * 32)
            square(i * tam_casa + borda, 
                   j * tam_casa + borda, 
                   tam_casa)

        
def mouseClicked():
    i = (mouseX - borda) / tam_casa 
    j = (mouseY - borda) / tam_casa 
    c = tabuleiro_a.get((i, j))
    if 0 <= i < tam_tabuleiro and 0 <= j < tam_tabuleiro:
        if not c:
            tabuleiro_a[(i, j)] = 1
        else:
            tabuleiro_a[(i, j)] = (c + 1) % 4
    print(tabuleiro_a)
     
def label(n, vertical=False):
    fill(0)
    pos =  n * tam_casa + borda + meia_casa 
    if vertical:
        text(n, meia_casa, pos)
    else:
        text(n, pos, height - meia_casa / 2)
