well = {}
piece = [((2, 2), 'b'), ((3, 2), 'b'), ((4, 2), 'b'), ((4, 3), 'b')]
cores = {
    'b': color(0, 0, 200),  # azul
    'w': 128  # cinza
    }

W = 10
H = 20
s = 25

def setup():
    size(525, 525)
    for y in range(H):
        well[0, y] = 'w'
        well[W, y] = 'w'
    for x in range(W + 1):
        well[x, H] = 'w'
    
def draw():
    background(0)
    for (x, y), b in list(well.items()) + piece:
        fill(cores[b])
        square(x * s, y * s, s)
        
    if frame_count % 10 == 0 and check_move(0, 1):
        move_piece(0, 1)
                
def check_move(h, v):
    for (x, y), _ in piece:
        if well.get((x + h, y + v)):
            return False
    return True

def move_piece(h, v):
    piece[:] = (((x + h, y + v), b) for (x, y), b in piece)

