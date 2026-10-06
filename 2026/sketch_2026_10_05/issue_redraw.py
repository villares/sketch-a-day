import py5

def setup():
    py5.size(200, 200)
    
def draw():
    #py5.no_loop()
    print('...')

def key_pressed():
    py5.redraw()
    
py5.run_sketch()