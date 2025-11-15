
import py5
import py5_tools

def setup():
    py5.size(500, 500)
    py5.background(0)
    py5_tools.animated_gif(
        'out.gif',
        frame_numbers=range(300, 450),
        duration=0.1)
    
def draw():
    print(py5.mouse_x)
    py5.translate(250, 250)
    py5.rotate(py5.radians(py5.mouse_x))
    py5.rect_mode(py5.CENTER)
    py5.square(250, 250, 200)

py5.run_sketch()
