ROTATION = {0 : 0, BOTTOM : 0, DOWN : 0,
            1 : HALF_PI, LEFT : HALF_PI,
            2 : PI, TOP : PI, UP : PI,
            3 : PI + HALF_PI, RIGHT: PI + HALF_PI,
            BOTTOM + RIGHT : 0, DOWN + RIGHT : 0,
            BOTTOM + LEFT : HALF_PI, DOWN + LEFT : HALF_PI,
            TOP + LEFT : PI, UP + LEFT : PI,
            TOP + RIGHT: PI + HALF_PI, UP + RIGHT: PI + HALF_PI,
            }
    
def quarter_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, ROTATION[quadrant], HALF_PI)

def half_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, ROTATION[quadrant], PI)

def circle_arc(x, y, radius, start_ang, sweep_ang):
    arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang)
