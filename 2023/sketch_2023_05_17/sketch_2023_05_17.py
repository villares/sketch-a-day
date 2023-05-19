from collections import deque

import py5

rotations = 8
margin = 100
vx, vy = 2, 3
brush_x, brush_y = 200, 200
positions = deque(maxlen=500)


def setup():
    py5.size(600, 600)
    py5.no_stroke()
    py5.color_mode(py5.HSB)  # Hue, Saturation, Brightness
    py5.background(0)


def draw():
    global brush_x, brush_y, vx, vy
    py5.background(0)
    angle = py5.radians(360 / rotations)
    # moves 0, 0 to the center of the canvas
    py5.translate(py5.width / 2, py5.height / 2) 
    for i in range(rotations):  # repeats "rotations" times
        py5.rotate(angle)
        for j, (x, y) in enumerate(positions):
            py5.fill((py5.frame_count + j / 10) % 255, 200, 200)
            py5.circle(x - py5.width / 2, y - py5.height / 2, 5)

    positions.append((brush_x, brush_y))

    vx = vx + py5.random(-0.5, 0.5)
    vy = vy + py5.random(-0.5, 0.5)

    if abs(vx) > 5:
        vx = 0
    if abs(vy) > 5:
        vy = 0

    brush_x = brush_x + vx
    brush_y = brush_y + vy

    if brush_x > (py5.width - margin) or brush_x < margin:
        vx = -vx
    if brush_y > (py5.height - margin) or brush_y < margin:
        vy = -vy

py5.run_sketch()
