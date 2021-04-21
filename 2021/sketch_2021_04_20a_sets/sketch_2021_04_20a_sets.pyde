set1, set2 = set(), set()
c1x, c1y, c2x, c2y = 300, 300, 600, 300

def setup():
    size(900, 600)
    noStroke()    
    for i in range(2000):
        x = random(width)
        y = random(height)
        if dist(x, y, c1x, c1y) < 270:
            set1.add((x, y))
        if dist(x, y, c2x, c2y) < 270:
            set2.add((x, y))
            
def draw():
    background(100, 0, 0)
    draw_set(set1, 15, color(200, 200, 0))
    draw_set(set2, 10, color(0, 0, 255))
    simetric_dif = set1 ^ set2
    draw_set(simetric_dif, 5, color(255, 0, 0))
    intersection = set1 & set2
    draw_set(intersection, 5, color(0))
                
def draw_set(set, tam, cor):
    fill(cor)
    for x, y in set:
        circle(x, y, tam)
        
        
