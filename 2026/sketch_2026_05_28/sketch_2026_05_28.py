# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
from telemetrix_helper import init_board

mode_a, mode_b = 0, 0
data = {}

def setup():
    global board, enc_a, enc_b
    py5.size(800, 800)
    if board := init_board():
        enc_a = board.init_encoder(pin_a=12, pin_b=11, pin_sw=10)
        enc_b = board.init_encoder(pin_a=7, pin_b=6, pin_sw=5)
        board.set_pin_mode_digital_output(13)
    else:
        print('Unable to connect to the Arduino')
        py5.no_loop()
    py5.background(0)
    py5.no_stroke()

def draw():
    if mode_a == 0:
        data['x'] = enc_a.position * 4
    if mode_b == 0:
        data['y'] = enc_b.position * 4
    
    py5.fill(255)
    py5.circle(data['x'], data['y'], 10) 
    
    if enc_a.consume_press():
        board.digital_write(13, False)
    if enc_b.consume_press():
        board.digital_write(13, True)
    
    
def exiting():
    board.shutdown()
    print('Shutting down telemetrix connection.')

py5.run_sketch(block=False)