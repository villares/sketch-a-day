"""
This will hopefully switch between Arduino (Firmata) variable input and
nice sliders based on Peter Farell's Sliders htts://twitter.com/hackingmath
https://github.com/hackingmath/python-sliders http://farrellpolymath.com/

2020-03-14 Fix for Arduino no the first serial port (index 0)!
2022-08-03 Converting for use with py5 and pyFirmata
2022-08-05 Trying to make it compatible with all py5 "modes"
"""

import py5

class InputInterface:

    def __init__(self, port=None):
        self.source = get_arduino(port)
        if self.source is None:
            sketch = py5.get_current_sketch()
            w, h = sketch.width, sketch.height
            # start, end, default
            A = Slider(0, 1023, 512)
            B = Slider(0, 1023, 512)
            C = Slider(0, 1023, 512)
            D = Slider(0, 1023, 512)
            A.position(40, h - 70)
            B.position(40, h - 30)
            C.position(w - 140, h - 70)
            D.position(w - 140, h - 30)
            self.sliders = {1: A, 2: B, 3: C, 4: D}

    def analog_read(self, pin):
        if self.source is not None:
            return self.source.analog_read(pin)
        else:
            return self.sliders[pin].val

    def update(self):
        if self.source is None:
            for pin, slider in self.sliders.items():
                slider.update()

    def key_pressed(self):
        sketch = py5.get_current_sketch()
        k, kc = sketch.key, sketch.key_code
        if k == 'a':
            self.sliders[1].down = True
        if k == 'd':
            self.sliders[1].up = True
        if k == 's':
            self.sliders[2].down = True
        if k == 'w':
            self.sliders[2].up = True
        if kc == py5.LEFT:
            self.sliders[3].down = True
        if kc == py5.RIGHT:
            self.sliders[3].up = True
        if kc == py5.DOWN:
            self.sliders[4].down = True
        if kc == py5.UP:
            self.sliders[4].up = True

    def key_released(self):
        sketch = py5.get_current_sketch()
        k, kc = sketch.key, sketch.key_code
        if k == 'a':
            self.sliders[1].down = False
        if k == 'd':
            self.sliders[1].up = False
        if k == 's':
            self.sliders[2].down = False
        if k == 'w':
            self.sliders[2].up = False
        if kc == py5.LEFT:
            self.sliders[3].down = False
        if kc == py5.RIGHT:
            self.sliders[3].up = False
        if kc == py5.DOWN:
            self.sliders[4].down = False
        if kc == py5.UP:
            self.sliders[4].up = False

    def digital_read(self, pin):
        sketch = py5.get_current_sketch()
        k, ikp = sketch.key, sketch.is_key_pressed
        space_pressed = ikp and k == ' '
        if self.source is not None:
            if pin == 13:
                return self.source.digital_read(13) or space_pressed
            else:
                return self.source.digital_read(pin)
        else:
            return space_pressed

    def help(self):
        from javax.swing import JOptionPane
        if self.source is not None:
            message = """   Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem"""
        else:
            message = """    Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem
            'a' (-) ou 'd' (+) para o slider 1
            's' (-) ou 'w' (+) para o slider 2
             ←(-) ou  → (+) para o slider 3
             ↓  (-) ou  ↑  (+) para o slider 4"""
        ok = JOptionPane.showMessageDialog(None, message)


class Slider:

    SLIDERS = []

    def __init__(self, low, high, default):
        """slider has range from low to high
        and is set to default"""
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False
        self.up, self.down = False, False
        Slider.SLIDERS.append(self)

    def position(self, x, y):
        """slider's position on screen"""
        self.x = x
        self.y = y
        # the position of the rect you slide
        self.rectx = self.x + py5.remap(self.val, self.low, self.high, 0, 120)
        self.recty = self.y - 10

    def update(self):
        """updates the slider"""
        sketch = py5.get_current_sketch()
        mx, my, imp = sketch.mouse_x, sketch.mouse_y, sketch.is_mouse_pressed
        # To draw the slider without any style or coord tansformation
        py5.push()         
        py5.reset_matrix() 
        #py5.camera() # uncomment this if on P3D
        py5.rect_mode(py5.CENTER)
        # black translucid rect behind slider
        py5.fill(0, 100)
        py5.no_stroke()
        py5.rect(self.x + 60, self.y, 130, 20)
        # gray line behind slider
        py5.stroke_weight(4)
        py5.stroke(200)
        py5.line(self.x, self.y, self.x + 120, self.y)
        # press mouse to move slider
        if (self.x < mx < self.x + 120 and self.y < my < self.y + 20):
            py5.fill(250)
            py5.text_size(10)
            py5.text(str(int(self.val)), self.rectx, self.recty + 35)
            if imp:
                self.rectx = mx
        # key usage
        if self.up:
            self.rectx += 1
        if self.down:
            self.rectx -= 1
        # constrain rectangle
        self.rectx = py5.constrain(self.rectx, self.x, self.x + 120)
        # draw rectangle
        py5.no_stroke()
        py5.fill(255)
        py5.rect(self.rectx, self.recty + 10, 10, 20)
        self.val = py5.remap(
            self.rectx,
            self.x,
            self.x + 120,
            self.low,
            self.high
        )
        py5.pop()


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
