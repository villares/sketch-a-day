

def setup():
    size(500, 500)
    
    v = Py5Vector(100, 100)
    new_mag = -10
    if new_mag < 0:
        v, new_mag = -v, -new_mag
    v.mag = new_mag
    print(v)