from buttons import Button

estado_inicial = True

b_color = color(255, 0, 0)

def setup():
    global b1, b2
    size(400, 400)
    b1 = Button(100, 150, 100, 50,
                txt="black\nbackground",
                func=black)
    b2 = Button(100, 250, 100, 50,
                txt="red\nbackground",
                func=vermelho)

def draw():
    background(b_color)
    Button.display_all(mousePressed)


def black():
    global b_color
    b_color = color(0)

def vermelho():
    global b_color
    b_color = color(255, 0, 0)
