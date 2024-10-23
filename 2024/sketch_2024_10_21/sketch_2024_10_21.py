import py5  # check out https://github.com/py5coding 

# matplotlib must be installed for py5 to know the color names!

def setup():
    py5.size(600, 200)
    cores = ['RED', 'green', 'blue', 'gray', 'white', py5.css4_colors.BISQUE]
    x = 50
    for cor in cores:
        py5.fill(cor)
        py5.circle(x, 100, 100)
        x += 100
        
py5.run_sketch(block=False)