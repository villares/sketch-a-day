# https://twitter.com/nicolasbaez/status/1431004791958904835?s=20
# 3D polar to rectangular and back

r = 320

def setup():
    size(800, 800, P3D)
    # hint(ENABLE_DEPTH_SORT)
    hint(ENABLE_DEPTH_TEST)
    # hint(ENABLE_DEPTH_MASK)
    
def draw():
    background(240)
    translate(width / 2, height / 2)
    rotateX(frameCount / 10.0)
    for da in range(90):
        a = radians(da * 4)
        for db in range(90):
            s = 5
            # if (da, db) == (mouseX, mouseY):
            #     s = 20
            b = radians(db * 4)
            x = r * sin(a) * cos(b)
            y = r * sin(a) * sin(b)
            z = r * cos(a)
            stroke(0)
            fill(0, 0, 255)
            push()
            translate(x, y, z)
            box(s)
            pop()
            oa = TWO_PI - acos(z / r) - frameCount / 20.0
            ob = atan2(y, x) + PI + frameCount / 10.0
            # print(degrees(oa), da * 4, degrees(ob), db * 4)
            x = r * sin(oa) * cos(ob)
            y = r * sin(oa) * sin(ob)
            z = r * cos(oa)
            stroke(0)
            push()
            translate(x, y, z)
            fill(255, 0, 0)
            box(s)
            pop()
        
