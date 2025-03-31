# A zoom interface from John @introscopia https://introscopia.itch.io/

import py5

zpt = {'x': 0, 'y': 0, 'scale': 1, 'amount': 0}  # zoom & pan transformation values
seed = 1

def setup():
    py5.size(500, 500)
    py5.no_stroke()
    
def draw():
    # Your drawing goes here
    with py5.push_matrix():
        py5.translate(zpt['x'], zpt['y'])
        py5.scale(zpt['scale'])
        py5.background(0)
        py5.random_seed(seed)
        w = 500
        for _ in range(10):
            x, y = py5.random(-w/2, w + w/2), py5.random(-w/2, w + w/2)
            for d in range(w * 2, 0, -10):
                py5.fill(py5.random(255),py5.random(255),py5.random(255), 50)
                py5.circle(x, y, d)
    # HUD (Head-Up Display, like if projected on the windscreen, unaffected by zoom & pan)
    with py5.push_style():
        margin = 40
        py5.no_fill()
        py5.stroke(255)
        py5.rect(margin, margin, py5.width - margin * 2, py5.height - margin * 2)
        py5.fill(255)
        py5.text_size(margin / 3)
        py5.text_align(py5.LEFT, py5.TOP)
        py5.text(str(zpt), margin, py5.height - margin / 2)

def mouse_wheel(e):
    xrd = (py5.mouse_x - zpt['x']) / zpt['scale']
    yrd = (py5.mouse_y - zpt['y']) / zpt['scale']
    zpt['amount'] -= e.get_count()
    zpt['scale'] = 1.1 ** zpt['amount']
    zpt['x'] = int(py5.mouse_x - xrd * zpt['scale'])
    zpt['y'] = int(py5.mouse_y - yrd * zpt['scale'])

def mouse_dragged():
    zpt['x'] += py5.mouse_x - py5.pmouse_x
    zpt['y'] += py5.mouse_y - py5.pmouse_y

def key_pressed():
    global seed
    seed += 1

py5.run_sketch()

