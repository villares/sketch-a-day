tamanho = 50 # tamanho da bolinha (pequena)
px, py = 250, 250 # posição inicial pra bola
vx = 15 # velocidade no x da bola
# lista de quatro cores
quatro_cores = [color(0),    # preto 
                color(255, 0, 0),  # vermelho
                color(0, 255, 0), # verde
                color(0, 0, 255)] # azul
cor_atual = 0

def setup():
    size(900, 500) # tamanho o desenho
def draw():
    background(255) # fundo branco
    # vamos desenhar uma linha no meio da tela
    line(450, 0, 450, 500) 
    global px, tamanho, cor_atual
    px = px + vx
    fill(quatro_cores[cor_atual])
    circle(px, py, tamanho) # desenha a bola
    if px > 900: # se a posição x > 900
        px = 0 # ponha px valendo 0
        cor_atual = cor_atual + 1
        if cor_atual > 3:
            cor_atual = 0
    # quando ela passar pelo meio aumenta
    if px > 400 and px < 500:  # entre estes valores
        tamanho = 300
    else: # senão
        tamanho = 50
        
