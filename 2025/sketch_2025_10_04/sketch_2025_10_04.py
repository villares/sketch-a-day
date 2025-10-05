import py5

def setup():
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 100, 100)
    py5.background('w')
    for i in range(100):
        for j in range(100):
            py5.stroke(i, j)
            py5.point(i, j)
            
py5.run_sketch()