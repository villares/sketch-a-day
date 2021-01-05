add_library('video')

def setup():
    global tamanho, colunas, filas, video
    size(500, 500)
    frameRate(10)
    noStroke()
    # smooth()
    rectMode(CENTER)
    tamanho = 10  # tamanho das células da grade
    colunas = width / tamanho
    filas = height / tamanho
    video = Capture(this, width, height)
    # Começa a captura
    video.start()

def draw():
    escala = 0.05
    t = frameCount / 2
    
    if video.available():
        background(0)
        video.read()
        video.loadPixels()
        # Loopando nas colundas da grade
        for i in range(colunas):
            # Loopando nas filas da grade
            for j in range(filas):
                x = i * tamanho 
                y = j * tamanho 
                loc = x + y * video.width  # acha posição do pixel na captura
                cor = video.pixels[loc]  # pega cor do pixel
                lumin = brightness(cor)  # calcula luminosidade do pixel
                nx = noise(x * escala, (x + y) * escala, t * escala) * 1000 - 500
                ny = noise(y * escala, (x + y) * escala, t * escala) * 1000 - 500
                fill(255)
                fator_bagunca = map(mouseX + lumin / 5, 0, width, 0.01, .1)
                circle( x + tamanho / 2 + nx * fator_bagunca,
                        y + tamanho / 2 + ny * fator_bagunca,
                        tamanho * lumin / 255)
                circle( x + tamanho / 2 - nx * fator_bagunca,
                        y + tamanho / 2 - ny * fator_bagunca,
                        tamanho * lumin / 255)
                circle( x + tamanho / 2 + nx * fator_bagunca,
                        y + tamanho / 2 - ny * fator_bagunca,
                        tamanho * lumin / 255)
                circle( x + tamanho / 2 - nx * fator_bagunca,
                        y + tamanho / 2 + ny * fator_bagunca,
                        tamanho * lumin / 350)
                      
