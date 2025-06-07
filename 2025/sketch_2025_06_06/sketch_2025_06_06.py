
def setup():
    size(600, 300)
    text_align(CENTER)
    text_font(create_font('Inconsolata Bold', 18))
    stroke_weight(10.0)    
    stroke_join(MITER)
    corner(50, 20)
    label('MITER', 100, 130, extra='(default)')
    stroke_join(BEVEL)
    corner(250, 20)
    label('BEVEL', 300, 130)
    stroke_join(ROUND)
    corner(450, 20)
    label('ROUND', 500, 130)
    translate(50, 160)
    text_align(LEFT)
    fill(255)
    stroke_cap(ROUND)
    line(20, 30, 80, 30)
    text("stroke_cap('ROUND') (default)", 100, 35)
    stroke_cap(SQUARE)
    line(20, 70, 80, 70)
    text("stroke_cap('SQUARE')", 100, 75)
    stroke_cap(PROJECT)
    line(20, 110, 80, 110)
    text("stroke_cap('PROJECT')", 100, 115)
    save('out.png')
    
def label(mode, x, y, extra=''):
    fill(255)
    text(f'stroke_join({mode})\n{extra}', x, y)
    
def corner(x, y):
    no_fill()
    triangle(x, y, x + 100, y, x + 50, y + 80)

    
