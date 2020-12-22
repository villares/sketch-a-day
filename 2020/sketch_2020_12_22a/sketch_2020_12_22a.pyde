from buttons import Button

estado_inicial = True

BLUE, RED = color(0, 0, 200), color(255, 0, 0)
b_color = BLUE

def setup():
    global b0, b1, show_hide
    size(400, 400)
    show_hide = Button(100, 100, 100, 50,
                txt="show\noptions",
                func=Button.toggle)
    b0 = Button(100, 150, 100, 50,
                txt="blue\nbackground",
                func=bgnd_setter(BLUE))
    b0.active = True
    b1 = Button(100, 200, 100, 50,
                txt="red\nbackgound",
                func=bgnd_setter(RED))

def draw():
    background(b_color)
    show_hide.display(mousePressed)
    if show_hide.active:
        b0.display(mousePressed)
        b1.display(mousePressed)
    
def bgnd_setter(c):
    def setter(button):
        global b_color
        button.exclusive_on()
        b_color = c
    return setter

# def red_BLUE(button):
#     global b_color
#     button.toggle()
#     if button..active:
#         b_color = color(255, 0, 0)
#     else:
#         b_color = color(0)
