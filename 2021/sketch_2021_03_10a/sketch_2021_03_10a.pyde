from __future__ import unicode_literals

context_menu_clicked = None

def setup():
    global context_menu, main_menu
    context_menu = (
        {"name": "create", "x": 20, "y": 0, "func": create},
        {"name": "rename", "x": 20, "y": 20, "func": rename},
        {"name": "delete", "x": 20, "y": 40, "func": delete},
    )
    main_menu = [
        {"name": "red",   "x": 20, "y": 20, "func": (lambda: fill(200, 0, 0))},
        {"name": "green", "x": 20, "y": 40, "func": (lambda: fill(0, 200, 0))},
        {"name": "blue",  "x": 20, "y": 60, "func": (lambda: fill(0, 0, 200))},
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
        x, y, item = context_menu_clicked
        draw_interface_elements(context_menu, x, y)
    draw_interface_elements(main_menu)
    pop()

def create(item):
    r, g, b = int(random(256)), int(random(256)), int(random(256))
    name = "#{0:02x}{1:02x}{2:02x}".format(r, g, b)
    func = lambda : fill(r, g, b)
    new_item = { "name" : name.upper(),
                  "x": 20,
                  "y":  main_menu[-1]["y"] + 20,
                  "func": func}
    main_menu.append(new_item)

def rename(picked_item):
    if picked_item:
        new_name = input(question='Rename {} to?'.format(picked_item['name']),
                         suggestion=picked_item['name'])
        if new_name: 
            picked_item['name'] = new_name
    
def delete(picked_item):
    for menu_item in reversed(main_menu):
        if menu_item == picked_item:
            main_menu.remove(picked_item)
            repack_menu(main_menu)
            return
    
def repack_menu(menu_items):
    y = 20
    for item in menu_items:
        item['y'] = y
        y += 20


def mouse_over(x, y, e):
    return (x + e['x'] < mouseX < x + e['x'] + textWidth(e['name']) and
            y + e['y'] < mouseY < y + e['y'] + 20)

def draw_interface_elements(menu_items, x_offset=0, y_offset=0):
    for item in menu_items:
        if item_disabled(item):
            fill(128)  # Dark grey for diabled
        elif mouse_over(x_offset, y_offset, item):
            fill(255)  # White for mouse over
        elif context_menu_clicked and context_menu_clicked[-1] == item:
            fill(240)  # Light grey if picked with right button
        else:
            fill(0)    # otherwise black
        text(item['name'], x_offset + item['x'], y_offset + item['y'])
  
def item_disabled(item):
    if context_menu_clicked:
        picked_item = context_menu_clicked[-1]
        if item['name'] == 'create':
            return False  # Create is always available
        elif picked_item == None:
            return True   # Other items unavailable if nothing picked
        else:
            return False  # otherwise they are available
    else:
        return False # nothing is disabled if context_menu_clicked is False
            
def mouseClicked():
    global context_menu_clicked
    item = check_click(main_menu)
    if mouseButton == RIGHT and not context_menu_clicked:
        context_menu_clicked = (mouseX, mouseY, item)
    elif context_menu_clicked:
        x, y, item = context_menu_clicked
        context_menu_clicked = False    
        context_item = check_click(context_menu, x, y)
        if context_item:
            context_item['func'](item)
    elif item:
        item['func']()
            
def check_click(menu_items, x_offset=0, y_offset=0):
        for item in menu_items:
            if mouse_over(x_offset, y_offset, item):
                print(item['name'])
                return item
        else:
            return None
        
def input(question='', suggestion=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(None, question, suggestion)
