# colorful tree / árvore colorida
 
def setup():
    size(800, 800)
    color_mode(HSB)
    no_stroke()

def draw(): # laço/loop principal (ele fica repetindo)
    background(0)
    galho(400, 500, 120, -HALF_PI)
    
def galho(x, y, length, direction):
    nx = x  + length * cos(direction)
    ny = y  + length * sin(direction)
    angle = radians(length)
    #line(x, y, nx, ny) #x1, y1, x2, y2
    shorten = 0.8 # reduz 20% quando multiplica
    if length > 5:
       xa, ya = galho(nx, ny, length * shorten, direction + angle)
       xb, yb = galho(nx, ny, length * shorten, direction - angle)
       fill((32 * direction) % 255, 200, 200, 2 * (120 - length))
       triangle(xa, ya, nx, ny, xb, yb)
    return nx, ny 