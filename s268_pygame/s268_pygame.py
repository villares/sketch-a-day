# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s268"  # 20180923

import pygame  # install Pygame https://www.pygame.org
from random import choice
from random import randint

gliphs = [lambda x, y, s: rect(x, y, s, s),
          lambda x, y, s: ellipse(x, y, s, s),
          lambda x, y, s: triangle(x - s, y, x - s, y + s, x, y + s),
          lambda x, y, s: triangle(x + s, y, x + s, y - s, x, y - s),
          ]

def setup():
    size(700, 700)
    rectMode(CENTER)

def draw():
    background(250)
    fill(120, 120, 200)
    noLoop()
    # ensamble of 5 , on grid also order=5
    grid(width/2, height/2, 5, 120, ensamble, 5)


def ensamble(ex, ey, order):
    for _ in range(order):
        order, spacing, side = randint(3, 11), 12, 6
        x, y = randint(-6, 5) * side, randint(-6, 5) * side
        grid(ex+x, ey+y, order, spacing, choice(gliphs), side)


def grid(x, y, order, spacing, function, *args):
    xo, yo = (x - order * spacing / 2, y - order * spacing / 2)
    for i in range(order):
        gx = spacing/2 + i * spacing
        for j in range(order):
            gy = spacing/2 + j * spacing
            function(xo + gx, yo + gy, *args)


# Now stuff to make it easier to port from Processing to Pygame

def triangle(x0, y0, x1, y1, x2, y2):
    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, current_fill,
                        [[x0, y0], [x1, y1], [x2, y2]], 0)
    pygame.draw.polygon(screen, current_stroke,
                        [[x0, y0], [x1, y1], [x2, y2]], stroke_weight)

def line(x1, y1, x2, y2):
    pygame.draw.line(screen, current_fill, [x1, y1], [x2, y2], stroke_weight)
#    pygame.draw.aaline(screen, current_stroke, [x1, y1],[x2, y2], True)

def rect(x, y, w, h):
    if _rect_mode == CENTER:
        x -= w/2
        y -= h/2
    pygame.draw.rect(screen, current_fill, [x, y, w, h], 0)
    pygame.draw.rect(screen, current_stroke, [x, y, w, h], stroke_weight)

def ellipse(x, y, w, h):
    pygame.draw.ellipse(screen, current_fill, [x, y, w, h], 0)
    pygame.draw.ellipse(screen, current_stroke, [x, y, w, h], stroke_weight)

def background(r, g=None, b=None):
    if g and b:
        screen.fill((r, g, b))
    else:
        screen.fill((r, r, r))

def fill(r, g=None, b=None):
    global current_fill
    if g and b:
        current_fill = (r, g, b)
    else:
        current_fill = (r, r, r)

def size(h, w):
    global height, width
    height, width = h, w

def noLoop():
    global _pause
    _pause = True

def loop():
    global _pause
    _pause = False
    
def rectMode(c):
    _rect_mode = c
        

def run():
    global CENTER, CORNER, _rect_mode
    _rect_mode = CORNER = 0
    CENTER = 3
    global width, height, screen, current_fill, current_stroke, stroke_weight, _pause
    # Initialize the game engine
    pygame.init()
    current_fill = (255, 255, 255)
    current_stroke = (0, 0, 0)
    stroke_weight = 1
    width, height = 100, 100
    _done = False
    _pause = False

    setup()

    # Set the height and width of the screen
    screen = pygame.display.set_mode([height, width])
    pygame.display.set_caption(SKETCH_NAME)
    clock = pygame.time.Clock()
    draw()
    # Loop until the user clicks the close button.
    while not _done:
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                _done = True  # Flag that we are _done so we exit this loop
            if event.type == pygame.KEYDOWN:
                    _pause = not _pause
        # All drawing code happens after the for loop and but
        # inside the main while _done==False loop.
        # Draw on screen
        if not _pause:
            draw()
        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
    # Be IDLE friendly
    pygame.quit()

run()
