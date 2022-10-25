from functools import cache

initial_length = 15 
shorten = 0.8 # reduz 20% quando multiplica
 
def setup():
    size(800, 800)
    color_mode(HSB)
    no_stroke()

def draw(): # laço/loop principal (ele fica repetindo)
    background(0)
    galho(400, 500, initial_length, -HALF_PI)
    
def galho(x, y, length, direction):
    nx, ny, angle = new_point(x, y, length, direction)
    if length > 5:
       xa, ya = galho(nx, ny, length * shorten, direction + angle)
       xb, yb = galho(nx, ny, length * shorten, direction - angle)
       fill((8 * length) % 255, 200, 200, 2 * (120 - length))
       triangle(xa, ya, nx, ny, xb, yb)
    return nx, ny

@cache
def new_point(x, y, length, direction):
    return  (
        x  + length * cos(direction),
        y + length * sin(direction),
        radians(length)
        )

def key_pressed():
    global initial_length
    if key == 'a':
        initial_length += 5
    elif key == 'z':
        initial_length -= 5
        