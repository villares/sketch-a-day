import py5

from villares.arcs import b_circle_arc

def setup():
    py5.size(600, 600)
    r = 30
    for y in range(0, py5.height + 1, r * 2):
        with py5.begin_shape():
            for i, x in enumerate(range(r, py5.width, r * 2)):
                if i % 2 == 0:
                    b_circle_arc(x, y, r, py5.PI, py5.PI, mode=2)
                else:
                    b_circle_arc(x, y, r, py5.PI, -py5.PI, mode=2)
            w, i_offset = x, i
            for i, x in enumerate(range(w, 0, -r * 2)):
                if (i + i_offset) % 2 == 0:
                    b_circle_arc(x, y + r, r, 0, -py5.PI, mode=2)
                else:
                    b_circle_arc(x, y + r, r, 0, py5.PI, mode=2)
    py5.save(__file__[:-3] + '.png')
py5.run_sketch(block=False)
