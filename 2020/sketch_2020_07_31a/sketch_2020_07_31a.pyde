add_library('video')    # import processing.video.*
add_library('opencv_processing') # import gab.opencv.*


from particles import ParticleSystem

def setup():
    global video, opencv, particles
    size(400, 400)
    video = Capture(this, 640/2, 480/2)
    opencv = OpenCV(this, 640/2, 480/2)
    video.start()

    particles = ParticleSystem(PVector(width / 2, 50))
    # repeller = Repeller(width / 2, 280, power=20000)
    colorMode(HSB)
    for _ in range(20):
        particles.addParticle(PVector(random(width), random(height)))



def draw():
    background(0)
    opencv.loadImage(video)
    opencv.calculateOpticalFlow()
    ave_flow = PVector().set(opencv.getAverageFlow())
    print ave_flow
    if ave_flow.x == ave_flow.x: # to avoid NaN :)
        particles.run(ave_flow)

    stroke(255)
    scale(1.5, 2)
    opencv.drawOpticalFlow()


        
def captureEvent(c):
    c.read()
