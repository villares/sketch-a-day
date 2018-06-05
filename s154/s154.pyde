# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s154", "###.png"  # 180603

perlinScale = 0.1
mx, my, z = 0, 0, 0

def setup():
    size(500, 500)  # define o tamanho da tela em pixels. Largura X Altura
    noStroke()
    colorMode(HSB)

def draw():
    global mx, my, z
    background(0)
    cols = 50
    tam = width / cols
    n_max, n_min = 0.5, 0.5
    for x in range(cols):
        for y in range(cols):
            n = noise((mx + x) * perlinScale,
                      (my + y) * perlinScale,
                      z * perlinScale)
            if n > n_max:
                n_max = n
            if n < n_min:
                n_min = n

    for x in range(cols):
        for y in range(cols):
            n = noise((mx + x) * perlinScale,
                      (my + y) * perlinScale,
                      z * perlinScale)
            nn = map(n, n_min, n_max, 0, 255)
            fill(nn, 255, 255)
            ellipse(tam / 2 + x * tam, tam / 2 + y * tam,
                    tam - 1, tam - 1)
    mx += 1
    my += 1
    z += 1           
    
    #if frameCount <= 50: saveFrame(OUTPUT)
    # Gif exporter lib did not work well for the colours! :(
