add_library('video')    # import processing.video.*
add_library('opencv_processing') # import gab.opencv.*

from particles import ParticleSystem
debug = False
gravity = 0.05

def setup():
    global video, opencv
    size(1000, 600)
    colorMode(HSB)
    cameras = Capture.list()
    video = Capture(this, 320, 240, cameras[0])
    video.start()
    opencv = OpenCV(this, 640/2, 480/2)
    create_system()
    
def create_system():
    global particles
    particles = ParticleSystem(PVector(width / 2, 50))
    for _ in range(60):
        particles.addParticle(PVector(random(width), random(height)))
    background(0)

def draw():
    background(0)
    # fill(0, 10)
    # rect(0, 0, width, height)
    opencv.loadImage(video)
    opencv.calculateOpticalFlow()
    ave_flow = PVector().set(opencv.getAverageFlow())
    # print ave_flow
    if ave_flow.x == ave_flow.x: # to avoid NaN :)
        particles.run(PVector(ave_flow.x, ave_flow.y + gravity))
#        particles.run(ave_flow)
    if debug:
        tint(255, 100)
        #image(video, 0, 0)
        stroke(255)
        strokeWeight(0.5)
        opencv.drawOpticalFlow()
            
def keyPressed():
    global debug
    if key == 'd':
        debug = not debug
    if key == ' ':
        create_system()
        
        
def captureEvent(c):
    if debug:
        print(frameCount, frameRate)
    c.read()
