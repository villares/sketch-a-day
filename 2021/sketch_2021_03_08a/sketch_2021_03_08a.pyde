from __future__ import unicode_literals

botoes = ({"name": "grey", "y": 0, "func": (lambda: stroke(128))},
          {"name": "green", "y": 20, "func": (lambda: stroke(0, 200, 0))},
          {"name": "blue", "y": 40, "func": (lambda: stroke(0, 0, 200))},
          )

menu_clicked = False

def setup():
    size(300, 300)
    stroke(128)
    strokeWeight(5)
    
def draw():
    background(200)
    noFill()
    circle(150, 150, 200)
    desenha_botoes()
    
def desenha_botoes():
    textAlign(LEFT, CENTER)
    if menu_clicked:
        x, y = menu_clicked
        for b in botoes:
            if mouse_over(b):
                fill(255)
            else:
                fill(0)
            text(b['name'], x, y + b['y'])        

def mouse_over(b):
    x, y = menu_clicked
    return (x < mouseX < x + textWidth(b['name']) and 
            y + b['y'] < mouseY < y + b['y'] + 20) 

def mouseClicked():
    global menu_clicked
    if mouseButton == RIGHT and not menu_clicked:
        menu_clicked = (mouseX, mouseY)
    elif menu_clicked:
        for b in botoes:
            if mouse_over(b):
                print(b['name'])
                b['func']()
                break
        else:
            print(None);
        menu_clicked = False
