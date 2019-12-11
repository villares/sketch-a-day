add_library('sound') # aviso de que vai usar o microfone

from estrela import Estrela
from boid import Boid
from flock import Flock

def setup():
    global dados, instrumentos, oscP5, novos_dados, estrelas
    global input, loudness
    global flock
    flock = Flock()
    size(800, 600)
    # fullScreen()  # testar se 1 vai para segundo monitor
    background(0)
    # Burocracia para receber o som e analisar o volume
    source = AudioIn(this, 0)
    source.start()
    loudness = Amplitude(this)
    loudness.input(source)
    for i in range(18):
        flock.addBoid(Boid(width / 2, height / 2))
                
def draw():
    fill(0, 10)
    noStroke()
    rect(0, 0, width, height)
    volume = loudness.analyze()
    tamanho = int(map(volume, 0, 0.5, 30, 350))
    # amp =  200 * noise(frameCount * .02)
    flock.run(tamanho)
