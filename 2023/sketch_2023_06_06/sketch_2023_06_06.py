# Convertendo para Python o clipador de retângulos do John @Introscopia
# https://gist.github.com/Introscopia/e32720497e3c962874e3a3bd406cfa5e
# Usando py5 (https://py5coding.org) para a demo/teste

import py5

rects = []
drag_x = drag_y = None

def setup():
    py5.size(600, 400)
    rects.append(Rect(50, 50, 500, 300))

def draw():
    py5.background(0)
    py5.rect_mode(py5.CORNER)
    py5.fill(255, 200)
    py5.stroke(255)
    for r in rects:
        py5.rect(r.x, r.y, r.w, r.h)
    if drag_x:
        py5.rect_mode(py5.CORNERS)
        py5.stroke(255, 0, 0)
        py5.no_fill()
        py5.rect(py5.mouse_x, py5.mouse_y, drag_x, drag_y)

def mouse_pressed():
    global drag_x, drag_y
    drag_x, drag_y = py5.mouse_x, py5.mouse_y

def mouse_released():
    global drag_x, drag_y
    clip_rects(rects, Rect(min(py5.mouse_x, drag_x), min(py5.mouse_y, drag_y),
                           abs(py5.mouse_x - drag_x), abs(py5.mouse_y - drag_y)))
    drag_x = drag_y = None


class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def clip_rects(rects: list[Rect], knife: Rect) -> None:
    """
    Clipping function that will remove the knife area from the provided Rects,
    creating, resizing or removing axis aligned Rects (mutates the input).
    """
    knife_r = knife.x + knife.w  # knife's right edge x
    knife_b = knife.y + knife.h  # knife's bottom edge y

    for r in rects[:]:  # iterating over a copy of rects
        r_r = r.x + r.w  # rect's right edge x
        r_b = r.y + r.h  # rect's bottom edge y

        if (knife.x >= r_r or
            knife.y >= r_b or
            knife_r <= r.x or
            knife_b <= r.y):
            continue  # not intersecting with knife

        top_in = knife.y > r.y and knife.y < r_b
        bot_in = knife_b > r.y and knife_b < r_b
        lef_in = knife.x > r.x and knife.x < r_r
        rig_in = knife_r > r.x and knife_r < r_r

        total = top_in + bot_in + lef_in + rig_in

        if total == 0:  # FULL CLIP
            r.w = 0   # marks for removal in the end

        elif total == 1:  # RESIZE
            if top_in:
                r.h = knife.y - r.y
            elif bot_in:
                r.y, r.h = knife_b, r_b - knife_b
            elif lef_in:
                r.w = knife.x - r.x
            elif rig_in:
                r.x, r.w = knife_r, r_r - knife_r

        elif total == 2: # CORNERS AND SLICE THROUGH
            if rig_in and bot_in:  # top left corner clipped
                rects.append(Rect(r.x, knife_b, knife_r - r.x, r_b - knife_b))
                r.x, r.w = knife_r, r_r - knife_r
            elif lef_in and bot_in:  # top right corner clipped
                rects.append(Rect(knife.x, knife_b, r_r - knife.x, r_b - knife_b))
                r.w = knife.x - r.x
            elif lef_in and top_in:  # bottom right corner clipped
                rects.append(Rect(knife.x, r.y, r_r - knife.x, knife.y - r.y))
                r.w = knife.x - r.x
            elif rig_in and top_in:  # bottom left corner clipped
                rects.append(Rect(r.x, r.y, knife_r - r.x, knife.y - r.y))
                r.x, r.w = knife_r, r_r - knife_r
            elif lef_in and rig_in:  # vertical slice
                rects.append(Rect(knife_r, r.y, r_r - knife_r, r.h))
                r.w = knife.x - r.x
            elif top_in and bot_in:  # horizontal slice
                rects.append(Rect(r.x, knife_b, r.w, r_b - knife_b))
                r.h = knife.y - r.y

        elif total == 3:  # BITES
            if rig_in and bot_in and top_in:  # Left bite
                rects.append(Rect(r.x, r.y, knife_r - r.x, knife.y - r.y))
                rects.append(Rect(r.x, knife_b, knife_r - r.x, r_b - knife_b))
                r.x, r.w = knife_r, r_r - knife_r
            elif lef_in and bot_in and rig_in:  # top bite
                rects.append(Rect(knife.x, knife_b,  knife.w, r_b - knife_b))
                rects.append(Rect(knife_r, r.y, r_r - knife_r, r.h))
                r.w = knife.x - r.x
            elif lef_in and top_in and bot_in:  # right bite
                rects.append(Rect(knife.x, r.y, r_r - knife.x, knife.y - r.y))
                rects.append(Rect(knife.x, knife_b, r_r - knife.x, r_b - knife_b))
                r.w = knife.x - r.x
            elif rig_in and top_in and lef_in:  # bottom bite
                rects.append(Rect(knife.x, r.y, knife.w, knife.y - r.y))
                rects.append(Rect(knife_r, r.y, r_r - knife_r, r.h))
                r.w = knife.x - r.x

        elif total == 4: # HOLE
            rects.append(Rect(knife.x, r.y, knife.w, knife.y - r.y))
            rects.append(Rect(knife.x, knife_b,  knife.w, r_b - knife_b))
            rects.append(Rect(knife_r, r.y, r_r - knife_r, r.h))
            r.w = knife.x - r.x

    # Filter out 0 area rects
    rects[:] = [r for r in rects if r.w * r.h != 0]


py5.run_sketch()

