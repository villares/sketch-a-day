# ASCII video

"""
 Aperte 'g' para gravar um PDF na pasta do sketch
 Press 'g' to record a PDF
 a, d, w, s to change sizes
"""
add_library('video')
add_library('pdf')
recordingPDF = False
grid_size = 16  # tamanho da grade
font_size = 16  # tamanho dsa letras
gliphs = (
    " .`-_':,;^=+/\"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLu" +
    "nT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q"
    )[::-1]
print(gliphs)    

def setup():
    global fonte
    global colunas, filas, video
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
    background(0)


def draw():
    global recordingPDF, filas, colunas
    colunas = int(width / grid_size)
    filas = int(height / grid_size)
    if video.available():
        background(255) 
        # se foi apertado 'g'
        if recordingPDF:
            # fill(0)
            # rect(0, 0, width, height)
            beginRecord(PDF, "Imagem.pdf")
        video.read()
        video.loadPixels()
        # Loopando as colunas da grade
        for i in range(colunas):
            # Loop das filas
            for j in range(filas):
                x = i * grid_size
                y = j * grid_size
                pos = y * video.width + x # índice da posição do pixel
                #cor = video.get(x, y)
                cor = video.pixels[pos]
                bri = brightness(cor)
                dar = int(map(bri, 0, 255, 0, len(gliphs)-1))
                fill(cor) # gliph color
                textSize(font_size)
                text(gliphs[dar], x + grid_size / 2, y + grid_size / 2)
             # dim fo loop das filas
         # fim do loop das colunas
        if (recordingPDF):
            endRecord()
            println('saved ascii_image.pdf')
            recordingPDF = False


def keyPressed(self):
    global recordingPDF, font_size, grid_size
    if key == 'g':
        recordingPDF = True
    if key == 'w':
        font_size += 1
    if key == 's' and font_size > 1:
        font_size -= 1
    if key == 'a':
        grid_size += 1
    if key == 'd' and grid_size > 1:
        grid_size -= 1
 
