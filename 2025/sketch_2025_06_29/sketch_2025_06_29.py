numbers = [10, 20, 50, 30, 10]

spacing = 60
margin = 60

def setup():
    size(800, 400)
    cursor(CROSS)
    stroke_weight(3)
    
def draw():
    global i
    background(200, 100, 100)
    fill(255)
    text_size(spacing * 0.7)
    text_align(LEFT, CENTER)
    text(repr(numbers), spacing * 0.2, 80)
    x = margin
    for n in numbers:
        fill(n * 3, 128, 255 - n * 4)
        if n != 0:
            circle(x, 200, n)
        else:
            point(x, 200)
        x = x + spacing
    i = constrain(int(mouse_x - margin + spacing / 2) // spacing,
                  0, len(numbers) + 1)
    text_size(20)
    fill(255)
    text_align(CENTER, CENTER)
    text(i, mouse_x, mouse_y)

def mouse_clicked():
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
        