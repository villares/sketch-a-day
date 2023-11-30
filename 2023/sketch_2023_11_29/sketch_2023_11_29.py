from random import choice

shps = ['A', 'A', 'A', 'A', 'B']
elements = []

def setup():
    global final_x
    size(600, 600)
    elements.append((0, 0, 100, 100, 'debug'))
    final_x = 0
    for y in range(150, 551, 100):  # andando na vertical
        x = 0
        for n in range(30):
            w = random(10, 40)
            h = random_int(1, 5) * 20
            shp = choice(shps) # sorteio
            elements.append((x, y - h, w, h, shp))
            x = x + w
        final_x = max(x, final_x)
    for element in elements[:]:
        xo, yo, wo, ho, coro = element
        elements.append((xo + x, yo, wo, ho, coro)) 
        
def draw():
    background(0, 0, 100)
    no_stroke()
    x_offset = frame_count
    for element in elements:
        fill(255)
        x, y, w, h, shp = element
        if shp ==  'A':
            fill(255)
            margin = 2
            rect(x - x_offset + margin,
                 y + margin,
                 w - 2 * margin,
                 h - 2 * margin)
        elif shp == 'B':
            fill(255, 0, 0)
            circle(x - x_offset, y, w)
#         elif shp == 'debug':
#            fill(0)
#            circle(x - x_offset, y, 10)
       
    if frame_count < final_x and frame_count % 10 == 0:
        save_frame('####.png')