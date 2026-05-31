# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
from telemetrix_helper import init_board

mode_a, mode_b = 0, 0
mode_states = 2 # 0, 1

data = {
    'xa': 200,
    'ya': 400,
    'da': 200,
    'ca': 0,
    'xb': 600,
    'yb': 400,
    'db': 200,
    'cb': 4,
    }
mode_keys = {
    (0, 0): ('da', 'db'),
    (1, 0): ('xa', 'ya'),
    (0, 1): ('xb', 'yb'),
    (1, 1): ('ca', 'cb'),
}    

def setup():
    global board, enc_a, enc_b
    py5.size(800, 800)
    if board := init_board():
        enc_a = board.init_encoder(pin_a=12, pin_b=11, pin_sw=10)
        enc_b = board.init_encoder(pin_a=7, pin_b=6, pin_sw=5)
        board.set_pin_mode_digital_output(13)
        set_encoder_positions()
    else:
        print('Unable to connect to the Arduino')
        py5.exit_sketch()
    py5.background(0)
    py5.color_mode(py5.HSB)
    py5.no_fill()
    py5.stroke_weight(2)

def draw():
    global mode_a, mode_b
    ka, kb = mode_keys[mode_a, mode_b]
    data[ka] = enc_a.position * 4
    data[kb] = enc_b.position * 4
    py5.stroke(data['ca'] % 32 * 8, 255, 255)
    py5.circle(data['xa'], data['ya'], data['da'])
    py5.stroke(data['cb'] % 32 * 8, 255, 255)
    py5.circle(data['xb'], data['yb'], data['db']) 
    
    if enc_a.consume_press():
        mode_a = (mode_a + 1) % mode_states
        set_encoder_positions()
        #board.digital_write(13, False)        
    if enc_b.consume_press():
        mode_b = (mode_b + 1) % mode_states
        set_encoder_positions()
        
def set_encoder_positions():
    ka, kb = mode_keys[mode_a, mode_b]
    enc_a.position = data[ka] // 4         
    enc_b.position = data[kb] // 4 

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    
def exiting():
    if board:
        board.shutdown()
        print('Shutting down telemetrix connection.')

py5.run_sketch(block=False)