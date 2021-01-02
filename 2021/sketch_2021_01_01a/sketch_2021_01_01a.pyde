from __future__ import division

# add_library('gifAnimation')
# from villares.gif_export import gif_export

def setup():
    global grid
    size(1024, 512)
    rectMode(CENTER)
    colorMode(HSB)
    noFill()
    stroke(255)

def draw():
    global f
    f = frameCount / 80.0
    background(0)
    translate(width / 2, height / 2)
    grid(0, 0, width, height, 20, 10, 10) 
    # if f <= TWO_PI:
    #     if frameCount % 2:
    #         gif_export(GifMaker, "output")
    # else:
    #     gif_export(GifMaker)
    #     gif_export(GifMaker)
    #     gif_export(GifMaker)
    #     gif_export(GifMaker, finish=True)

def grid(x, y, tw, th, cols, rows, piles):
        cw = tw / cols
        ch = th / rows
        xoffset = (cw - tw) / 2.0
        yoffset = (ch - th) / 2.0
        cells = []
        for i in range(cols):
            nx = x + cw * i + xoffset
            for j in range(rows):
                ny = y + ch * j + yoffset
                for k in range(piles):
                    stroke((k * 16) % 256, 255, 255)
                    nz = k * 4 * cos(f + ny) * 4 * sin(f + nx)
                    square(nx, ny, nz)
                    



def keyPressed():
    from villares.helpers import sketch_name
    saveFrame(sketch_name() + ".png")
