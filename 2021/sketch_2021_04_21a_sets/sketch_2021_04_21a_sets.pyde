from __future__ import unicode_literals

def setup():
    global conjuntos
    size(900, 900)
    set1, set2 = set(), set()
    c1x, c1y, c2x, c2y = 300, 300, 600, 300
    textFont(createFont('Source Code Pro Bold', 24))
    for i in range(2000):
        x = random(width)
        y = random(height)
        if dist(x, y, c1x, c1y) < 270:
            set1.add((x, y))
        if dist(x, y, c2x, c2y) < 270:
            set2.add((x, y))
    conjuntos = (
        {'set' : set1 - set2,'label' : 'set1 - set2 (diferença)',
        'visible': True, 'diameter': 20, 'color' : color(200, 0, 0)},                  
        {'set' : set2 - set1,'label' : 'set2 - set1 (diferença)',
        'visible': True, 'diameter': 20, 'color' : color(0, 0, 200)},                           
        {'set' : set1 | set2,'label' : 'set1 | set2 (união)',
        'visible': True, 'diameter': 18, 'color' : color(200, 200, 200)},           
        {'set' : set1, 'label' : 'set1',
        'visible': True, 'diameter': 14, 'color' : color(0, 200, 200)},
        {'set' : set2, 'label' : 'set2',
        'visible': True, 'diameter': 10, 'color' : color(200, 200, 0)},
        {'set' : set1 & set2, 'label' : 'set1 & set2 (intersecção)',
        'visible': True, 'diameter': 6, 'color' : color(0, 200, 0)},
        {'set' : set1 ^ set2, 'label' : 'set1 ^ set2 (diferença simétrica)',
        'visible': True, 'diameter': 6, 'color' : color(255, 0, 255)},
    )             
    
def draw():
    background(100)
    noStroke()
    textSize(24)
    for i, c in enumerate(conjuntos):
        fill(c['color'], 100 + 155 * c['visible'])
        text(c['label'], 30, 650 + i * 30)
        if c['visible']:
            for x, y in c['set']:
                circle(x, y, c['diameter'])        
    
def mouseClicked():
    for i, c in enumerate(conjuntos):
        y = 650 + i * 30 - 20
        if y < mouseY < y + 30 and 30 < mouseX < 30 + textWidth(c['label']):
            c['visible'] = not c['visible']
        
        
