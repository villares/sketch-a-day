from __future__ import division

# add_library('gifAnimation')
# from villares.gif_export import gif_export

def setup():
    global cols, rows, pixs
    size(600, 400);
    img = loadImage('img.jpg')
    cols, rows = 300, 200
    sx = img.width / float(cols)
    sy = img.height / float(rows)
    pixs = {}
    for i in range(cols):
        x = int(sx / 2 + i * sx)
        for j in range(rows):
            y = int(sy / 2 + j * sy)
            c = img.get(x, y)
            pixs[(i, j)] = c
            
def draw():
    clear()
    s = 2 
    # t = map(mouseX, 0, width, 0, 1) # for testing with the mouse
    t = (1 + cos(frameCount / 10.0)) / 2.1  # used for the animation
    for i in range(rows):
        # make a list for a row (fila) recording color and row position
        fila = [(pixs.get((j, i), 0), j) # (color, original j-position)
                for j in range(cols)]  
        
        # sort fila (row in Portuguese) by color (brightness, hue or saturation)
        # sorted_fila = reversed(sorted(fila, key=lambda t:brightness(t[0])))
        # sorted_fila = (sorted(fila, key=lambda t:hue(t[0])))
        sorted_fila = (sorted(fila, key=lambda t:saturation(t[0])))

        new_fila = [(c, lerp(j, oj, t))  # color, lerped j-position (mixing original-j and sorted-j)
                    for j, (c, oj) in enumerate(sorted_fila)] 
         
        sorted_new_fila = sorted(new_fila, key=lambda t:t[1])  # now sorted by the lerped-j
        for j, (c, nj) in enumerate(sorted_new_fila):    
            noStroke()
            fill(c)
            rect(j * s, i * s, s, s)
                
    # if frameCount / 10.0 <= TWO_PI:
    #     gif_export(GifMaker, "melts", delay=200) # try less!
    # else:
    #     gif_export(GifMaker, finish=True)
