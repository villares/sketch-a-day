
def setup():
    size(360, 300)
    strokeWeight(2)
    
def draw():
    background(200)
    for x in range(width):
        y = height - brutal_sigmoid(radians(x)) * 300
        point(x, y)
    x = frameCount % 360
    y = height - brutal_sigmoid(radians(x)) * 300
    circle(x, y, 10)

def brutal_sigmoid(angle):        
    m = cos(angle) * 10
    r = 1 / (1 + exp(-m))  
    if r < 0.001:
        return 0
    elif r > 0.999:
        return 1
    else:  
        return r
    
    
