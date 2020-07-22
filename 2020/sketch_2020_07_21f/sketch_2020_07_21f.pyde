"""
Simple Real-Time Slit-Scan Program.  By Golan Levin.

Ported to Python mode.
h
This demonstration depends on the canvas height being equal 
to the video capture height. If you would prefer otherwise, 
consider using the image copy() def rather than the 
direct pixel-accessing approach I have used here. 
"""

add_library('video')


def setup():
    global video, videoSliceX, drawPositionX

    size(600, 240)

    # This the default video input, see the GettingStartedCapture
    # example if it creates an error
    video = Capture(this, 320, 240)

    # Start capturing the images from the camera
    video.start()

    videoSliceX = video.width / 2
    drawPositionX = width - 1
    background(0)


def draw():
    global drawPositionX
    if video.available():
        video.read()
        video.loadPixels()

        # Copy a column of pixels from the middle of the video
        # To a location moving slowly across the canvas.
        loadPixels()
        for y in range(video.height):
            setPixelIndex = y * width + drawPositionX
            getPixelIndex = y * video.width + videoSliceX
            pixels[setPixelIndex] = video.pixels[getPixelIndex]

        updatePixels()

        drawPositionX -= 1
        # Wrap the position back to the beginning if necessary.
        if drawPositionX < 0:
            drawPositionX = width - 1
