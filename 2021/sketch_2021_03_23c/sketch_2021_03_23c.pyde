circles = []
last_addition = millis()

def setup():
    size(500, 500)
    background(0, 0, 200)
    noFill()

def random_point():
    x = int(random(width))
    y = int(random(height))
    return (x, y)

def valid_circle(x, y, r):
    if not r < x < width - r:
        return False
    if not r < y < height - r:
        return False
    if len(circles) == 0:
        return True
    for xo, yo, ro in circles:
        if dist(x, y, xo, yo) < r + ro + 2:
            return False
    return True
            
def draw():
    global last_addition
    for x, y, r in circles:
        circle(x, y, r * 2);
    d = millis() - last_addition
    if d < 5000:
        x, y = random_point()
        for r in range(100, 1, -1):
            if valid_circle(x, y, r):
                circles.append((x, y, r))
                print(d)
                last_addition = millis()
                break
    else:
        print("no more")
        noLoop()
        
