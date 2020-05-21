from __future__ import unicode_literals

teclas_apertadas = set()  # conjunto (set) vazio
nomes = {UP: '↑',
         DOWN: '↓',
         LEFT: '←',
         RIGHT: '→',
         ALT: 'Alt',
         CONTROL: 'Ctrl',
         SHIFT: 'Shift',
         BACKSPACE: 'Bcksp',
         TAB: 'Tab',
         ENTER: 'Enter',
         RETURN: 'Return',
         ESC: 'Esc',
         DELETE: 'Del',
         524: 'Meta',
         525: 'Menu',
         65406: 'AltGr',
         155: 'Insert',
         36: 'Home',
         35: 'End',
         33: 'PgUp',
         34: 'PgDwn',
         144: 'NumLk',
         ' ': 'espaço',
         }

def setup():
    size(512, 256)
    textAlign(CENTER, CENTER)
    textSize(15)
    strokeWeight(3)

def draw():
    if ' ' in teclas_apertadas:
        background(0)
    else:
        background(50, 100, 50)
    
    for i, k in enumerate(sorted(teclas_apertadas)):
        n = nomes.get(k, k)
        x = i * 64
        fill(0, x / 2, 200)
        rect(x, 96, 64, 64)
        fill(255)
        text(n, x + 32, 128)

def keyPressed():
    if key != CODED:
        teclas_apertadas.add(chr(keyCode))
    else:
        teclas_apertadas.add(keyCode)

    # isso impede que o sketch seja encerrado com ESC!
    if key == ESC:
        this.key = ' '

def keyReleased():
    if key != CODED:
        teclas_apertadas.discard(chr(keyCode))
    else:
        teclas_apertadas.discard(keyCode)
