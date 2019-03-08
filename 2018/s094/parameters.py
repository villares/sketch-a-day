# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This will hpefully switch between Arduino (Firmata) variable input and
nice sliders based on Peter Farell's Sliders htts://twitter.com/hackingmath
https://github.com/hackingmath/python-sliders http://farrellpolymath.com/
"""
class Inputs:
    TILT = None
    
    @staticmethod
    def select_source(Arduino):
        Inputs.Arduino = Arduino  # to make available on this module
        port_list = [str(num) + ": " + port for num, port
                     in enumerate(Arduino.list())
                     if ("usb" in port.lower()
                         or "COM" in port)]
        if not port_list:
            port_list.append(None)
        user_input = option_pane("Is your Arduino connected?",
                                 "Choose the port or, Cancel\nto use sliders:",
                                 port_list,
                                 -1)  # index for default option
        return user_input

    @staticmethod
    def setup_inputs(port):

        if port == None:
            # start, end, default, + key, - key
            A = Slider(0, 1023, 128, 'q', 'a')
            B = Slider(0, 1023, 128, 'w', 's')
            C = Slider(0, 1023, 128, 'e', 'd')
            D = Slider(0, 1023, 128, 'r', 'f')

            A.position(40, height - 70)
            B.position(40, height - 30)
            C.position(width - 140, height - 70)
            D.position(width - 140, height - 30)

            @staticmethod
            def update():
                Slider.update_all()
                Inputs.TILT = (keyPressed and key == ' ')

        else:
            arduino = Inputs.Arduino(this, Inputs.Arduino.list()[port], 57600)

            A = Analog_input(arduino, 1)
            B = Analog_input(arduino, 2)
            C = Analog_input(arduino, 3)
            D = Analog_input(arduino, 4)
            
            @staticmethod
            def update():
                Analog_input.update_all()
                Inputs.TILT = arduino.digitalRead(13) == Inputs.Arduino.HIGH
                
        Inputs.update_inputs = update
        return A, B, C, D


def option_pane(title, message, options, default=None, index_only=True):
    from javax.swing import JOptionPane

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

    def __init__(self, low, high, default, more_key, less_key):
        '''slider has range from low to high
        and is set to default'''
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False
        self.more = more_key
        self.less = less_key
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
        if keyPressed:
            if key == self.more:
                self.rectx += 1
            if key == self.less:
                self.rectx -= 1
        # constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + 120)
        # draw rectangle
        strokeWeight(1)
        fill(255)
        rect(self.rectx, self.recty + 10, 10, 20)
        self.val = map(self.rectx, self.x, self.x + 120, self.low, self.high)
        popStyle()

    def value(self):
        ''' backwards compatible method... '''
        self.update()
        return self.val

    @classmethod
    def update_all(cls):
        for slider in Slider.SLIDERS:
            slider.update()

class Analog_input:

    INPUTS_LIST = []

    def __init__(self, board, pin):
        self.board = board
        self.pin = pin
        self.val = 100
        Analog_input.INPUTS_LIST.append(self)

    def update(self):
        arduino = self.board
        self.val = arduino.analogRead(self.pin)

    def value(self):
        self.update()
        return self.val

    @classmethod
    def update_all(cls):
        for reader in Analog_input.INPUTS_LIST:
            reader.update()
 
