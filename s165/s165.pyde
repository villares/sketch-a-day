# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s165", ".gif"  # 180613
"""
Exemplo de Perlin Noise em três dimensões 
"""

add_library('peasycam')
perlinScale = 0.1
z = 10

def setup():
    size(500, 500, P3D)  # define o tamanho da tela em pixels. Largura X Altura
    #noStroke()
    colorMode(HSB)
    cam = PeasyCam(this, 500)
    cam.setMaximumDistance(1000)
    cam.setMinimumDistance(1000)

def draw():
    background(0)
    translate(-width/2, -height/2, 0)
    cols = 30
    tam = width / cols
    for zz in range(cols):
       for x in range(cols):
        for y in range(cols):
            n = noise((mouseX + x) * perlinScale,
                      (mouseY + y) * perlinScale,
                      (zz + z) * perlinScale)
            fill(240 * n, 255, 255)
            with pushMatrix():
                translate(tam / 2 + x * tam, tam / 2 + y * tam, zz * tam)
                box( tam - tam * n)

def keyPressed():
    global z
    if keyCode == UP:
        z += 1
    if keyCode == DOWN:
        z -= 1
