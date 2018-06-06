# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s155", ".gif"  # 180603

add_library('gifAnimation')
from gif_export_wrapper import *

perlinScale = 0.1
mx, my, mz = 0, 0, 0

def setup():
    size(500, 500)  # define o tamanho da tela em pixels. Largura X Altura
    noStroke()
    colorMode(HSB)

def draw():
    global mx, my, mz
    background(100)
    cols = 20
    tam = width / cols
    n_max, n_min = 0.5, 0.5
    for x in range(cols):
        for y in range(cols):
            for z in range(0, 100, 10):
                n = noise((mx + x) * perlinScale,
                          (my + y) * perlinScale,
                          mz * perlinScale)
                if n > n_max:
                    n_max = n
                if n < n_min:
                    n_min = n

    for x in range(cols):
        for y in range(cols):
            for z in range(0, 100, 10):
                n = noise((mx + x) * perlinScale,
                          (my + y) * perlinScale,
                          (mz + z) * perlinScale)
                nn = map(n, n_min, n_max, 0, 255)
                nd =  map(n, n_min, n_max, 0, tam)
                fill(nn, 200)
                noStroke()
                ellipse(tam / 2 + x * tam, tam / 2 + y * tam,
                        nd, nd)
    mx += 0.5
    my += 0.5
    mz += 0.5

    gif_export(GifMaker, frames=60, filename=SKETCH_NAME)
    # if frameCount <= 50:
    #     saveFrame(OUTPUT)
    # Gif exporter lib did not work well for the colours! :(
