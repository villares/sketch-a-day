def setup():
    size(400, 400)
    
    
def mouse_dragged():
    if mouse_button == LEFT:
        print('left')
    elif mouse_button == RIGHT:
        print('right')
    elif mouse_button == CENTER:
        print('middle')
    else:
        print(mouse_button)
