"""
Porting Brightness Thresholding
by Golan Levin
to Python Mode
 
Determines whether a test location (such as the cursor) is contained within
the silhouette of a dark object.
"""
add_library('video')

black = color(0)
white = color(255)

def setup():
    global video, num_pixels
    size(640, 480)  # Change size to 320 x 240 if too slow at 640 x 480
    strokeWeight(5)

    # This the default video input, see the GettingStartedCapture
    # example if it creates an error
    video = Capture(this, width, height)

    # Start capturing the images from the camera
    video.start()

    num_pixels = video.width * video.height
    noCursor()
    smooth()


def draw():
    if video.available():
        video.read()
        video.loadPixels()
        threshold = 127  # Set the threshold value
        # Turn each pixel in the video frame black or white depending on its
        # brightness
        loadPixels()
        for i in range(num_pixels):
            pixel_brightness = brightness(video.pixels[i])
            # If the pixel is brighter than the
            if pixel_brightness > threshold:
                pixels[i] = white  # threshold value, make it white
            else:  # Otherwise,
                pixels[i] = black  # make it black

        updatePixels()
        # Test a location to see where it is contained. Fetch the pixel at the test
        # location (the cursor), and compute its brightness
        testValue = get(mouseX, mouseY)
        testBrightness = brightness(testValue)
        if testBrightness > threshold:  # If the test location is brighter than
            fill(black)  # the threshold set the fill to black
        else:  # Otherwise,
            fill(white)  # set the fill to white

        ellipse(mouseX, mouseY, 20, 20)
