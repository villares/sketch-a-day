teclas_apertadas = set()  # conjunto (set) vazio

pa = {'x': 128, 'y': 128,
      'fill': color(0, 0, 200), 'stroke': 0,
      'sobe': 'W', 'desce': 'S',
      'esq': 'A', 'dir': 'D',
      'inv': TAB}

pb = {'x': 384, 'y': 128,
      'fill': color(200, 0, 0), 'stroke': 255,
      'sobe': UP, 'desce': DOWN,
      'esq': LEFT, 'dir': RIGHT,
      'inv': ENTER}

players = (pa, pb)

anima_fundo = False
cor_fundo = 128

def setup():
    size(512, 256)
    textAlign(CENTER, CENTER)
    textSize(15)
    strokeWeight(3)

def draw():
    global cor_fundo
    if anima_fundo:
        cor_fundo = abs(cor_fundo + sin(frameCount / 60.)) % 256
    background(cor_fundo)
    
    for p in players:
        fill(p['fill'])
        stroke(p['stroke'])
        ellipse(p['x'], p['y'], 50, 50)

        # Ajusta a posição dos círculos
        if p['sobe'] in teclas_apertadas:
            p['y'] -= 1
        if p['desce'] in teclas_apertadas:
            p['y'] += 1
        if p['esq'] in teclas_apertadas:
            p['x'] -= 1
        if p['dir'] in teclas_apertadas:
            p['x'] += 1

def keyPressed():
    teclas_apertadas.add(keyCode if key == CODED else chr(keyCode))

    for p in players:
        if p['inv'] in teclas_apertadas:
            p['fill'], p['stroke'] = p['stroke'], p['fill']

def keyReleased():
    global anima_fundo
    
    teclas_apertadas.discard(keyCode if key == CODED else chr(keyCode))

    if keyCode == SHIFT:
        print anima_fundo
        anima_fundo = not anima_fundo
        
    if key == ' ':
        pa['x'], pa['y'] = 128, 128
        pb['x'], pb['y'] = 384, 128
