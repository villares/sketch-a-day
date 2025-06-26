numeros = [10, 20, 50, 30, 10]

def setup():
    size(800, 400)
    text_size(30)
    
def draw():
    background(100)
    fill(255)
    text(repr(numeros), 30, 80)
    x = 60
    for numero in numeros:
        fill(numero * 3, 128, 255 - numero * 4)
        circle(x, 200, numero)
        x = x + 60

def key_pressed():
    if key == 'c':
        numeros.clear()
    elif key == 'p' and numeros:
        numeros.pop()
    elif key == 's':
        numeros.sort()
    elif key == 'r':
        numeros.reverse()
    elif key == 'a':
        numeros.append(random_choice((10, 20, 40, 50, 60)))
        