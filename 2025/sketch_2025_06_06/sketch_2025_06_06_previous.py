
def setup():
    size(600, 600)
    scale(1.5)
    text_align(CENTER)
    text_font(create_font('Inconsolata Bold', 18))
    stroke_weight(10.0)
    translate(0, 50)
    stroke_join(MITER)
    corner(50, 20)
    label('MITER', 100, 130, extra='(default)')
    stroke_join(BEVEL)
    corner(250, 20)
    label('BEVEL', 300, 130)
    stroke_join(ROUND)
    corner(250, 190)
    label('ROUND', 300, 300)
    translate(50, 120)
    fill(255)
    stroke_cap(SQUARE)
    line(20, 67, 80, 67)
    text("stroke_cap(SQUARE)", 50, 90)
    stroke_cap(PROJECT)
    line(20, 107, 80, 107)
    text("stroke_cap(PROJECT)", 50, 130)
    stroke_cap(ROUND)
    line(20, 147, 80, 147)
    text("stroke_cap(ROUND)\n(default)", 50, 170)
    #save('/home/villares/GitHub/material-aulas/Processing-Python-py5/assets/mais_atributos.png')
    
def label(mode, x, y, extra=''):
    fill(255)
    text(f'stroke_join({mode})\n{extra}', x, y)
    
def corner(x, y):
    no_fill()
    triangle(x, y, x + 100, y, x + 50, y + 80)

    

