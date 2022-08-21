
increment = 0.01
# The noise function's 3rd argument, a global variable that increments
# once per cycle
zoff = 0.0
# We will increment zoff differently than xoff and yoff
zincrement = 0.02


def setup():
    size(320, 320)
    frame_rate(30)


def draw():
    scale(2)
    print(get_frame_rate())
    global zoff
    # Optional: adjust noise detail here
    # noiseDetail(8,0.65f)
    load_np_pixels()
    xoff = 0.0  # Start xoff at 0

    # For every x,y coordinate in a 2D space, calculate a noise value and
    # produce a brightness value
    for x in range(width):
        xoff += increment     # Increment xoff
        yoff = 0.0     # For every xoff, start yoff at 0
        for y in range(height):
            yoff += increment  # Increment yoff

            # Calculate noise and scale by 255
            bright = 128 + os_noise(xoff, yoff, zoff) * 128
            # Try using this line instead
            # float bright = random(0,255)

            # Set each pixel onscreen to a grayscale value
            np_pixels[y, x, 1:] = [0, 255 - bright, bright]
    update_np_pixels()
    zoff += zincrement  # Increment zoff