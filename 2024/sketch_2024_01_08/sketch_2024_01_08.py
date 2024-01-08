# based on branrickman's
# https://github.com/branrickman/double-pyndulum-interactive/blob/master/src/main.py

import py5
import pymunk

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
FPS = 50

pendulum_group = []

def setup():
    py5.size(800, 800)
    py5.no_stroke()
    pendulum_group[:] = [
        Pendulum(200, 500, 300, 600, number=2, mode=False),
        Pendulum(200, 600, 300, 600, number=1, mode=False),
    ]

def draw():
    py5.background(0)
    space.step(1 / FPS)
    for pendulum in pendulum_group:
        pendulum.draw()

# pymunk variables
space = pymunk.Space()
space.gravity = (0, -900)

# colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 255, 0)
YELLOW = (235, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 255)

color_list = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE] * 2

def convert_coords(point):  # convert to int, transform to pygame y convention
    return int(point[0]), int(SCREEN_HEIGHT - point[1])

class PendulumConnector:
    def __init__(self, body, link, link_type='body'):
        self.body = body
        if link_type == 'body':
            self.link = link
        elif link_type == 'static_body':
            self.link = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.link.position = link
        joint = pymunk.PinJoint(self.body, self.link)
        joint.collide_bodies = False
        space.add(joint)

    def draw(self):
        pos1 = convert_coords(self.body.position)
        pos2 = convert_coords(self.link.position)
        py5.stroke(255)
        py5.stroke_weight(5)
        py5.line(*pos1, *pos2) #, 5)
        py5.no_stroke()
        py5.circle(*convert_coords(self.link.position), 5)


class PendulumPoint:
    def __init__(self, x, y, number):
        # pymunk properties
        self.body = pymunk.Body()
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.collision_type = 2
        self.position_log = []
        self.position_trail_radius = 5

        self.radius = 10
        self.color = color_list[number]

        space.add(self.body, self.shape)

    def draw(self):
        converted_position = convert_coords(self.body.position)
        self.position_log.append(converted_position)
        py5.fill(*self.color)
        py5.circle(*converted_position, self.radius * 2)


class Pendulum:
    def __init__(self, x1, y1, x2, y2, number, x3=(SCREEN_WIDTH // 2), y3=(SCREEN_HEIGHT // 2), mode=0):
        self.pend_point1 = PendulumPoint(x1, y1, number)
        self.pend_point2 = PendulumPoint(x2, y2, number + 4)
        self.pend_conn1 = PendulumConnector(self.pend_point1.body, (x3, y3), link_type='static_body')
        self.pend_conn2 = PendulumConnector(self.pend_point1.body, self.pend_point2.body, link_type='body')
        self.static_x = x3
        self.static_y = y3
        self.mode = mode
        self.draw_trail = True

    def draw(self):
        if self.draw_trail:
            for i in range(len(self.pend_point1.position_log)):
                py5.fill(*self.pend_point1.color)
                py5.circle(*self.pend_point1.position_log[i],
                            self.pend_point1.position_trail_radius * 2)
            for i in range(len(self.pend_point2.position_log)):
                py5.fill(*self.pend_point2.color)
                py5.circle(*self.pend_point2.position_log[i],
                            self.pend_point2.position_trail_radius * 2)
        if self.mode:
            self.pend_conn1.draw()
            self.pend_conn2.draw()
        self.pend_point1.draw()
        self.pend_point2.draw()

   
py5.run_sketch()