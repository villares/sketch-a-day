from __future__ import unicode_literals

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

def draw():
    rect(10, 10, 10, 10)
    if current:
        img = current
        background(0)
        w, h = img.width, img.height
        p = w / h
        if mostra_img:
            image(img, 0, 0, width, width / p)
        hcw = cw / 2
        for x in range(hcw, width, cw):
            ix = map(x, 0, width, 0, w)
            for y in range(hcw, height, cw):
                iy = map(y, 0, height, 0, h)
                cor = img.get(int(ix), int(iy))
                fill(cor)
                circle(x, y, cw)
    else:
        background(200)

def keyPressed():
    global mostra_img, mostra_bol, cw
    if key == "i":
        mostra_img = not mostra_img
    if key == "o":
        mostra_bol = not mostra_bol
    if str(key) in '-_' and cw > 1:
        cw -= 1
    if str(key) in '=+':
        cw += 1
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
