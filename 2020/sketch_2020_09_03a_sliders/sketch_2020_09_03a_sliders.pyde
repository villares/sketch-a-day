""" 
 based on:
 ControlP5::addListener() (v1.2)
 GoToLoop (2018-Jun-20)
 https://Discourse.Processing.org/t/
 how-to-active-controlevent-in-controlp5-python-mode/1113/8
"""

add_library('controlP5')

bg = 200
tx = 100

def setup():
    size(400, 300)

    global slider_a, slider_b
    slider_a = (ControlP5(this)
                .addSlider('fundo')
                .setSize(width / 2, 20)
                .setPosition(width / 4, height / 2)
                .setRange(0, 255)
                .setValue(bg)
                .addListener(sliderListener)
                )
    slider_b = (ControlP5(this)
                .addSlider('texto')
                .setSize(width / 2, 20)
                .setPosition(width / 4, 40 + height / 2)
                .setRange(0, 255)
                .setValue(tx)
                .addListener(sliderListener)
                )

def draw():
    background(bg)
    fill(tx)
    text("HELLO SLIDERS", 120, 120)

def sliderListener(evt):
    global bg, tx
    if evt.isFrom(slider_a):
        bg = int(evt.getValue())
    if evt.isFrom(slider_b):
        tx = int(evt.getValue())
