add_library('sound')

def setup():
    global amplitude, amostras, onda
    size(600, 500)
    fonte = AudioIn(this, 0)
    fonte.start()
    amplitude = Amplitude(this)
    amplitude.input(fonte)
    amostras = 60
    onda = Waveform(this, amostras)
    onda.input(fonte)

def draw():
    volume = amplitude.analyze()
    background(volume * 1000)
    lista_amostras = onda.analyze()
    for i, a in enumerate(lista_amostras):
        fill(128)
        rect(i * 10, 300, 10, 300 * a)
