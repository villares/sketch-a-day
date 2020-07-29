"""
Frame Differencing Video Capture library example by Golan Levin.
Quantify the amount of movement in the video frame using frame-differencing.
"""
add_library('video')   # import processing.video.*


def setup():
    global video, num_px, previous_frame
    size(640, 480)
    # This the default video input, see the GettingStartedCapture
    # example if it creates an error
    video = Capture(this, width, height)
    # Start capturing the images from the camera
    video.start()
    num_px = video.width * video.height
    # Create an array to store the previously captured frame
    previous_frame = [0] * num_px
    loadPixels()


def draw():
    if video.available():
        # When using video to manipulate the screen, use video.available() and
        # video.read() inside the draw() method so that it's safe to draw to
        # the screen
        video.read()  # Read the new frame from the camera
        video.loadPixels()  # Make its pixels[] array available

        movement_sum = 0  # Amount of movement in the frame
        # For each pixel in the video frame...
        for i in range(num_px):
            currColor = video.pixels[i]
            prevColor = previous_frame[i]
            # Extract the red, green, and blue components from current pixel
            currR = (currColor >> 16) & 0xFF  # Like red(), but faster
            currG = (currColor >> 8) & 0xFF
            currB = currColor & 0xFF
            # Extract red, green, and blue components from previous pixel
            prevR = (prevColor >> 16) & 0xFF
            prevG = (prevColor >> 8) & 0xFF
            prevB = prevColor & 0xFF
            # Compute the difference of the red, green, and blue values
            diffR = abs(currR - prevR)
            diffG = abs(currG - prevG)
            diffB = abs(currB - prevB)
            # Add these differences to the running tally
            movement_sum += diffR + diffG + diffB
            # Render the difference image to the screen
            # diff = color(diffR, diffG, diffB), but done with bitwise operations
            diff =  0xff000000 | (diffR << 16) | (diffG << 8) | diffB
            # pixels[i]= diff
            # pixels[i] = 0xffffffff if brightness(diff) < 64 else 0xff000000
            pixels[i] = 0xffffffff if diffR+diffG+diffB < 64 else 0xff000000
            # Save the current into the 'previous' buffer
            previous_frame[i] = currColor

        # updatePixels()
        # To prevent flicker from frames that are all black (no movement),
        # only update the screen if the image has changed.
        if movement_sum / 1000000 > 2:
            updatePixels()
        #     # Print the total amount of movement to the console
        print(movement_sum / 1000000, frameRate)
