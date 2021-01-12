"""
Use something other than a computer as an autonomous process (or use a non-computer random source).
"""
from math import isnan
add_library('video')
add_library('opencv_processing') # import gab.opencv.*
walker = PVector()

def setup():
    global video, opencv
    size(400, 400)
    video = Capture(this, 320, 240) 
    video.start()
    opencv = OpenCV(this, 320, 240)
    background(0)
    noStroke()
    
def draw():
    global walker
    translate(width / 2, height / 2)
    opencv.loadImage(video)
    opencv.calculateOpticalFlow()
    average_flow = PVector().set(opencv.getAverageFlow())
    walker += average_flow * 5  if not isnan(average_flow.mag()) else PVector(0, 0)
    circle(walker.x, walker.y, 10)
     
def captureEvent(c):
    c.read()
