def my_box(side):
    front = ((-1, +1, -1),
             (-1, +1, +1),
             (+1, +1, +1),
             (+1, +1, -1),
             )
    back = ((-1, -1, -1),
            (-1, -1, +1),
            (+1, -1, +1),
            (+1, -1, -1),
            )
    left = ((-1, -1, -1),
            (-1, -1, +1),
            (-1, +1, +1),
            (-1, +1, -1),
            )
    right = ((+1, -1, -1),
             (+1, -1, +1),
             (+1, +1, +1),
             (+1, +1, -1),
             )
    down = ((-1, -1, -1),
            (+1, -1, -1),
            (+1, +1, -1),
            (-1, +1, -1),
            )
    top = ((-1, -1, +1),
           (+1, -1, +1),
           (+1, +1, +1),
           (-1, +1, +1),
           )

    faces = ((top, color(200,100, 100)),
             (down, color(0)),
             (right, color(100, 200, 100)),
             (left, color(100,100, 200)),
             (back, color(75)),
             (front, color(75)),
             )

    for pts, shade in faces:
        hs = side / 2  # half side
        fill(shade)
        beginShape()
        for pt in pts:
            x, y, z = pt
            vertex(x * hs, y * hs, z * hs)
        endShape(CLOSE)
