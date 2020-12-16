from villares import ubuntu_jogl_fix
from villares.gif_export import gif_export

add_library('gifAnimation')

    
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
    f = frameCount / 80.0
    background(0)
    ortho()
    translate(width / 2, height / 2, 0)
    rotateX(QUARTER_PI * sin(f))
    rotateZ(QUARTER_PI * sin(f))
    # rotateX(QUARTER_PI)
    # rotateZ(QUARTER_PI)
    draw_grid(grid)
    if frameCount % 2:
        gif_export(GifMaker, "a", finish=False, delay=340)
    if f >= PI:
        # noSmooth()
        gif_export(GifMaker, "a", finish=False)
        exit()
    
def keyPressed():
    redraw()
  
def draw_grid(grid):
    for cell in grid:
        if len(cell) == 3:
            x, y, cw = cell
            stroke(8 + 2 * (cw + 2), 255, 255)
            sbox(x, y, cw, cos(f))
        else:
            draw_grid(cell)
  
        
def rec_grid(x, y, n, tw):
    pushMatrix()
    translate(x, y)
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
                stroke(8 + 2 * cw, 255, 255)
                cells.append((screenX(nx, ny), screenY(nx, ny), cw-2))
    popMatrix()
    return cells
    
    
def sbox(x, y, s, s2):
    pushMatrix()
    translate(x , y, -abs(s * s2)  + s * s2)
    box(s, s, s2 * 256 - s)
    popMatrix()
