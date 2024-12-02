# py5 imported mode sketch - learn more at https://py5coding.org

def setup():
    size(600, 600)
    background(255, 0, 0)
    
def draw():
    #background(255, 0, 0)
    d = random(20, 100)
    fill(random(255),
         random(255),
         random(255), 100) # R G B A
    if is_mouse_pressed:
        circle(mouse_x, mouse_y, d)
        
def key_pressed():
    if key == 's':
        save_frame('####.png')
