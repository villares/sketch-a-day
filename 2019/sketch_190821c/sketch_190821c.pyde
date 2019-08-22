add_library('pdf')
linhas = []
divisoes = 5
salvar_pdf = False
ponto_clique = []

def setup():
    size(500, 500)

def draw():
    if salvar_pdf:
        beginRecord(PDF, "####.pdf")

    stroke(255)  # traço branco
    strokeWeight(10)  # espessura do traço ("peso")
    mh, mv = width / 2, height / 2
    translate(mh, mv)
    background(0, 128, 32)  # verde (mude a sua cor!)

    for num in range(divisoes):
        rotate(radians(360 / divisoes))
        for linha in linhas:
            x1, y1, x2, y2 = linha
            line(x1 - mh, y1 - mv, x2 - mh, y2 - mv)
            scale(1, -1)
            line(x1 - mh, y1 - mv, x2 - mh, y2 - mv)
            scale(1, -1)

    if salvar_pdf:
        endRecord()
        global salvar_pdf
        salvar_pdf = False

    if ponto_clique:
        for num in range(divisoes):
            rotate(radians(360 / divisoes))
            line(ponto_clique[0] - mh, ponto_clique[1] - mv,
                 mouseX - mh, mouseY - mv)
            scale(1, -1)
            line(ponto_clique[0] - mh, ponto_clique[1] - mv,
                 mouseX - mh, mouseY - mv)
            scale(1, -1)

def mousePressed():  # def mouseDragged():
    if ponto_clique:
        px, py = ponto_clique
        linhas.append((px, py, mouseX, mouseY))
    if mouseButton == LEFT:
        ponto_clique[:] = mouseX, mouseY
    elif mouseButton == RIGHT:
        ponto_clique[:] = []

def keyPressed():
    if key == "a":
        linhas[:] = []  # esvazia lista de linhas
        ponto_clique[:] = []
    if key == "g":
        saveFrame("#####.png")
        print("salvando PNG")
    if key == "p":
        global salvar_pdf
        salvar_pdf = True
        print("salvando PDF")
    if keyCode == BACKSPACE and linhas:
        linhas[:] = linha[:-1]
        
