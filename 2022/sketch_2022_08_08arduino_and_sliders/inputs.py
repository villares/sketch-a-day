
"""
This will hopefully switch between Arduino (Firmata) variable input and
nice sliders based on Peter Farell's Sliders htts://twitter.com/hackingmath
https://github.com/hackingmath/python-sliders http://farrellpolymath.com/

2020-03-14 Fix for Arduino no the first serial port (index 0)!
2022-08-03 Converting for use with py5 and pyFirmata
2022-08-05 Trying to make it compatible with all py5 "modes"
2022-08-06 Adding scroll wheel support to the sliders and other tweaks

"""

import py5
from locale import getdefaultlocale

interface_texts = {
    'en': {'arduino enabled help': """   Keys:
            'h' for help on keys
            'p' to save an image""",
           'sliders enabled help': """    Keys:
            'h' for help on keys
            'p' to save an image
            'a' (-) or 'd' (+) for slider 1
            's' (-) or 'w' (+) for slider 2
             ←  (-) or  →  (+) for slider 3
             ↓  (-) or  ↑  (+) for slider 4"""           
    },
    'pt': {'arduino enabled help': """   Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem""",
           'sliders enabled help': """    Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem
            'a' (-) ou 'd' (+) para o slider 1
            's' (-) ou 'w' (+) para o slider 2
             ←  (-) ou  →  (+) para o slider 3
             ↓  (-) ou  ↑  (+) para o slider 4"""
    },
}
try:
    loc = getdefaultlocale()[0][:2]
except (TypeError, ValueError):
    loc = 'en'
TR = interface_texts.get(loc, interface_texts['en'])

def tr(text):
    """Translate text."""
    return TR.get(text, text)

class InputInterface:

    def __init__(self, port=None):
        self.source = get_arduino(port)
        if self.source is None:
            sketch = py5.get_current_sketch()
            w, h = sketch.width, sketch.height
            # start, end, default
            A = Slider(0, 1023, 512, 'A', ('a', 'd'))
            B = Slider(0, 1023, 512, 'B', ('s', 'w'))
            C = Slider(0, 1023, 512, 'C', (py5.LEFT, py5.RIGHT))
            D = Slider(0, 1023, 512, 'D', (py5.DOWN, py5.UP))
            A.position(40, h - 70)
            B.position(40, h - 30)
            C.position(w - C.width - 40, h - 70)
            D.position(w - D.width - 40, h - 30)
            self.keys_pressed = set()
            self.sliders = {1: A, 2: B, 3: C, 4: D}
            for slider in self.sliders.values():
                slider.keys_pressed = self.keys_pressed

    def analog_read(self, pin):
        if self.source is not None:
            return self.source.analog_read(pin)
        else:
            return self.sliders[pin].val

    def update(self):
        if self.source is None:
            for slider in self.sliders.values():
                slider.update()

    def key_pressed(self):
        sketch = py5.get_current_sketch()        
        kp = sketch.key_code if sketch.key == py5.CODED else sketch.key
        self.keys_pressed.add(kp)

    def key_released(self):
        sketch = py5.get_current_sketch()
        kr = sketch.key_code if sketch.key == py5.CODED else sketch.key
        self.keys_pressed.discard(kr)

    def digital_read(self, pin):
        if pin == 13:
            space_pressed = ' ' in self.keys_pressed
            if self.source is not None:
                return self.source.digital_read(13) or space_pressed
            else:
                return space_pressed
        else:
            if 2 <= pin <= 9:
                nk = str(pin)
            else:
                nk = {10: '0', 11: '1', 12: '-'}[pin]
            num_key_pressed = nk in self.keys_pressed
            if self.source is not None:
                return self.source.digital_read(pin) or num_key_pressed
            else:
                return num_key_pressed
            
    def mouse_wheel(self, e):
        if self.source is None:
            for slider in self.sliders.values():
                if slider.mouse_over(e.get_x(), e.get_y()):
                    slider.rectx += e.get_count()

    def help(self):
        from tkinter import messagebox
        #from javax.swing import JOptionPane
        if self.source is not None:
            message = tr('arduino enabled help')
        else:
            message = tr('sliders enabled help')
        #ok = JOptionPane.showMessageDialog(None, message)
        messagebox.showinfo(title='Help', message=message)


