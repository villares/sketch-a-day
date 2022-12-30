from itertools import product

parameters = {
    'A': 50,
    'B': 5,
    'C': 10,
    'D': 15,
    }
              
key_actions = {
    UP: ('A', +1), DOWN: ('A', -1),
    RIGHT: ('B', +1), LEFT: ('B', -1),
    'd': ('C', +1), 'a': ('C', -1),
    'w': ('D', +1), 's': ('D', -1),
}

keyboard = set()
     
def setup():
    size(800, 800)
    stroke(255)
    
def draw():
    background(0)
    for x, y in product(range(0, width, parameters['A'] * 5), repeat=2):
        with push_matrix():
            translate(x, y)
            stroke(x % 256, y % 256, 128) 
            rotate(radians(parameters['B']))
            lines([(n * parameters['C'], parameters['D'],
                    n * parameters['C'], -parameters['D'])
                   for n in range(-width // 10, width // 10)])
    #print(parameters)
    update_parameters()
    
def update_parameters():
    for k in keyboard:
        if t := key_actions.get(k):
           parameters[t[0]] += t[1]
    
def key_pressed():
    k = key_code if key == CODED else key
    keyboard.add(k)
    
def key_released():
    k = key_code if key == CODED else key
    keyboard.discard(k)
    