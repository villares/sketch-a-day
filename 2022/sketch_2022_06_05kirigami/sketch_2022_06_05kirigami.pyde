# Para atividade com corte laser no Sesc Av. Paulista
# Usar com Processing IDE e modo Python
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/

add_library('pdf') # equivale a importar a lib de PDF no Processing
mode_3D = True     # modo 3D ou 2D (muda com tecla '3')
save_pdf = False   # Avisa que vai exportar, tecla 's'
s = 0.005          # 'escala' do Perlin noise

def setup():
    size(600, 600, P3D)   # tamanho da tela do Processing

def draw():
    global save_pdf
    background(10)
    # versão "manual edite as tuplas
    elementos = [         # [(x, largura, altura, profundidade), ... ]
     (50, 60, 200, 30),
     (110, 60, 50, 100),
     (220, 160, 80, 60),           
     (380, 60, 180, 40),           
    ]
    margem = elementos[0][0]  # margem é o x do primeiro elemento    
    # Versão "automática" com Perlin noise - use noiseSeed(nnn) para travar (escolha o número)
    # # noiseSeed(123)
    # elementos = [] 
    # margem =  x = 50
    # while x < 580 - margem:
    #     w = 60 * noise(2000 + x * s * 10)  # largura do elemento
    #     a = 300 * noise(1000 + x * s)      # altura do elemento
    #     b = 300 * noise(x * s)             # profundidade do elemento
    #     elementos.append((x, w, a, b))
    #     x += w
    if mode_3D and not save_pdf:
        fill(255)
        stroke(0)
        push()
        translate(width / 2, height / 4, -height)
        rotateX(QUARTER_PI)
        rotateZ(QUARTER_PI / 2)
        translate(-width / 4, height / 2, 0)  # -height / 2, 0)
        rect_base(0, 0, 600, 400, *[(x, 0, w, b) for x, w, a, b in elementos])
        for x, w, a, b in elementos:
            rect_h(x, 0, w, b, z=a)
        rotateX(HALF_PI)
        rect_base(0, 0, 600, 400, *[(x, 0, w, a) for x, w, a, b in elementos])
        for x, w, a, b in elementos:
            rect_h(x, 0, w, a, z=-b)
        pop()
    else:
        background(255)
        noFill()
        if save_pdf:
            beginRecord(PDF, 'output###.pdf')
        rect(0, 0, 600, 600)
        last_x = 0
        for x, w, a, b in elementos:
            if x != last_x:
                stroke(0, 0, 200)
                line(last_x, height / 2, x, height / 2)
            y = 300
            stroke(200, 0, 0)
            line(x, y - a, x, y + b)
            line(x + w, y - a, x + w, y + b)
            stroke(0, 0, 200)
            line(x, y - a, x + w, y - a)
            line(x, y - a + b, x + w, y - a + b)
            line(x, y + b, x + w, y + b)
            last_x = x + w
        stroke(0, 0, 200)
        line(last_x, height / 2, width, height / 2)
        if save_pdf:
            endRecord()
            save_pdf = False

def rect_h(x, y, w, h, z):
    with pushMatrix():
        translate(0, 0, z)
        rect(x, y, w, h)

def rect_base(x, y, w, h, *furos):
    if furos:
        beginShape()
        vertex(x, y)
        vertex(x + w, y)
        vertex(x + w, y + h)
        vertex(x, y + h)
        for furo in furos:
            rect_base(*furo)
        endShape(CLOSE)
    else:
        beginContour()
        vertex(x, y)
        vertex(x, y + h)
        vertex(x + w, y + h)
        vertex(x + w, y)
        endContour()

def keyPressed():
    global mode_3D, save_pdf
    if key == 's':
        save_pdf = True
        print('Salvando PDF')
    elif key == '3':
        mode_3D = not mode_3D