class Slider:

    def __init__(self, low, high, default, label='', control_keys=None):
        """slider has range from low to high
        and is set to default"""
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False
        self.is3D = py5.get_graphics()._instance.is3D()
        self.control_keys = control_keys
        self.keys_pressed = {}
        self.label = label
        self.width, self.height = 120, 20
        self.template = "{:.0f}"  # para formatar como mostra o valor
        self.label_align = py5.LEFT
    
    def position(self, x, y):
        """slider's position on screen"""
        self.x = x
        self.y = y
        # the position of the rect you slide
        self.rectx = self.x + py5.remap(self.val,
                                        self.low, self.high,
                                        0, self.width)

    def update(self):
        """updates the slider"""
        sketch = py5.get_current_sketch()
        mx, my, imp = sketch.mouse_x, sketch.mouse_y, sketch.is_mouse_pressed
        # To draw the slider without any style or coord tansformation
        py5.push()         
        py5.reset_matrix()
        if self.is3D:
            py5.camera()
        py5.rect_mode(py5.CENTER)
        # black translucid rect behind slider
        py5.fill(255, 128)
        py5.no_stroke()
        py5.rect(self.x + self.width / 2, self.y, self.width, self.height)
        # gray line behind slider
        py5.stroke_weight(3)
        py5.stroke(128)
        py5.line(self.x + self.height / 2,
                 self.y,
                 self.x + self.width - self.height / 2,
                 self.y)
        #py5.circle(self.x, self.y, 4)
        # press mouse to move slider
        tx = self.x + self.width * 0.5
        ty = self.y + self.height * 0.75
        if py5.brightness(py5.get(int(tx), int(ty))) < 128:
            py5.fill(255)
        else:
            py5.fill(0)        
        if self.mouse_over(mx, my):
            if imp:
                self.rectx = mx
            py5.text_align(py5.CENTER, py5.CENTER)
            py5.text_size(self.height / 2)
            py5.text(self.template.format(self.val), tx, ty)
        # draw label
        if self.label_align == py5.LEFT:
            py5.text_align(py5.LEFT, py5.CENTER)
            py5.text(self.label, self.x  + self.width + self.height / 4, self.y)
        else:
            py5.text(self.label, self.x + self.width / 2, self.y - self.height)
        # control keys
        #print(self.control_keys, self.keys_pressed)
        if self.control_keys:
            down, up = self.control_keys[0], self.control_keys[1]
            if down in self.keys_pressed:
                self.rectx -= 1
            if up in self.keys_pressed:
                self.rectx += 1
        # constrain rectangle
        self.rectx = py5.constrain(self.rectx,
                                   self.x + self.height / 4,
                                   self.x + self.width - self.height / 4)
        # draw rectangle
        py5.fill(255)
        py5.stroke(0)
        py5.stroke_weight(1)
        if self.is3D:
            py5.translate(0, 0, 1)
        py5.rect(
            self.rectx,
            self.y,
            self.height / 2,
            self.height)
        self.val = py5.remap(
            self.rectx,
            self.x + self.height / 4,
            self.x + self.width - self.height / 4,
            self.low,
            self.high)
        py5.pop()
    
    def mouse_over(self, mx, my):
        HW, HH = self.width / 2, self.height / 2 
        return (self.x < mx < self.x + self.width and
                self.y - HH / 2 < my < self.y + HH)
    
def get_arduino(port=None):
    """
    This is a PyFirmata 'helper' that tries to connect to an Arduino
    compatible board.
    
    If no port is informed, using pyserial's serial.tools.list_ports.comports(),
    if one port is found, tries that one. If more than one port is found,
    shows for the user to choose one. Returns None if no port is found or if the
    user cancels the dialog.
    
    If it successfully connects, it will return a pyfirmata Arduino object,
    but before that, it starts a pyfirmata.util.Iterator, and adds to the object
    both analog_read() and digital_read() functions that mimic Processing's
    Firmata library interface:
    Readings are never None, and analog pins return a value between 0 and 1023.
    """   
    from pyfirmata import Arduino, util
    from serial.tools import list_ports
    
    comports = [comport.device for comport in list_ports.comports()]
    if not comports:
        print('No ports found.')
        return None
    elif isinstance(port, str) and port not in comports:
        print(f'Port "{port}" not found.')
        return None
    elif isinstance(port, int):
        if port >= len(comports):
            print(f'Port [{port}] not found.')
            return None
        else:
            port = comports[port]
    elif len(comports) == 1:
        port = comports[0]
    elif port is None:
        port = option_pane(
            'Where is your board?',
            'Please select the USB port where your '
            'Arduino compatible board is connected:',
            comports,
            -1)  # index for default option
        if port is None:
            print('No port selected.')
            return None
    try:
        print(f'Connecting to port {port}...')
        arduino = Arduino(port)
        util.Iterator(arduino).start()
    except Exception as e:
        print(repr(e))
        return None
    # Prepare analog_read() for A0 A1 A2 A3 A4 A5
    for a in range(6):  
        arduino.analog[a].enable_reporting()
    arduino.analog_read = (lambda a: round(arduino.analog[a].read() * 1023)
                           if arduino.analog[a].read() is not None
                           else 0)
    # Prepare digital_read() for D2 to D13
    digital_pin_dict = {d: arduino.get_pin(f'd:{d}:i')
                        for d in range(2, 14)}
    for d in digital_pin_dict.keys():
        digital_pin_dict[d].enable_reporting()
    arduino.digital_read = (lambda d: digital_pin_dict[d].read()
                            if digital_pin_dict[d].read() is not None
                            else False)
    return arduino


def option_pane(title, message, options, default=None, index_only=False):
    """
    A helper for Java swing JOptionPane input dialog with drop down options.
    
    title     : str   - Dialog window's title (make it shorter than message).
    message   : str   - Text shown before the drop down.
    options   : list  - List of strings to show in the drop down.
    default   : int   - None or index to the pre-selected option in the list.
    index_only: False - Function returns an option string from the options list
                        provided, or None, if the dialog was cancelled;
                True  - Function returns the position index to the options list.    
    """
    from javax.swing import JOptionPane
    
    if default is None:
        default = options[0]
    elif index_only:
        default = options[default]

    selection = JOptionPane.showInputDialog(
        None,     # frame
        message,
        title,
        JOptionPane.INFORMATION_MESSAGE,
        None,     # for Java null
        options,
        default)  # must be in options, otherwise first is shown
    if selection:
        if index_only:
            return options.index(selection)
        else:
            # Trouble: selection can be java.lang.String
            return str(selection) if selection else None