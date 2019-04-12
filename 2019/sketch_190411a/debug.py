DEBUG = False

def debug_text(name, points, enum=False):
    if DEBUG:
        for i, p in enumerate(points):
            with push():
                
                fill(255, 0, 0)
                if enum:
                    translate(0, -5, 10)
                    text(name + "-" + str(i), *p)
                else:
                    translate(10, 10, 10)
                    text(name[i], *p)
