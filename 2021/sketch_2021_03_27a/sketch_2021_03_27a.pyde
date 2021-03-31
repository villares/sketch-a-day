
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

visivel_a = []
visivel_b = []

def setup():
    size(1200, 600)
    textAlign(CENTER, CENTER)
    
def draw():
    background(200)
    draw_tabuleiro(tabuleiro_a, visivel_a)
    translate(600, 0)
    draw_tabuleiro(tabuleiro_b, visivel_b)
    
def draw_tabuleiro(tabuleiro, visivel):
    for i in range(tam_tabuleiro):
        for j in range(tam_tabuleiro):
            if (i, j) in visivel:
                if (i, j) in tabuleiro:
                    fill(0)
                else:
                    fill(255)
            else:
                fill(128)
            square(i * tam_casa + borda, 
                   j * tam_casa + borda, 
                   tam_casa)
            
    for n in range(tam_tabuleiro):
        fill(0)
        pos =  n * tam_casa + borda + meia_casa 
        text(n, meia_casa, pos)
        text(n, pos, height - meia_casa * 1.2)
    
def mouseClicked():
    mnta = mouse_no_tabuleiro(mouseX, mouseY)    
    modifica_tabuleiro(mnta, visivel_a)     
    mntb = mouse_no_tabuleiro(mouseX - 600, mouseY)    
    modifica_tabuleiro(mntb, visivel_b)
        
def modifica_tabuleiro(pos, visivel):
    if pos in visivel:
        visivel.remove(pos)
    else:
        visivel.append(pos)

def mouse_no_tabuleiro(x, y):
    i = (x - borda) / tam_casa 
    j = (y - borda) / tam_casa 
    if 0 <= i < tam_tabuleiro and 0 <= j < tam_tabuleiro:
        return (i, j)
    else:
        return None
