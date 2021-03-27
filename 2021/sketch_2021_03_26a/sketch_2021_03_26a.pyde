
tam_tabuleiro = 15
tam_casa = 35
meia_casa = tam_casa / 2
borda = 36
tabuleiro_a = [(1, 1),(2, 1),(3, 1),(4, 1),
               (6, 6),
               (10, 6), (11, 7), (12, 6)
              ]

tabuleiro_b = [(1, 1),(2, 1),(3, 1),(4, 1),
               (6, 6),
               (6, 10), (7, 11), (6, 12)
              ]

def setup():
    size(1200, 600)
    textAlign(CENTER, CENTER)
    
def draw():
    background(200)
    draw_tabuleiro(tabuleiro_a)
    translate(600, 0)
    draw_tabuleiro(tabuleiro_b)
    
def draw_tabuleiro(tabuleiro):
    for i in range(tam_tabuleiro):
        label(i)
        for j in range(tam_tabuleiro):
            label(j, vertical=True)
            if (i, j) in tabuleiro:
                fill(0)
            else:
                fill(255)
            square(i * tam_casa + borda, 
                   j * tam_casa + borda, 
                   tam_casa)

        
def mouseClicked():
    i = (mouseX - borda) / tam_casa 
    j = (mouseY - borda) / tam_casa 
    if 0 <= i < tam_tabuleiro and 0 <= j < tam_tabuleiro:
        if (i, j) in tabuleiro_a:
            tabuleiro_a.remove((i, j))
        else:
            tabuleiro_a.append((i, j))
    print(tabuleiro_a)
     
def label(n, vertical=False):
    fill(0)
    pos =  n * tam_casa + borda + meia_casa 
    if vertical:
        text(n, meia_casa, pos)
    else:
        text(n, pos, height - meia_casa * 1.2)
