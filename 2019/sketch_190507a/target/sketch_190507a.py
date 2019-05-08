from pytop5js import *
# P5 = _P5_INSTANCE
param = [20, 20, 20, 20]
grid_elem = elem_size = rand_size = rand_posi = 20

def setup():
    # fullScreen()
    createCanvas(600, 600)
 #   	s1 = _P5_INSTANCE.createSlider(0, 255, 100)
	# s1.position(20, 20)
	# s2 = _P5_INSTANCE.createSlider(0, 255, 0);
	# s2.position(20, 50);
	# s3 = _P5_INSTANCE.createSlider(0, 255, 255);
	# s3.position(20, 80);
	# s4 = _P5_INSTANCE.createSlider(0, 255, 255);
	# s4.position(20,110);

    rectMode(CENTER)  # retângulos desenhados pelo centro
    colorMode(HSB, 255, 255, 255)  
    strokeWeight(2)  # espessura de linha 2px
    noFill()  # sem preenchimento
    frameRate(30)  # deixa um pouco mais lento
    
def draw():
	# global grid_elem
	# global elem_size, grid_elem, elem_size
    background(200)  # fundo cinza claro

 	# grid_elem = mouseX / 10

    # trava a randomização entre os ciclos de draw
    # mas varia com o número de colunas na grade
    randomSeed(int(grid_elem / 4))
    # calcula o espaçamento entre os quadrandos
    spac_size = int(width / (grid_elem + 1))
    # para cada coluna um x
    for x in range(spac_size / 2, width, spac_size):
        # para cada linha um y
        for y in range(spac_size / 2, width, spac_size):
            # sorteia um tamanho (se o rand_size > 0)
            square_size = elem_size + rand_size * random(-1, 1)
            stroke(square_size * 3, 255, 128)
            rect(x + rand_posi * random(-1, 1),  # desenha um quadrado
                 y + rand_posi * random(-1, 1),
                 square_size,
                 square_size)

# def mousePressed():
# 	global grid_elem


# This is required by pyp5js to work
start_p5(setup, draw)
