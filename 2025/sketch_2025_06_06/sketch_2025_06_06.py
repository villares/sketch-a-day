# Couldn't resist and updated this in  2025_06_08
# to see previous ugly 2025_06_06 version check folder

def setup():
    size(600, 600)
    scale(1.5)
    text_align(CENTER)
    text_font(create_font('Inconsolata Bold', 18))
    stroke_weight(10.0)
    translate(0, 50)
    join_demo(50, 20, 'MITER', extra='(default)')
    join_demo(250, 20, 'BEVEL')
    join_demo(250, 190,'ROUND')
    cap_demo(100, 190, 'ROUND', extra='(default)')
    cap_demo(100, 250, 'PROJECT')
    cap_demo(100, 310, 'SQUARE')
    
    save('/home/villares/GitHub/material-aulas/Processing-Python-py5/assets/mais_atributos.png')


def cap_demo(x, y, mode, extra=''):
    stroke_cap(eval(mode))
    stroke(0)
    fill(0, 0, 100)
    line(x - 50, y, x + 30, y)
    point(x + 50, y)
    text(f'{extra}\nstroke_cap({mode})', x, y - 40)
        
def join_demo(x, y, mode, extra=''):
    stroke_join(eval(mode))
    no_fill()
    triangle(x, y, x + 100, y, x + 50, y + 80)
    fill(0, 0, 100)
    text(f'{extra}\nstroke_join({mode})', x +  50, y - 40)

    
