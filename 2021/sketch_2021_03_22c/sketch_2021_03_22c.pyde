circles = []

def setup():
    size(500, 500)
    background(0, 0, 100)
    stroke(255)   
    strokeWeight(2)  
    noFill()   
    circles.append(random_circle())

def random_circle():
    r = int(random(2, 50))
    x = int(random(r, width - r))
    y = int(random(r, height - r))
    return (x, y, r)
            
def draw():
    if len(circles) < 1000:
        x, y, r = random_circle()
        for xo, yo, ro in circles:
            if dist(x, y, xo, yo) < r + ro + 4:
                break
        else:
            circles.append((x, y, r))
    for x, y, r in circles:
        circle(x, y, r * 2)
