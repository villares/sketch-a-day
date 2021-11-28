from __future__ import unicode_literals

active_category_name = '',

def setup():
    size(900, 450)
    global  categories, flags
    textSize(16)
    flags = [
        {"name": "Celestial",   "x": 20, "y": 40, "state": False},
        {"name": "Emporium", "x": 20, "y": 60, "state": False},
        {"name": "Benevolent",  "x": 20, "y": 80, "state": False},
        {"name": "Knowledge",  "x": 20, "y": 100, "state": False},
        ]
    # categories = [   # manual for tests
    #      {"name": A",   "x": 20, "y": 150, "state": False},
    #      {"name": "B", "x": 20, "y": 170, "state": True},
    #      {"name": "C",  "x": 20, "y": 190, "state": False},    
    # ]
    category_names = loadStrings('categories.txt') # from data/categories.txt
    categories = []
    for name in category_names:
        y = 140 if not categories else categories[-1]["y"] + 20
        novo_item = { "name" : name,
            "x": 20,
            "y":  y,
            "state": False}
        categories.append(novo_item)

def draw():
    background(200)
    draw_items(categories)
    draw_items(flags)

def mouse_over(x, y, e):
    return (x + e['x'] < mouseX < x + e['x'] + textWidth(e['name']) and
            y + e['y'] < mouseY < y + e['y'] + 20)

def draw_items(menu_items, x_offset=0, y_offset=0):
    push()
    textAlign(LEFT, CENTER)
    for item in menu_items:
        on = item['state']
        if item['name'].startswith('-'):  # separadores de cat
            fill(255) # em branco e sem o '-'
            text(item['name'][1:], x_offset + item['x'], y_offset + item['y'])
        else:
            if mouse_over(x_offset, y_offset, item):
                fill(100, 100, 255 * on)  # White for mouse over
            else:
                fill(0, 200 * on, 0)    # otherwise black
            text(item['name'], x_offset + item['x'], y_offset + item['y'])
    pop()
           
def mousePressed():
    # categories, like radio buttons    
    cat_selection = check_selection(categories)
    treat_category_selection(cat_selection)
    # flags, like checkboxes    
    flag_selection = check_selection(flags)
    treat_flag_selection(flag_selection)
    print(active_category_name, selected_flags)

    
def check_selection(menu_items, x_offset=0, y_offset=0):
    for item in menu_items:
        if mouse_over(x_offset, y_offset, item):
            return item
    else:
        return None
    
def treat_category_selection(selection):
    global active_category_name
    if selection:
        if selection['name'].startswith('-'):
            return # click on category separator
        elif selection['state'] == True:
            selection['state'] = False
            active_category_name = ''
        else:
            for cat in categories:
                cat['state'] = False
            selection['state'] = True
            active_category_name = selection['name']
            
def treat_flag_selection(selection):
    global selected_flags
    if selection:
        selection['state'] = not selection['state'] 
    selected_flags = [flag['name'] for flag in flags
                      if flag['state']]   # state == True
