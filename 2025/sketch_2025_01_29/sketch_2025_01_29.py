import py5

yo = 0 # vertical offset
noise_scale = 0.02

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    py5.no_stroke()
    py5.rect_mode(py5.CENTER)
    
def draw():
    py5.background(0)
    grid(0, 0, 600, 4)
    
    
def grid(xg, yg, w, order=2):
    step = w / order
    for i in range(order):
        x = xg + i * step
        for j in range(order):
            y = yg + (j * step) 
            n = py5.os_noise(
                x * noise_scale,
                (y + yo) * noise_scale,
                py5.mouse_x / 100 * noise_scale,
                         ) # -1 a 1
            d = py5.remap(n, -1, 1, 1, step)
            matiz = py5.remap(n, -1, 1, 0, 255)
            py5.fill(matiz, 200, 200)
            if step > 10 and n > 0.2:
                grid(x, y, step)             
            else:
                py5.square(x + step / 2, y + step / 2, step - 3)
        
def mouse_wheel(e):
    global yo
    yo += e.get_count()
    
py5.run_sketch()