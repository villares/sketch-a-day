from inputs import InputInterface

def setup():
    global inputs
    size(800, 800)
    color_mode(HSB)
    rect_mode(CENTER)  # retângulos desenhados pelo centro
    no_stroke()  # sem contorno
    frame_rate(30)
    # Ask user for Arduino port, uses slider if none is selected`
    inputs = InputInterface()

def draw():
    background(0)  
    grid_elem = int(inputs.analog_read(1) / 16)  # 0 a 63 linhas e colunas na grade
    elem_size = int(inputs.analog_read(2) / 16)  # 0 a 63 tamanho base dos quadrados
    rand_size = int(inputs.analog_read(3) / 16)  # escala a randomização do tamanho
    rand_posi = int(inputs.analog_read(4) / 16)  # escala a randomização da posição
    # trava a random entre os ciclos de draw
    # mas varia com o número de colunas na grade
    random_seed(int(inputs.analog_read(1) / 4))
    # espaçamento entre os quadrandos
    spac_size = int(width / (grid_elem + 1))
    for x in range(spac_size // 2, width, spac_size):  # um x p/ cada coluna
        for y in range(spac_size // 2, width, spac_size):  # um y p/ cada linha
            # sorteia um tamanho (se o rand_size > 0)
            square_size = elem_size + rand_size * random(-1, 1)
            offsetX = rand_posi * random(-1, 1)
            offsetY = rand_posi * random(-1, 1)
            HUE = (remap(offsetX + offsetY, -64, 64, 0, 255) + 32) % 255
            SAT = remap(square_size, 0, 63, 0, 255)
            fill(HUE, SAT, 255, 200)
            rect(x + offsetX,  # desenha um quadrado
                 y + offsetY,
                 square_size,
                 square_size)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    inputs.update()


def key_pressed():
    global GIF_EXPORT
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'h':
        inputs.help()

    inputs.key_pressed()

def key_released():
    inputs.key_released()

def mouse_wheel(e):
    inputs.mouse_wheel(e)