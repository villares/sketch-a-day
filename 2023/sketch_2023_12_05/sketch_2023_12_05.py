img = None
s = {'x':100, 'y':100, 'w':100, 'h':50}

def setup():
    global img
    size(1200, 600)
    img = load_image('a.jpg')


def draw():
    background(200)
    if img:
        f = img.width / img.height 
        image(img, 0, 0, height, height / f)
    x, y, w, h = s['x'], s['y'], s['w'], s['h']
    no_fill()
    stroke(255)
    rect(x, y, w, h)

def key_pressed():
    save_frame('out.png')
    if key == 'o':
        select_input('imagem', get_image)
    
        
def get_image(selection):
    global img
    if selection:
        img = load_image(selection)
        
        

