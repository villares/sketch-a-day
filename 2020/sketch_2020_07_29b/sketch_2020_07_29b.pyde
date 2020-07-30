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
            # currB = brightness(currColor)
            currB = currColor & 0xFF 
            # prevB = brightness(prevColor)
            prevB = prevColor & 0xFF
            diff = abs(currB - prevB)
            # Add these differences to the running tally
            movement_sum += diff
            pixels[i] = 0xffffffff if diff > 64 else 0xff000000
            # Save the current into the 'previous' buffer
            previous_frame[i] = currColor

        # updatePixels()
        # To prevent flicker from frames that are all black (no movement),
        # only update the screen if the image has changed.
        if movement_sum / 1000 > 2:
            updatePixels()
        #     # Print the total amount of movement to the console
        print(movement_sum, frameRate)
