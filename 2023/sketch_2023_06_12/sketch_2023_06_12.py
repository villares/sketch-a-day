"""
PONG - Com dois poteciômetros
"""
from inputs import get_arduino

# ARDUINO
POT_AMARELO = 0   # Pino que vai ser lido controle 'jogador Amarelo'
POT_VERDE = 5   # Pino que vai ser lido controle 'jogador Verde'
SERIAL = 0  # MUDE para o índice do seu Arduino na lista de portas seriais!

TAM_BOLA = 10
MEIA_BOLA = TAM_BOLA / 2
TAM_JOGADOR = 80
MEIO_JOGADOR = TAM_JOGADOR / 2
game_over = False

vx, vy = 0, 0

def setup():
    """ Executado no início """
    size(900, 500)
    rect_mode(CENTER)
    
    # ARDUINO SETUP
    global arduino
    arduino = get_arduino()
    if arduino is None:
        exit_sketch()
    # POSITIONS
    global x, y, p1x, p2x
    x = width / 2
    y = height / 2
    p1x = MEIA_BOLA
    p2x = width - MEIA_BOLA


def draw():
    """ Desenho dos frames """
    global x, y, vx, vy, p1y, p2y
    global game_over
    background(0)
    p1y = remap(arduino.analog_read(POT_AMARELO), 0, 1023, 0, height)
    p2y = remap(arduino.analog_read(POT_VERDE), 0, 1023, 0, height)
    # desenha bola
    fill(0, 0, 255)
    rect(x, y, TAM_BOLA, TAM_BOLA)
    # anda com a bola
    if not game_over:
        x = x + vx
        y = y + vy
    else:
        text_size(100)
        text_align(CENTER, CENTER)
        text("GAME OVER", width / 2, height / 2)
    # regras de rebatimento da bola
    if y < MEIA_BOLA or y > height - MEIA_BOLA:
        vy = -vy
    # checa rebatimento player 1 (lareral esquerda)
    if x < MEIA_BOLA:
        if p1y + MEIO_JOGADOR > y > p1y - MEIO_JOGADOR:
            vx = -vx
        else:
            game_over = True
    # checa rebatimento player 2 (lateral direita)
    if x > width - MEIA_BOLA:
        if p2y + MEIO_JOGADOR > y > p2y - MEIO_JOGADOR:
            vx = -vx
        else:
            game_over = True

            # desenha jogadores
    fill(255, 255, 0)
    rect(p1x, p1y, TAM_BOLA, TAM_JOGADOR)
    fill(0, 255, 0)
    rect(p2x, p2y, TAM_BOLA, TAM_JOGADOR)


def key_pressed():
    global x, y, vx, vy, game_over
    if key == ' ':
        if game_over:
            x = width / 2
            y = height / 2
            game_over = False
        if random(100) > 50:
            vx = -5
        else:
            vx = 5
        if random(100) > 50:
            vy = -2
        else:
            vy = 2

