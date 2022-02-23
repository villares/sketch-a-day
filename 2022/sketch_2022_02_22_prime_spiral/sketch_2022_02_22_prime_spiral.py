# The Prime Spiral (aka Ulam Spiral)
# The Coding Train / Daniel Shiffman
# https://thecodingtrain.com/CodingChallenges/167-prime-spiral.html
# https://youtu.be/a35KWEjRvc0
# Prime Spiral: https://editor.p5js.org/codingtrain/sketches/0Ud-XsaYb

# State of spiral
step = 1
state = 0
num_steps = 1
turn_counter = 1
# Scale / resolution
step_size = 5

# Function to test if number is prime
def is_prime(value):
    if value == 1:
        return False
    i = 2
    while i * i <= value:
        if value % i == 0:
            return False   
        i += 1 
    return True

def setup():
    global x, y, px, py
    size(500, 500)
    # set up spiral
    x = width / 2
    y = height / 2
    px = None
    py = None
    background(0)

def draw():
    global step, state, num_steps, turn_counter
    global x, y, px, py
    # If prime draw circle
    if is_prime(step):
        fill(255)
        stroke(255)
        circle(x, y, step_size * 0.5)
        if px is not None:
            line(x, y, px, py)
        px = x
        py = y

    # Move according to state
    if state == 0:
            x += step_size
    elif state == 1:
            y -= step_size
    elif state ==  2:
            x -= step_size
    elif state ==  3:
            y += step_size    
    # Change state
    if step % num_steps == 0:
        state = (state + 1) % 4
        turn_counter += 1
        if turn_counter % 2 == 0:
            num_steps += 1
    step += 1
    # Are we done?
    if x > width:
        no_loop()
    

