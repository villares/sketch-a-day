from villares.gif_export import gif_export
add_library('gifAnimation')


siz = 37.5  # tamanho da grade
font_size = 38 # tamanho das letras
noise_scale = 0.01


def setup():
    global img, fontes
    size(700, 700)
    smooth()
    noStroke()
    fontes = (
              createFont("Inconsolata ExtraLight", font_size),
              createFont("Inconsolata Light", font_size),
              createFont("Inconsolata Regular", font_size),
              createFont("Inconsolata Medium", font_size),
              createFont("Inconsolata SemiBold", font_size),
              createFont("Inconsolata Bold", font_size),
              createFont("Inconsolata ExtraBold", font_size),
              createFont("Inconsolata Black", font_size),
    )
    textAlign(CENTER, CENTER)
    background(200, 200, 0)


def draw():
    background(240, 240, 0)
    f = 500 + 250 * sin(radians(frameCount / 1.0)) 
    g = 500 + 250 * cos(radians(frameCount / 1.0 )) 
    i = 0
    of = 10
    for y in xrange(10, width - siz, siz):
        for x in xrange(0, height - siz / 2, siz / 2):
            bc = 255 * noise((x + g) * noise_scale, f * noise_scale, y * noise_scale, )
            bc2 = 255 * noise((x + of + g) * noise_scale, f * noise_scale, (y + of) * noise_scale, )        
            w = map(bc, 80, 150, 0, len(fontes)-1)
            w = constrain(w, 0, 7)
            c = is_this_a_man[i]
            fill(0)
            if c not in u'/—':
                textFont(fontes[int(w)])
            else:
                textFont(fontes[0])
            fill(0, 0, 200, 128)
            text(c, x + siz / 2 + bc2 / 100, y + siz / 2 + bc2 / 100)
            i = (i + 1) % len(is_this_a_man)
    filter(BLUR)       
    i = 0
    of = 10
    for y in xrange(10, width - siz, siz):
        for x in xrange(0, height - siz / 2, siz / 2):
            bc = 255 * noise((x + g) * noise_scale, f * noise_scale, y * noise_scale, )
            bc2 = 255 * noise((x + of + g) * noise_scale, f * noise_scale, (y + of) * noise_scale, )        
            w = map(bc, 80, 150, 0, len(fontes)-1)
            w = constrain(w, 0, 7)
            c = is_this_a_man[i]
            fill(0)
            if c not in u'/—':
                textFont(fontes[int(w)])
            else:
                textFont(fontes[0])            
            fill(0, 255)
            text(c, x + siz / 2, y + siz / 2)
            i = (i + 1) % len(is_this_a_man)

    gif_export(GifMaker)
    if frameCount / 1.0 > 360:
        gif_export(GifMaker, finish=True)
    
def keyPressed():
    if key == 's':
        saveFrame("a####.png")

# Primo Levi
is_this_a_man = \
u"""You who live safe/\
In your warm houses,/\
You who find, returning in the evening,/\
Hot food and friendly faces:/\
Consider if this is a man/\
Who works in the mud/\
Who does not know peace/\
Who fights for a scrap of bread/\
Who dies because of a yes or a no./\
Consider if this is a woman,/\
Without hair and without name
With no more strength to remember,/\
Her eyes empty and her womb cold/\
Like a frog in winter./\
Meditate that this came about:/\
I commend these words to you./\
Carve them in your hearts/\
At home, in the street,/\
Going to bed, rising;/\
Repeat them to your children,/\
Or may your house fall apart,/\
May illness impede you,/\
May your children turn their faces from you./\
 — Primo Levi, 1919—1987            
"""
    
