"""
 ASCII video
 a, d, w, s to change sizes
"""

add_library('video')

color_mode = False
recordingPDF = False
grid_size = 8  # tamanho da grade
font_size = 12  # tamanho dsa letras
gliphs = (
    " .`-_':,;^=+/\"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLu" +
    "nT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q"
    )[::-1]   
# esse [::-1]  é um "reverse" do string em Python, para o primiro glifo ser o mais escuro e o último o mais claro
print(gliphs)    

def setup():
    global fonte, n_cols, n_rows, video
    size(640, 480)
    noStroke()
    smooth()
    rectMode(CENTER)
    fonte = createFont("SourceCodePro-Bold",60)
    textFont(fonte)
    textAlign(CENTER, CENTER)
    video = Capture(this, width, height)
    # Começa a captura
    video.start()

def draw():
    global n_rows, n_cols
    n_cols = int(width / grid_size)
    n_rows = int(height / grid_size)
    if video.available():
        background(255) 
        video.read()
        video.loadPixels()
        for c in range(n_cols):
            x = c * grid_size
            for r in range(n_rows):
                y = r * grid_size
                i = y * video.width + x # índice da posição do pixel
                #colour = video.get(x, y)
                colour = video.pixels[i]
                bri = brightness(colour)
                g = int(map(bri, 0, 255, 0, len(gliphs)-1))
                if color_mode: fill(colour)
                else: fill(0)
                textSize(font_size)
                text(gliphs[g], x + grid_size / 2, y + grid_size / 2)


def keyPressed(self):
    global font_size, grid_size, color_mode
    if key == 'g':
        saveFrame("f####.png")
    if key == 'w':
        font_size += 1
    if key == 's' and font_size > 1:
        font_size -= 1
    if key == 'a':
        grid_size += 1
    if key == 'd' and grid_size > 1:
        grid_size -= 1
    if key == 'c':
        color_mode = not color_mode
