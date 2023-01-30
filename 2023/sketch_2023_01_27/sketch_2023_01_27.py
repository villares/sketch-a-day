# Based on Tom Larrow's experiment at:
# https://codeberg.org/TomLarrow/creative-coding-experiments/src/branch/main/x_0049/x_0049.py

def setup():
    size(800, 800)
    no_loop()
    no_stroke()
    color_mode(HSB)

def draw():
    background(150, 100, 100)     
    margin = width / 16  # Give us a margin on the right
    x = margin
    while x < width - margin:
        w = random_int(2, 7) * 5
        h = height * random_int(5, 10) / 12
        y = (height - h) / 2
        if x + w > width - margin:
            w = (width - margin) - x
        fill(w * 8, 200, 200)
        rect(x, y, w, h) 
        x += w    
        
    # Now that we have the image above, lets add grain, but only to the parts
    # that aren't the background
    load_np_pixels()  # Load the processing pixel array as an uint8 numpy array
    # Build a new numpy array the same size to hold our noise, and fill it with random values
    # It is an signed 16 array, so that it can handle negative numbers and
    # buffer overflows
    noise_pixels = np.random.randint(-50, 50, size=(width, height, 4))
    # np_pixels gives each pixel in an [A, R, G, B] format. We don't want to mess with the alpha, so setting
    # all the alpha values to zero, so that they don't change when we start
    # doing math on the array
    noise_pixels[:, :, 0] = 0
    # Add the contents of np_pixels to our noise_pixels array
    # This gives us an array where every pixel is adjusted by noise
    noise_pixels += np_pixels
    # Because our noise_pixels array is a signed 16-bit integer it can have negative numbers or numbers greater than 255
    # So we clip them to stay in those bounds to avoid buffer overflows once
    # we go back to uint8
    noise_pixels = np.clip(noise_pixels, 0, 255)
    # the numpy where function lets us make decisions based on a condition
    # I know that pixel 0,0 is a background color, so I compare each pixel to 0,0 to see if it's the background or not
    # If it is the background, copy in the value for that pixel from np_pixels (which is just our background)
    # Otherwise, copy in the value from our noise_pixels
    # This is how we end up with only the foreground components having grain
    my_display = np.where(np_pixels == np_pixels[0, 0], np_pixels, noise_pixels)
    set_np_pixels(my_display)  # Copy our new array back to np_pixels
    update_pixels()  # And run update_pixels() to actually see the results

def key_pressed():
    redraw()