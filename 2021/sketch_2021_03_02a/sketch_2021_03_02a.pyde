siz = 23  # tamanho da grade
font_size = 28 # tamanho das letras
noise_scale = 0.01


def setup():
    global img, fontes
    size(918, 908)
    smooth()
    # textMode(MODEL)
    # img = loadImage("1.png")
    # this.surface.setResizable(True)
    # this.surface.setSize(img.width, img.height)
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
    # colorMode(HSB)


def draw():
    background(0, 128, 128)
    xend = width # img.width
    yend = height #img.height
    # img.loadPixels()
    # Begin our loop for every pixel
    f = frameCount / 2.0
    i = 0
    of = 1
    for y in xrange(0, yend, siz):
        # xc = 0
        for x in xrange(0, xend, siz):
            # bc = 128 * noise(x * noise_scale, y * noise_scale, f * noise_scale)
            h = 16 + (255 + 16) * noise(y * noise_scale, f * noise_scale, x * noise_scale, )
            bc = 255 * noise(x * noise_scale, f * noise_scale, y * noise_scale, )
            bc2 = 255 * noise((x + of) * noise_scale, f * noise_scale, (y + of) * noise_scale, )

            fill(255 - bc)
            w = int(map(bc, 80, 150, 0, len(fontes)-1))
            w = constrain(w, 0, 7)
            c = is_this_a_man[i]
            # print(w)
            textFont(fontes[w])
            text(c, x + siz / 2, y + siz / 2)
            i = (i + 1) % len(is_this_a_man)
            # if c != " ":
            #     xc += textWidth(c) * 1.2
            # xc += siz

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
    
