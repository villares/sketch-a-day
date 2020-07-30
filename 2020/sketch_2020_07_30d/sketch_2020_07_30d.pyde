add_library('video')    # import processing.video.*
add_library('opencv_processing') # import gab.opencv.*

def setup():
    global video, opencv
    size(320, 240)
    video = Capture(this, 640/2, 480/2)
    opencv = OpenCV(this, 640/2, 480/2)
    video.start()

def draw():
    background(0)
    opencv.loadImage(video)
    opencv.calculateOpticalFlow()
    image(video, 0, 0)
    stroke(255,0,0); strokeWeight(1)
    opencv.drawOpticalFlow()
    ave_flow = opencv.getAverageFlow()
    scale_up = 20
    stroke(255); strokeWeight(3)
    line(video.width / 2,
         video.height / 2,
         video.width / 2 + ave_flow.x * scale_up,
         video.height / 2 + ave_flow.y * scale_up)
    
def captureEvent(c):
    c.read()
