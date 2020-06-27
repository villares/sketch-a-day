from __future__ import unicode_literals

add_library('sound')
bands = 8
smoothingFactor = 0.2
sum = [0] * 8
escala = 20

add_library('video')
mostra_img = False
mostra_bol = True
files = ["a.mp4",  # 0
         "b.mp4",  # 1
         ]
movies = []

current, index = None, None
cw = 5

def setup():
    global current
    # size(970, 520)
    size(770, 415)
    noStroke()
    for f in files:
        m = Movie(this, f)
        m.loop()
        movies.append(m)
    current = movies[1]
    current.play()

    global sample, fft
    global barWidth
    barWidth = width / float(bands)
    sample = SoundFile(this, "Moving Arp.mp3")
    sample.loop()
    fft = FFT(this, bands)
    fft.input(sample)
    
def draw():
    rect(10, 10, 10, 10)
    fft.analyze()
    for i in range(bands):
        e = ((0.5 + i))
        sum[i] +=  (fft.spectrum[i] * e - sum[i]) * smoothingFactor
    
    if current:
        img = current
        background(0)
        w, h = img.width, img.height
        p = w / (1 + h)
        if mostra_img:
            image(img, 0, 0, width, width / p)
        hcw = cw / 2
        for x in range(hcw, width, cw):
            ix = map(x, 0, width, 0, w)
            for y in range(hcw, height, cw):
                iy = map(y, 0, height, 0, h)
                cor = img.get(int(ix), int(iy))
                fill(cor)
                b = brightness(cor)
                banda = int(b / 32)
                circle(x, y, (cw / 2) + cw * sum[banda] * escala)
    else:
        background(200)

def keyPressed():
    global mostra_img, mostra_bol, cw, escala
    if key == "i":
        mostra_img = not mostra_img
    if key == "o":
        mostra_bol = not mostra_bol
    if str(key) in '-_' and cw > 1:
        cw -= 1
    if str(key) in '=+':
        cw += 1
    if str(key) in 'aA' and escala > 1:
        escala -= 1
    if str(key) in 'zZ':
        escala += 1

    global current, index
    if index is not None:
        if keyCode == RIGHT:  # Anterior
            current.stop()
            index = (index + 1) % len(movies)
            current = movies[index]
            current.play()
        elif keyCode == LEFT:  # Seguinte
            current.stop()
            index = (index - 1) % len(movies)
            current = movies[index]
            current.play()
        elif key == "0":
            current.stop()
            index = 0
            current = movies[index]
            current.play()
        elif key == "1":
            current.stop()
            index = 1
            current = movies[index]
            current.play()
    else:
        index = 0
        current = movies[0]
        current.play()


def movieEvent(m):
    m.read()
