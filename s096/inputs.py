# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from javax.swing import JOptionPane

"""
This will hpefully switch between Arduino (Firmata) variable input and
nice sliders based on Peter Farell's Sliders htts://twitter.com/hackingmath
https://github.com/hackingmath/python-sliders http://farrellpolymath.com/
"""
class Input:

    def __init__(self, Arduino):
        self.select_source(Arduino)
        if self.source > 0:
            self.arduino = Arduino(this, Arduino.list()[self.source], 57600)
        else:
            # start, end, default
            A = Slider(0, 1023, 128)
            B = Slider(0, 1023, 128)
            C = Slider(0, 1023, 128)
            D = Slider(0, 1023, 128)
            A.position(40, height - 70)
            B.position(40, height - 30)
            C.position(width - 140, height - 70)
            D.position(width - 140, height - 30)
            self.sliders = {1: A, 2: B, 3: C, 4: D}

    def analog(self, pin):
        if self.source:
            return self.arduino.analogRead(pin)
        else:
            return self.sliders[pin].val

    def update(self):
        if not self.source:
            for pin, slider in self.sliders.iteritems():
                slider.update()

    def keyPressed(self):
        if key == 'a':
            self.sliders[1].down = True
        if key == 'd':
            self.sliders[1].up = True
        if key == 's':
            self.sliders[2].down = True
        if key == 'w':
            self.sliders[2].up = True
        if keyCode == LEFT:
            self.sliders[3].down = True
        if keyCode == RIGHT:
            self.sliders[3].up = True
        if keyCode == DOWN:
            self.sliders[4].down = True
        if keyCode == UP:
            self.sliders[4].up = True

    def keyReleased(self):
        if key == 'a':
            self.sliders[1].down = False
        if key == 'd':
            self.sliders[1].up = False
        if key == 's':
            self.sliders[2].down = False
        if key == 'w':
            self.sliders[2].up = False
        if keyCode == LEFT:
            self.sliders[3].down = False
        if keyCode == RIGHT:
            self.sliders[3].up = False
        if keyCode == DOWN:
            self.sliders[4].down = False
        if keyCode == UP:
            self.sliders[4].up = False

    def digital(self, pin):
        space_pressed = keyPressed and key == ' '
        if self.source:
            if pin == 13:
                return self.arduino.digitalRead(13) or space_pressed
            else:
                return arduino.digitalRead(pin)
        else:
            return space_pressed

    def select_source(self, Arduino):
        # Input.Arduino = Arduino  # to make available on this module
        port_list = [str(num) + ": " + port for num, port
                     in enumerate(Arduino.list())]
        if not port_list:
            port_list.append(None)
        self.source = option_pane("O seu Arduino está conectado?",
                                  "Escolha a porta ou pressione Cancel\npara usar 'sliders':",
                                  port_list,
                                  -1)  # index for default option
        self.help()

    def help(self):
        if self.source:
            message = """   Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem
            'g' para salvar um GIF
            Tombe a lousa para lousa para limpar o desenho!"""
        else:
            message = """    Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem
            'g' para salvar um GIF
            'a' (-) ou 'd' (+) para o slider 1
            's' (-) ou 'w' (+) para o slider 2
             ←(-) ou  → (+) para o slider 3
             ↓  (-) ou  ↑  (+) para o slider 4
            [barra de espaço] para limpar o desenho"""
        ok = JOptionPane.showMessageDialog(None, message)


def option_pane(title, message, options, default=None, index_only=True):

    if default == None:
        default = options[0]
    elif index_only:
        default = options[default]

    selection = JOptionPane.showInputDialog(
        frame,
        message,
        title,
        JOptionPane.INFORMATION_MESSAGE,
        None,  # for Java null
        options,
        default)  # must be in options, otherwise 1st is shown
    if selection:
        if index_only:
            return options.index(selection)
        else:
            return selection

class Slider:

    SLIDERS = []

    def __init__(self, low, high, default):
        '''slider has range from low to high
        and is set to default'''
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False
        self.up, self.down = False, False
        Slider.SLIDERS.append(self)

    def position(self, x, y):
        '''slider's position on screen'''
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.rectx = self.x + map(self.val, self.low, self.high, 0, 120)
        self.recty = self.y - 10

    def update(self):
        '''updates the slider'''
        pushStyle()
        rectMode(CENTER)
        # black translucid rect behind slider
        fill(0, 100)
        noStroke()
        rect(self.x + 60, self.y, 130, 20)
        # gray line behind slider
        strokeWeight(4)
        stroke(200)
        line(self.x, self.y, self.x + 120, self.y)
        # press mouse to move slider
        if (self.x < mouseX < self.x + 120 and
                self.y < mouseY < self.y + 20):
            fill(250)
            textSize(10)
            text(str(int(self.val)), self.rectx, self.recty + 35)
            if mousePressed:
                self.rectx = mouseX
        # key usage
        if self.up:
            self.rectx += 1
        if self.down:
            self.rectx -= 1
        # constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + 120)
        # draw rectangle
        strokeWeight(1)
        fill(255)
        rect(self.rectx, self.recty + 10, 10, 20)
        self.val = map(self.rectx, self.x, self.x + 120, self.low, self.high)
        popStyle()
