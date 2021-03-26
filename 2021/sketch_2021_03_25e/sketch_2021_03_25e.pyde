
tam_tabuleiro = 15
tam_casa = 35
meia_casa = tam_casa / 2
borda = 36
tabuleiro_a = {(1, 1): "C",
                (2, 1): "C",
                (3, 1): "C",
                (4, 1): "C",
                (6, 6): "S",
                (10, 6): "H",
                (11, 7): "H",
                (12, 6): "H",
               }

cores = {"C": color(100, 0, 0),
         "S": color(0, 0, 100),
         "H": color(0, 100, 0),
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
                fill(cores[c])
            square(i * tam_casa + borda, 
                       j * tam_casa + borda, 
                       tam_casa)
            if c:
                fill(255)
                text(c, i * tam_casa + borda + meia_casa, 
                        j * tam_casa + borda + meia_casa) 

        
def mouseClicked():
    i = (mouseX - borda) / tam_casa 
    j = (mouseY - borda) / tam_casa 
    c = tabuleiro_a.get((i, j))
    if 0 <= i < tam_tabuleiro and 0 <= j < tam_tabuleiro:
        if not c:
            tabuleiro_a[(i, j)] = "S"
        elif c == "S":
            tabuleiro_a[(i, j)] = "C"
        else:
            tabuleiro_a[(i, j)] = None 
    print(tabuleiro_a)
     
def label(n, vertical=False):
    fill(0)
    pos =  n * tam_casa + borda + meia_casa 
    if vertical:
        text(n, meia_casa, pos)
    else:
        text(n, pos, height - meia_casa)
