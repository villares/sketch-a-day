from villares import ubuntu_jogl_fix  # you probably won't need this
# from villares.gif_export import gif_export

# add_library('gifAnimation')
ox, oy = 0, 0
    
def setup():
    global grid
    size(640, 640, P3D) 
    rectMode(CENTER)
    fill(0)
    colorMode(HSB)
    noSmooth()
    grid = rec_grid(0, 0, 16, width * 2)
            
def draw():
    global f
    f = frameCount / 40.0 
    background(0)
    ortho()
    translate(width / 2, height / 2, 0)
    rotateX(QUARTER_PI * (1 + cos(f + PI))/ 2 )
    rotateZ(QUARTER_PI * (1 + cos(f + PI)) / 2)
    draw_grid(grid)
    
    # if frameCount % 2:
    #     gif_export(GifMaker, "a", finish=False, delay=170)
    # if f >= TWO_PI:
    #     # noSmooth()
    #     gif_export(GifMaker, "a", finish=False)
    #     gif_export(GifMaker, "a", finish=False)
    #     gif_export(GifMaker, "a", finish=False)
    #     exit()
    
def keyPressed():
    redraw()
  
def draw_grid(grid):
    for cell in grid:
        if len(cell) == 3:
            x, y, cw = cell
            stroke(8 + 2 * (cw + 2), 255, 255)
            sbox(x, y, cw * cos(f + PI), cw)
        else:
            draw_grid(cell)
    
def rec_grid(x, y, n, tw):
    otranslate(x, y)
    cw = float(tw) / n
    margin = (cw - tw) / 2.0
    cells = []
    for i in range(n):
        nx = cw * i + margin
        for j in range(n):
            ny = cw * j + margin
            if cw > 8 and random(10) < 5:
                cs = rec_grid(nx, ny, 2, cw)
                cells.append(cs)
            else:
                cells.append((ox + nx, oy + ny, cw - 2))
    otranslate(-x, -y)
    return cells
    
def otranslate(x, y):
    global ox, oy
    ox += x
    oy += y
        
def sbox(x, y, s, s2):
    pushMatrix()
    translate(x , y, -abs(s * s2) / 4  + (s * s2) /4)
    box(s, s, s2 * 2 - s)
    popMatrix()
