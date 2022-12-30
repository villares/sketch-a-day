
parameters = {
    'A': 5,
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
    translate(width / 2, height / 2)
    rotate(radians(parameters['B']))
    for n in range(-parameters['A']//2, parameters['A']//2):
        line(n * parameters['C'], parameters['D'],
             n * parameters['C'], -parameters['D'])     
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
    