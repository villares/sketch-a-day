from pytop5js import *
grid_elem = elem_size = rand_size = rand_posi = 20
# P5 = _P5_INSTANCE
s1 = s2 = s3 = s4 = None

def setup():
	# s1 = _P5_INSTANCE.createSlider(0, 255, 100);
	# s1.position(20, 20);
	# s2 = _P5_INSTANCE.createSlider(0, 255, 0);
	# s2.position(20, 50);
	# s3 = _P5_INSTANCE.createSlider(0, 255, 255);
	# s3.position(20, 80);
	# s4 = _P5_INSTANCE.createSlider(0, 255, 255);
	# s4.position(20,110);


    # fullScreen()
    createCanvas(600, 600)
    rectMode(CENTER)  # retângulos desenhados pelo centro
    colorMode(HSB, 255, 255, 255)  
    strokeWeight(2)  # espessura de linha 2px
    noFill()  # sem preenchimento
    frameRate(30)  # deixa um pouco mais lento
    
def draw():
	global grid_elem
    background(200)  # fundo cinza claro

    # # 0 a 63, número de linhas e colunas na grade
    # grid_elem = s1.value()
    # # 0 a 63, tamanho base de cada quadrado
    # elem_size = int(input.analog(2) / 16)
    # # 0 a 63, ativa faixa entre -64 e 63 para randomizar tamanho
    # rand_size = int(input.analog(3) / 16)
    # # 0 a 63, ativa faixa equivalente para randomizar a posição
    # rand_posi = int(input.analog(4) / 16)

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

# This is required by pyp5js to work
start_p5(setup, draw)
