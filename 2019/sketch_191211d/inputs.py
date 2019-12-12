# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from javax.swing import JOptionPane

"""
This will switch between Arduino (Firmata) variable input and
nice sliders based on Peter Farell's Sliders htts://twitter.com/hackingmath
https://github.com/hackingmath/python-sliders http://farrellpolymath.com/
"""

class Slider:

    sliders = []
    firmata_port = None
    d_width = 120

    def __init__(self, low, high, default=None, kbd=None):
        self.kbd = kbd or ('a', 'd')
        '''slider has range from low to high
        and is set to default'''
        self.low = low
        self.high = high
        self.val = default if default is not None else (low + high) / 2
        self.clicked = False
        self.up, self.down = False, False
        self.sliders.append(self)
        self.label = None
        self.w, self.h = 120, 20

    def position(self, x, y):
        '''slider's position on screen'''
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.rectx = self.x + \
            map(self.val, self.low, self.high, 0, self.d_width)
        self.recty = self.y - 10

    def update(self, display=True):
        '''updates the slider'''
            # key usage
        if self.up:
            self.rectx += 1
        if self.down:
            self.rectx -= 1
            # draw
        if display:
            self.display()

    def display(self, show_value=True):
        pushMatrix()
        resetMatrix()
        pushStyle()
        rectMode(CENTER)
        stroke(200)
        strokeWeight(4)
        line(self.x, self.y, self.x + self.d_width, self.y)
        # press mouse to move slider
        if (self.x < mouseX < self.x + self.d_width and
                self.y - 10 < mouseY < self.y + 10):
            textSize(10)
            fill(0)
            text(str(int(self.val)), self.rectx, self.recty + 35)
            if mousePressed:
                self.rectx = mouseX
        # constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + self.d_width)
        # draw rectangle
        fill(250)
        stroke(0)
        strokeWeight(1)
        rect(self.rectx, self.recty + 10, 10, 20)
        self.val = map(self.rectx, self.x, self.x + 120, self.low, self.high)
        # draw label
        fill(0)
        textSize(10)
        # if show_value:
        #     text(int(self.val),self.rectx,self.recty + 35)
        if self.label is not None:
            # text label
            text(self.label, self.x + 135, self.y)
        popStyle()
        popMatrix()

    def value(self, display=True):
        self.update(display=display)
        return self.val

    def key_pressed(self):
        down, up = self.kbd
        k = keyCode if isinstance(down, int) else key
        if k == down:
            self.down = True
        if k == up:
            self.up = True

    def key_released(self):
        down, up = self.kbd
        k = keyCode if isinstance(down, int) else key
        if k == down:
            self.down = False
        if k == up:
            self.up = False

    @classmethod
    def keyPressed(cls):
        for slider in cls.sliders:
            slider.key_pressed()

    @classmethod
    def keyReleased(cls):
        for slider in cls.sliders:
            slider.key_released()

    @classmethod
    def update_all(cls, display=True):
        for i, slider in enumerate(cls.sliders):
            slider.update(display)
            if cls.firmata_port is not None:
                a = slider.analog(cls.analog_pins[i])
                slider.rectx = map(a, 0, 1023, slider.x, slider.x + 120)

    @classmethod
    def get_val(cls, n):
        return cls.sliders[n].val

    @classmethod
    def create_defaults(cls, Arduino=None, num=4):
        if Arduino:
            cls.setup_firmata(Arduino)
        # start, end, default
        A = Slider(0, 1023, 128, ("a", "d"))
        B = Slider(0, 1023, 128, ("s", "w"))
        C = Slider(0, 1023, 128, (LEFT, RIGHT))
        D = Slider(0, 1023, 128, (DOWN, UP))
        A.position(40, height - 70)
        B.position(40, height - 30)
        C.position(width - 140, height - 70)
        D.position(width - 140, height - 30)
        return A, B, C, D

    @classmethod
    def help(cls):
        message = """    Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem
            'a' (-) ou 'd' (+) para o slider 1
            's' (-) ou 'w' (+) para o slider 2
             ←(-) ou  → (+) para o slider 3
             ↓  (-) ou  ↑  (+) para o slider 4
            [barra de espaço] para limpar o desenho"""
        ok = JOptionPane.showMessageDialog(None, message)

    def analog(cls, pin):
        if cls.firmata_port is not None:
            return cls.arduino.analogRead(pin)

    def digital(cls, pin=13):
        space_pressed = keyPressed and key == ' '
        if cls.firmata_port is not None:
            if pin == 13:
                return cls.arduino.digitalRead(13) or space_pressed
            else:
                return arduino.digitalRead(pin)
        else:
            return space_pressed

    @classmethod
    def setup_firmata(cls, Arduino, analog_pins=(1, 2, 3, 4)):
        cls.firmata_port = cls.select_port(Arduino)
        println("Firmata port selected: {}".format(cls.firmata_port))
        if cls.firmata_port is not None:
            cls.analog_pins = analog_pins
            cls.arduino = Arduino(
                this, Arduino.list()[cls.firmata_port], 57600)

    @classmethod
    def select_port(cls, Arduino):
        port_list = [str(num) + ": " + port for num, port
                     in enumerate(Arduino.list())]
        if not port_list:
            port_list.append(None)
        return option_pane("O seu Arduino está conectado?",
                           "Escolha a porta ou pressione Cancel\npara usar 'sliders':",
                           port_list,
                           0)  # index for default option


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
