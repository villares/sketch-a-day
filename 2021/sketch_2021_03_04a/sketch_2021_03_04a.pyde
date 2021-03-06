siz = 36  # tamanho da grade
font_size = 38 # tamanho das letras
noise_scale = 0.01


def setup():
    global img, fontes
    size(808, 808)
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


def draw():
    background(240)
    xend = width # img.width
    yend = height #img.height
    # img.loadPixels()
    # Begin our loop for every pixel
    f = sin(radians(frameCount / 10.0)) * 360
    g = cos(radians(frameCount / 10.0 )) * 360
    i = 0
    of = 10
    for y in xrange(0, yend - siz, siz):
        # xc = 0
        for x in xrange(0, xend - siz / 2, siz / 2):
            bc = 255 * noise((x + g) * noise_scale, f * noise_scale, y * noise_scale, )
            bc2 = 255 * noise((x + of + g) * noise_scale, f * noise_scale, (y + of) * noise_scale, )        
            w = int(map(bc, 80, 150, 0, len(fontes)-1))
            w = constrain(w, 0, 7)
            c = is_this_a_man[i]
            # print(w)
            textFont(fontes[w])
            fill(0, 0, 120, 100)
            text(c, x + siz / 2 + bc2 / 80, y + siz / 2 + bc2 / 80)
            fill(0)
            text(c, x + siz / 2, y + siz / 2)
            i = (i + 1) % len(is_this_a_man)


def keyPressed():
    if key == 's':
        saveFrame("a####.png")

# Primo Levi
is_this_a_man = \
"""
You who live safe
In your warm houses,
You who find, returning in the evening,
Hot food and friendly faces:
Consider if this is a man
Who works in the mud
Who does not know peace
Who fights for a scrap of bread
Who dies because of a yes or a no.
Consider if this is a woman,
Without hair and without name
With no more strength to remember,
Her eyes empty and her womb cold
Like a frog in winter.
Meditate that this came about:
I commend these words to you.
Carve them in your hearts
At home, in the street,
Going to bed, rising;
Repeat them to your children,
Or may your house fall apart,
May illness impede you,
May your children turn their faces from you.
"""
    
