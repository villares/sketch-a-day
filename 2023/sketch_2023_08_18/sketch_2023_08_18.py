# using py5 imported mode (https://py5coding.org to learn more)

def setup():
    global output_canvas
    size(600, 600)  # drawing size
    frame_rate(1)
    output_canvas = create_graphics(width, height)
    
def draw():
    background (0) # turn this on if you want... it won't record.
    begin_record(output_canvas) # starts recording
    output_canvas.clear()  # clears pixels 
    color_mode(HSB)  # this needs to be inside the recording!
    no_stroke()  # same as with the color_mode, has to be brought here
    w = 60
    for j in range(10):    
        y = w / 2 + j * w
        for i in range(10):   # 0, 1, 2, ... 9
            x = w / 2 + i * w
            d = random(10, w)
            fill(d * 3, 255, 255)
            circle(x + random(-15, 15),
                   y + random(-15, 15), d)
    end_record()  # end recording
    if frame_count <= 10: # only 10 images saved
        # frame number in the filename feature ('###.png') not available
        # when saving from the offscreen buffer, so I'm using an f-string.
        output_canvas.save(f'{frame_count}.png', drop_alpha=False)
        

