
grid = {}
w = 60

def setup():
    global w
    size(600, 600)
    color_mode(HSB)
    n = width // w
    while len(grid) < n * n:
        for j in range(n):
            space_j = n - j
            for i in range(n):
                space_i = n - i
                s_limit = min(3, min(space_j, space_i))
                s = random_int(1, s_limit)
                print(s)
                if test_fit(i, j, s):
                    fill_grid(i, j, s)
                    fill(s * 32, 255, 255, 100)
                    square(i * w, j * w, w * s)
                    fill(0)
                    text_align(CENTER, CENTER)
                    text(str(s), i * w + w / 2, j * w + w / 2)
    save('out.png')     
                
def fill_grid(i, j, s):
    for di in range(s):
        for dj in range(s):
            grid[i + di, j + dj] = True
        
def test_fit(i, j, s):
    for di in range(s):
        for dj in range(s):
            if grid.get((i + di, j + dj)):
                return False
    return True
    
    