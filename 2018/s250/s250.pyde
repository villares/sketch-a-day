# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s250"  # 20180905
OUTPUT = ".png"

def settings():
    """ making it easier to add a markdown static "blog" entry """
    from log_aid import print_text_for_readme
    print_text_for_readme(SKETCH_NAME, OUTPUT)

def setup():
    size(400, 400)

def draw():
    background(220)
    with pushMatrix():
        translate(100, 200)
        rotate(frameCount/10.)
        noFill()
        ellipse(0, 0, 100, 100)
        fill(0)
        ellipse(50, 0, 10, 10)
    with pushMatrix():
        translate(300, 200)
        rotate(frameCount/20.)
        noFill()
        ellipse(0, 0, 100, 100)
        fill(0)
        ellipse(0, 50, 10, 10)
        
