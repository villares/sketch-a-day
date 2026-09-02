import py5

N = 20
offset_x = offset_y = 0
keys = set()

def setup():
    global cell_size
    py5.size(600, 600, py5.P3D)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(20)
    cell_size = py5.width / N
    py5.no_fill()
    #py5.rect_mode(py5.CENTER)
    
def draw():
    global offset_x, offset_y
    py5.background(200)
    py5.no_fill()
    py5.rotate_x(py5.radians(15)) 
    si = int(offset_x / cell_size) - 1
    ei = int((offset_x + py5.width) / cell_size) + 1
    sj = int(offset_y / cell_size) - 1
    ej = int((offset_y + py5.height) / cell_size) + 1
    for i in range(si, ei):
        for j in range(sj, ej):
            x = i * cell_size + cell_size / 2 - offset_x
            y = j * cell_size + cell_size / 2 - offset_y
            
            with py5.push_matrix():
                
                for t in range(0, 11):
                    c = py5.lerp_color(0, 244, t / 10)
                    ij = py5.remap(t, 0, 10, i, j)
                    py5.stroke(c)
                    py5.circle(x, y, 10 + ij * 10)
                    py5.translate(0, 0, 20)
     #           py5.circle(x, y, 10 + i * 10)
            #py5.text(f'{i},{j}', x, y)

    if py5.LEFT in keys:
        offset_x -= 2
    if py5.RIGHT in keys:
        offset_x += 2
    if py5.UP in keys:
        offset_y -= 2
    if py5.DOWN in keys:
        offset_y += 2

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == py5.CODED:
        keys.add(py5.key_code)

def key_released():
    if py5.key == py5.CODED:
        keys.discard(py5.key_code)

py5.run_sketch(block=False)

