numbers = [10, 20, 50, 30, 10]

spacing = 60
margin = 60

def setup():
    size(800, 400)
    text_size(30)
    stroke_weight(5)
    
def draw():
    background(100)
    fill(255)
    text(repr(numbers), 30, 80)
    x = margin
    for n in numbers:
        fill(n * 3, 128, 255 - n * 4)
        if n != 0:
            circle(x, 200, n)
        else:
            point(x, 200)
        x = x + spacing

def mouse_clicked():
    i = (mouse_x - 60) // spacing + 1
    print(i)
    numbers.insert(i, 0)

def key_pressed():
    if key == 'c':
        numbers.clear()
    elif key == 'p' and numbers:
        numbers.pop()
    elif key == 's':
        numbers.sort()
    elif key == 'r':
        numbers.reverse()
    elif key == 'a':
        numbers.append(int(random_int(2, 60)))
        