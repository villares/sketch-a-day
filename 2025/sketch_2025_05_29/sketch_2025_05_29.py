import py5

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    
def draw():
    py5.background(240)
    passo = 0.01
    for x in range(500):
        n = py5.noise((x + py5.mouse_x) * passo, py5.mouse_y * passo)
        y = n * 250
        py5.stroke(y, 200, 200)
        py5.line(x, 250, x, 250 - y)
        
    passo = 0.01
    for x in range(500):
        n = py5.os_noise((x + py5.mouse_x) * passo, py5.mouse_y * passo) # precisa x, y
        y = 125 + n * 125
        py5.stroke(y, 200, 200)
        py5.line(x, 500, x, 500 - y)
        
py5.run_sketch()