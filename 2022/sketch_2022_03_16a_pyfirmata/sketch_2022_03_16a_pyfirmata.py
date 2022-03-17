import py5
from pyfirmata import ArduinoNano, util

pins = []

def setup():
    global board
    py5.size(600, 400)
    py5.no_fill()
    py5.stroke(255)
    board = ArduinoNano('/dev/ttyUSB0')
    #board.digital[13].write(0)
    it = util.Iterator(board)
    it.start()
    for i in range(1, 5):
        board.analog[i].enable_reporting()
        pins.append(board.analog[i])
    #analog_0 = board.get_pin('a:0:i')

def draw():
    py5.background(100, 128, 200)
    for i, pin in enumerate(pins):     
        v = pin.read()
        if v:
            x = 50 + i * 50
            py5.circle(x, 200, v * 50)
    
py5.run_sketch()
