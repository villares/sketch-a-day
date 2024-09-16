import py5

grid = {}
w = 30

def setup():
    global w
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    n = py5.width // w
    for j in range(n):
        for i in range(n):
            s_limit = min(4, min(n - j, n - i))
            s = py5.random_int(1, s_limit)
            # print(s)
            if test_fit(i, j, s) or test_fit(i, j, s := 1):
                fill_grid(i, j, s)
                    
    py5.save('out.png')     
                
def fill_grid(i, j, s):
    py5.fill(s * 32, 255, 255, 100)
    py5.square(i * w, j * w, w * s)
    py5.fill(0)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text(str(s), i * w + (w * s)  / 2, j * w + (w * s) / 2)
    for di in range(s):
        for dj in range(s):
            grid[i + di, j + dj] = True
        
def test_fit(i, j, s):
    for di in range(s):
        for dj in range(s):
            if grid.get((i + di, j + dj)):
                return False
    return True
    
py5.run_sketch()