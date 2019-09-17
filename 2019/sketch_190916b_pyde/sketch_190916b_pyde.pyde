add_library('sound') # aviso de que vai usar o microfone

x = 10

def setup():
    global input, loudness
    size(640, 360)
    fill(255, 0, 150)
    # Burocracia para receber o som e analisar o volume
    input = AudioIn(this, 0)
    input.start()
    loudness = Amplitude(this)
    loudness.input(input)

def draw():
    global x
    volume = loudness.analyze()
    tamanho = int(map(volume, 0, 0.5, 1, 350))
    if tamanho > 200: # se o tamanho for maior que 200
        fill(0, 0, 200, 100) # azul
    else:
        fill(200, 0, 0, 100) # vermelho
    if tamanho < 50:
        fill(255, 200) # branco meio transparente
        rect(0, 0, width, height) # retângulo que pega a tela toda
    circle(x, 180, tamanho)
    x = x + 10
    if x > width:
        x = 0
    
def keyPressed():
    saveFrame("####.png")
