# import copy as cp

add_library('pdf')
polys = []
current_poly = []
divisoes = 5
salvar_pdf = False
ponto_clique = []

def setup():
    size(700, 700)
    strokeJoin(ROUND)

def draw():
    if salvar_pdf:
        beginRecord(PDF, "####.pdf")

    mh, mv = width / 2, height / 2
    translate(mh, mv)
    background(240, 240, 200) 
    
    angulo = radians(360. / divisoes)
    fill(0, 0, 200)
    noStroke()
    for num in range(divisoes):
        rotate(angulo)
        for poly in polys:
            # (x1, y1), (x2, y2) = poly
            print poly
            draw_poly(poly)
            scale(-1, 1)
            draw_poly(poly)
            scale(-1, 1)

    if salvar_pdf:
        endRecord()
        global salvar_pdf
        salvar_pdf = False

    if current_poly:
        noFill()
        stroke(0)
        for num in range(divisoes):
            rotate(angulo)
            draw_poly(current_poly + [(mouseX, mouseY)])
            scale(-1, 1)
            draw_poly(current_poly + [(mouseX, mouseY)])
            scale(-1, 1)

def draw_poly(poly):
    pushMatrix()
    translate(-width / 2, -height / 2)
    beginShape()
    for p in poly:
        vertex(p[0], p[1])
    endShape(CLOSE)
    popMatrix()

def mousePressed():  # def mouseDragged():
    if mouseButton == LEFT:
        current_poly.append((mouseX, mouseY))    
    if mouseButton == RIGHT:
        polys.append(current_poly + [(mouseX, mouseY)])
        current_poly[:] = []

def keyPressed():
    global salvar_pdf, divisoes
    if key == "a":
        polys[:] = [[]]  # esvazia lista de polys
        ponto_clique[:] = []
    if key == "g":
        saveFrame("#####.png")
        print("salvando PNG")
    if key == "p":
        salvar_pdf = True
        print("salvando PDF")
    if key == BACKSPACE and polys:
        polys.pop()
    if key == "-" and divisoes > 2:
        divisoes -= 1
    if key == "+" or key == "=":
        divisoes += 1        
        
