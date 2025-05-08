import py5
import numpy as np

# zoom and pan transformation state dict
T = {'x': 0, 'y': 0, 'scale': 1, 'i': 0}

def setup():
    global main_shp
    py5.size(500, 500, py5.P2D)
    py5.stroke_join(py5.ROUND)
    
    x = np.linspace(0, 5, 500)
    y0 = x ** 3
    y1 = 1 / (py5.EPSILON + y0)
    y2 = x ** (1/3)
    pts0 = np.stack((x, -y0), axis=1) * 100
    pts1 = np.stack((x, -y1), axis=1) * 100
    pts2 = np.stack((x, -y2), axis=1) * 100

    main_shp = py5.create_shape(py5.GROUP)
    pts = py5.create_shape()
    with pts.begin_shape(py5.POINTS):
        pts.stroke_weight(5)
        pts.stroke(0, 0, 200)
        pts.vertices(pts0)
        pts.stroke(0, 200, 0)
        pts.vertices(pts1)
        pts.stroke(200, 0, 200)
        pts.vertices(pts2)
    main_shp.add_child(pts)

def draw():
    py5.background(0)
    with py5.push_matrix():
        py5.translate(T['x'], T['y'])
        py5.scale(T['scale'])
        py5.shape(main_shp, 0, py5.height)

def translate_and_scale_gdf(gdf, x, y, x_scale, y_scale):
    gdf['geometry'] = gdf.geometry.translate(x, y)
    gdf['geometry'] = gdf.geometry.scale(
        xfact=x_scale, yfact=y_scale, origin=(0, 0))

def mouse_wheel(e):
    xrd = (py5.mouse_x - T['x']) / T['scale']
    yrd = (py5.mouse_y - T['y']) / T['scale']
    T['i'] -= e.get_count()
    T['scale'] = 1.1 ** T['i']
    T['x'] = py5.mouse_x - xrd * T['scale']
    T['y'] = py5.mouse_y - yrd * T['scale']

def mouse_dragged():
    T['x'] += py5.mouse_x - py5.pmouse_x
    T['y'] += py5.mouse_y - py5.pmouse_y

def key_pressed():
    print('salvando png')
    py5.save_frame('###out.png')

py5.run_sketch()