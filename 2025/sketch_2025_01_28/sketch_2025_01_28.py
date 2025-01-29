import py5

yo = 0 # vertical offset
noise_scale = 0.01
step = 15

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    py5.no_stroke()
    
def draw():
    py5.background(0)
    for x in range(0, 600, step):
        for y in range(0, 600, step):
            n = py5.os_noise(
                x * noise_scale,
                (y + yo) * noise_scale,
                py5.frame_count * noise_scale,
                         #mouse_y * noise_scale,
                         ) # -1 a 1
            d = py5.remap(n, -1, 1, 1, step)
            matiz = py5.remap(n, -1, 1, 0, 255)
            py5.fill(matiz, 200, 200)
            py5.circle(x + step / 2, y + step / 2, d)
        
def mouse_wheel(e):
    global yo
    yo += e.get_count() * step
    
py5.run_sketch()