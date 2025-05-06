import py5
import geobr  # https://github.com/ipeaGIT/geobr

T = {'x': 0, 'y': 0, 'scale': 1, 'i': 0}

def setup():
    global main_shp, geodata
    py5.size(1000, 1000)
    py5.stroke_join(py5.ROUND)
    py5.color_mode(py5.HSB)
    #ancient = geobr.read_municipality(code_muni="all", year=1872)
    geodata = geobr.read_municipality(code_muni="all", year=2022)
    x_min, y_min, x_max, y_max = geodata.total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h
    translate_and_scale_gdf(geodata, -x_min, -y_min, x_scale, -y_scale)    
    
    state_names = sorted(set(a for a in geodata.name_state if str(a) != 'nan'))
    state_color = {a: py5.color(i * (255 / len(state_names)),
                             200, 200)
                             #128 + (i % 3) * 64 , 128 + (i % 2) * 128)
                for i, a in enumerate(state_names)}
    print(state_names)
    main_shp = py5.create_shape(py5.GROUP)
    py5.stroke_weight(0.1)
    for g, s in zip(geodata.geometry, geodata.name_state):
        if c := state_color.get(s):
            py5.fill(c)
        else:
            py5.fill(200)
        main_shp.add_child(py5.convert_shape(g))


def draw():
    py5.background(200)
    with py5.push_matrix():
        py5.translate(T['x'], T['y'])
        py5.scale(T['scale'])
        py5.shape(main_shp, 0, py5.height)

def translate_and_scale_gdf(gdf, x, y, x_scale, y_scale):
    gdf['geometry'] = gdf.geometry.translate(x, y)
    gdf['geometry'] = gdf.geometry.scale(
        xfact=x_scale, yfact=y_scale, origin=(0, 0))

def mouse_wheel(e):
    print(T)
    xrd = (py5.mouse_x - T['x']) / T['scale']
    yrd = (py5.mouse_y - T['y']) / T['scale']
    T['i'] -= e.get_count()
    T['scale'] = 1.1 ** T['i']
    T['x'] = py5.mouse_x - xrd * T['scale']
    T['y'] = py5.mouse_y - yrd * T['scale']

def mouse_dragged():
    print(T) 
    T['x'] += py5.mouse_x - py5.pmouse_x
    T['y'] += py5.mouse_y - py5.pmouse_y

def key_pressed():
    print('salvando png')
    py5.save_frame('###out.png')

py5.run_sketch()