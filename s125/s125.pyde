# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s125"  # 180505

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import *
from inputs import *

def setup():
    global input, GIF_EXPORT
    size(600, 600)
    rectMode(CENTER)  # retângulos desenhados pelo centro
    textAlign(CENTER, CENTER)
    noFill()  # sem contorno
    frameRate(30)
    strokeWeight(3)
    Cell.ELEMENTS = []
    GIF_EXPORT = False
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino, slider_pins=[1, 2])
    create_grid()

def draw():
    background(127)  # fundo cinza claro

    for cell in Cell.ELEMENTS:
        cell.draw_()
    # uncomment next lines to export GIF
    global GIF_EXPORT
    if not frameCount % 20 and GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=1000,
                                delay=300,
                                filename=SKETCH_NAME)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    input.update()


def keyPressed():
    global GIF_EXPORT
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'g':  # save GIF
        GIF_EXPORT = True
    if key == 'h':
        input.help()
    input.keyPressed()
    create_grid()

def keyReleased():
    input.keyReleased()

def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]

def item_at_x_y(x, y, collenction, width_):
    return collection[x + y * width_]

def pointy_hexagon(x, y, r):
    with pushMatrix():
        translate(x, y)
        rotate(radians(30))  # pointy, comment out for "flat_hexagon()"
        beginShape()
        for i in range(6):
            sx = cos(i * TWO_PI / 6) * r
            sy = sin(i * TWO_PI / 6) * r
            vertex(sx, sy)
        endShape(CLOSE)

def calculate_neighbours():
    pass

def create_grid():
    global GRID_SIDE, RAND_SIZE, SPAC_SIZE
    # seize inputs
    GRID_SIDE = int(input.analog(1) / 16)  # 0 a 63 linhas e colunas na grade
    RAND_SIZE = int(input.analog(2) / 16)  # escala a randomização do tamanho
    randomSeed(int(input.analog(1)) / 4)
    # espaçamento entre os elementos
    SPAC_SIZE = int(width / (GRID_SIDE + 0.01))

    # empty list
    Cell.ELEMENTS[:] = []
    v = SPAC_SIZE * 1.5
    h = SPAC_SIZE * sqrt(3)
    for _ in range(1):
        for ix in range(GRID_SIDE):  # um x p/ cada coluna
            # um y p/ cada linha
            for iy in range(GRID_SIDE):
                if iy % 2:
                    x = ix * h + h / 4
                else:
                    x = ix * h - h / 4
                y = iy * v
                final_size = SPAC_SIZE + RAND_SIZE * random(-1, 1)
                C = map(final_size, 0, 63, 0, 255)
                Cell.ELEMENTS.append(Cell(C, x, y, final_size, int(random(2))))
                
class Cell():
    
    def __init__(self, col, x, y, siz, sta):
        self.color_ = col
        self.x = x
        self.y = y
        self.size_ = siz
        self.status = sta 
    
    def draw_(self):
        if dist(self.x, self.y, mouseX, mouseY) < SPAC_SIZE * 2:
            fill(0, 100)
        else:
            noFill()
        if self.status:
            stroke(self.color_)
            pointy_hexagon(self.x, self.y, self.size_)
            fill(255)
            text(str(self.neighbours()), self.x, self.y)

            
    def neighbours(self):
        count = 0
        for cell in Cell.ELEMENTS:
            if cell is not self and cell.status:
                if dist(self.x, self.y, cell.x, cell.y) < SPAC_SIZE * 2:
                   count += 1
        return count
