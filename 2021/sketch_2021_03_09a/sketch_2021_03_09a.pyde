from __future__ import unicode_literals

context_menu_clicked = False

def setup():
    global context_menu, main_menu
    context_menu = (
        {"name": "create", "y": 0, "func": create},
        {"name": "rename", "y": 20, "func": rename},
        {"name": "delete", "y": 40, "func": delete},
    )
    main_menu = [
        {"name": "red", "y": 0, "func": (lambda: fill(200, 0, 0))},
        {"name": "green", "y": 20, "func": (lambda: fill(0, 200, 0))},
        {"name": "blue", "y": 40, "func": (lambda: fill(0, 0, 200))},
    ]
    size(300, 300)

def draw():
    background(200)
    circle(150, 150, 150)
    draw_interface()

def draw_interface():
    push()
    textAlign(LEFT, CENTER)
    if context_menu_clicked:
        x, y = context_menu_clicked
        draw_interface_elements(context_menu, x, y)
    draw_interface_elements(main_menu)
    pop()

def create():
    r, g, b = int(random(256)), int(random(256)), int(random(256))
    name = "#{0:02x}{1:02x}{2:02x}".format(r, g, b)
    func = lambda : fill(r, g, b)
    new_item = { "name" : name.upper(),
                  "y":  main_menu[-1]["y"] + 20,
                  "func": func}
    main_menu.append(new_item)

def rename():
    pass

def delete():
    pass
    
def mouse_over(x, y, e):
    return (x < mouseX < x + textWidth(e['name']) and
            y + e['y'] < mouseY < y + e['y'] + 20)

def draw_interface_elements(ies, x=20, y=20):
    for item in ies:
        if mouse_over(x, y, item):
            fill(255)
        else:
            fill(0)
        text(item['name'], x, y + item['y'])
        
def mouseClicked():
    global context_menu_clicked
    if mouseButton == RIGHT and not context_menu_clicked:
        context_menu_clicked = (mouseX, mouseY)
    elif context_menu_clicked:
        x, y = context_menu_clicked
        context_menu_clicked = False    
        check_click(context_menu, x, y)
    else:
        check_click(main_menu)
        
                    
def check_click(its, x=20, y=20):
        for item in its:
            if mouse_over(x, y, item):
                print(item['name'])
                item['func']()
                return True
        else:
            return False
            print(None)
