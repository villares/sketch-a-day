from villares import ubuntu_jogl_fix

    
def setup():
    global grid
    size(640, 640, P3D) 
    rectMode(CENTER)
    fill(0)
    colorMode(HSB)
    smooth(8)
    # strokeWeight(2)
    grid = rec_grid(0, 0, 16, width * 2)
            
def draw():
    global f
    f = frameCount / 20.0
    background(0)
    ortho()
    translate(width / 2, height / 2, 0)
    # rotateX(QUARTER_PI + mouseX / 100.0)
    # rotateZ(QUARTER_PI + mouseX / 100.0)
    rotateX(QUARTER_PI)
    rotateZ(QUARTER_PI)
    draw_grid(grid)
    saveFrame("###.png")
    if f >= PI:
        exit()
    
def keyPressed():
    redraw()
  
def draw_grid(grid):
    for cell in grid:
        if len(cell) == 3:
            x, y, cw = cell
            stroke(8 + 2 * (cw + 2), 255, 255)
            sbox(x, y, cw * sin(f))
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
                # push()
                # translate(0, 0,  -cw/3)
                # sbox(nx, ny, cw-2)
                # pop()
                cells.append((screenX(nx, ny), screenY(nx, ny), cw-2))

    popMatrix()
    return cells
    
    
def sbox(x, y, s):
    pushMatrix()
    translate(x , y)
    box(s)
    popMatrix()
