
import py5
from pymunk_helpers import Simulation, Segment, Ball

def setup():
    global sim
    py5.size(600, 600)
    sim = Simulation(gravity=(0, 900))
    Segment(50, 500, 550, 500, static=True)
    Ball(100, 100, 100)
    
def draw():
    py5.background(0, 0, 200)
    sim.draw_and_update(step=1/60)
    
def mouse_dragged():
    Ball(py5.mouse_x, py5.mouse_y, py5.random(10, 50))
    
py5.run_sketch()