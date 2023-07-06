from inputs import InputInterface


def setup():
    global inputs
    size(500, 500)
    inputs = InputInterface()
    
def draw():
    
    circle(100, 100, inputs.analog_read(1))
    circle(400, 100, inputs.analog_read(2))
    circle(400, 400, inputs.analog_read(3))
    circle(100, 400, inputs.analog_read(4))


    inputs.update(display=False)
    
def key_pressed():
    inputs.key_pressed()
    
def key_released():
    inputs.key_released()
