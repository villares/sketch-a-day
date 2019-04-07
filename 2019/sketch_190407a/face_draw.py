

def face_draw(points):
    beginShape()
    for p in points:
        vertex(*p)
    endShape(CLOSE)
