# port of aBe Hamoid's work!
# https://discourse.processing.org/t/program-to-test-hint-with-transparency/4361
# plus a few hints from https://processing.org/reference/hint_.html
# 19/11/2019 update: plus some ideas from GoToLoop

# ["name", hint_enabled, hint_disable_constant, hint_enable_constant]
hints = (["DEPTH_TEST", False,
          DISABLE_DEPTH_TEST, ENABLE_DEPTH_TEST],
         ["DEPTH_SORT", False,
          DISABLE_DEPTH_SORT, ENABLE_DEPTH_SORT],
         ["DEPTH_MASK", False,
          DISABLE_DEPTH_MASK, ENABLE_DEPTH_MASK],
         ["OPTIMIZED_STROKE", True,
          DISABLE_OPTIMIZED_STROKE, ENABLE_OPTIMIZED_STROKE],
         ["STROKE_PERSPECTIVE", False,
          DISABLE_STROKE_PERSPECTIVE, ENABLE_STROKE_PERSPECTIVE],
         )
use_sphere = False


def setup():
    size(800, 600, P3D)
    apply_hints()

def draw():
    this.surface.title = 'FPS: {}'.format(this.round(frameRate))
    background(255)

    fill(0)
    for i, (name, status, _, _) in enumerate(hints):
        text("{} {}".format(name, str(status)), 20, 20 + i * 20)
    text("<- use the mouse to toggle settings", 200, 40)
    text("click here to toggle shape", 300, 580)
    
    fill(255, 40, 20, 100)
    translate(width / 2, height / 2)
    rotateY(frameCount * 0.005)

    for x in range(-200, 201, 200):
        for y in range(-200, 201, 200):
            pushMatrix()
            translate(x, 0, y)
            if use_sphere:
                sphere(90)
            else:
                box(180)
            popMatrix()

def mousePressed():
    global use_sphere    
    if mouseY > height - 100:
        use_sphere = not use_sphere

    id = mouseY / 20
    if id < len(hints):
        hints[id][1] = not hints[id][1]
        
    apply_hints()    

def apply_hints():
    for _, status, disable_const, enable_const in hints:
        hint(enable_const if status else disable_const)
