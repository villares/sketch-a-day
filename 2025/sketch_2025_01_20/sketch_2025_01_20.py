# based on s234 20180820
# based on sketch_2022_08_16
from itertools import product
GRID_SIZE = 32
border = 50
grid = dict()

# Cutting-plane position (press + & - to change)
cut_plane = GRID_SIZE // 3 * 2
seed = 582

def setup():
    global box_size
    size(700, 700, P3D)
    no_stroke()
    # sets border and grid box_size
    box_size = (width - border * 2) / GRID_SIZE
    print(box_size)
    # grid is a dict for a 3D grid
    for x, y, z in product(range(GRID_SIZE), repeat=3):
        grid[(x, y, z)] = None
    # crear objects
    create_rods()
    create_tubes()

def draw(): 
    point_light(255, 255, 255, -100, -100, -100)
    translate(0, 0, -height / 2)
    background(0)   
    for (x, y, z), state in grid.items():
        if z < cut_plane and state is not None:
            plot_box(x, y, z, box_size)


def create_rods():
    # sets the objects, list of tuples -> hollowed boxes
    random_seed(seed)
    m = GRID_SIZE - 1
    box_list = []
    num_boxes = 10
    border = 1
    for i in range(num_boxes):
        # random size in range 3 to GRID_SIZE - borders
        w = random_int(3, m - border * 2)
        h = random_int(3, m - border * 2)
        d = random_int(3, m - border * 2)
        # random position
        x = random_int(border, m - w - border)
        y = random_int(border, m - h - border)
        z = random_int(border, m - d - border)
        big_ugly(x, y, z, w, h, d)

def key_pressed():
    """ press P to save an image """
    global seed
    if key in ['p', 'P']:
        save_frame(f's{seed}.png')
    if key == ' ':
        grid.clear()
        seed = random_int(1000)  # seed = 205
        random_seed(seed)
        print(f"seed: {seed}")
        create_rods()
        create_tubes()
    # cut plane adjust
    global cut_plane
    if key == '-':
        cut_plane -= 1
        print(cut_plane)
    if key in ['+', '=']:
        cut_plane += 1
        print(cut_plane)


def big_box(px, py, pz, w, h=None, d=None, c=255):
    h = h if h else w
    d = d if d else w
    for z, y, x in product(range(pz, pz + d),
                           range(py, py + h),
                           range(px, px + w)):
        if (0 <= x < GRID_SIZE and
            0 <= y < GRID_SIZE and
            0 <= z < GRID_SIZE):
            grid[(x, y, z)] = c


def big_ugly(px, py, pz, w, h=None, d=None, c=255):
    h = h if h else w
    d = d if d else w
    for z, y, x in product(range(pz, pz + d),
                           range(py, py + h),
                           range(px, px + w)):
        if (0 <= x < GRID_SIZE and
            0 <= y < GRID_SIZE and
            0 <= z < GRID_SIZE):
            if w % 3 == 1:
                orient = x % 2 and y % 2
            elif w % 3 == 2:
                orient = x % 2 and z % 2
            else:
                orient = y % 2 and z % 2
            if orient:
                grid[(x, y, z)] = c

def create_tubes():
    # sets the objects, list of tuples -> hollowed boxes
    m = GRID_SIZE - 1
    tube_list = []
    num_tubes = 10
    border = 1
    for i in range(num_tubes):
        # random size in range 3 to GRID_SIZE - borders
        w = random_int(3, m - border * 2)
        h = random_int(3, m - border * 2)
        d = random_int(3, m - border * 2)
        # random position
        x = random_int(border, m - w - border)
        y = random_int(border, m - h - border)
        z = random_int(border, m - d - border)
        box_tuple = (x, y, z, w, h, d)
        #print(box_tuple)
        tube_list.append(box_tuple)
    # solid boxes
    for i, (x, y, z, w, h, d) in enumerate(tube_list):
        big_box(x, y, z, w, h, d,
                color(64 + (i % 3) * 32, 200, 200, 100))
    # erase inside boxes, making tubes
    for i, (x, y, z, w, h, d) in enumerate(tube_list):
        side = (i % 3) + 1
        if side == 1:
            h -= 2
            w -= 2
            z -= 1
        elif side == 2:
            d -= 2
            h -= 2
            x -= 1
        else:
            w -= 2
            d -= 2
            y -= 1
        big_box(x + 1, y + 1, z + 1, w, h, d,
                # use color(0) below, instead of None to debug
                # color(0))
                None)


def plot_box(x, y, z, side):
    front = ((-1, +1, -1),
             (-1, +1, +1),
             (+1, +1, +1),
             (+1, +1, -1),
             )
    back = ((-1, -1, -1),
            (-1, -1, +1),
            (+1, -1, +1),
            (+1, -1, -1),
            )
    left = ((-1, -1, -1),
            (-1, -1, +1),
            (-1, +1, +1),
            (-1, +1, -1),
            )
    right = ((+1, -1, -1),
             (+1, -1, +1),
             (+1, +1, +1),
             (+1, +1, -1),
             )
    down = ((-1, -1, -1),
            (+1, -1, -1),
            (+1, +1, -1),
            (-1, +1, -1),
            )
    top = ((-1, -1, +1),
           (+1, -1, +1),
           (+1, +1, +1),
           (-1, +1, +1),
           )

    faces = ((top, color(200, 200, 100)),
             (down, color(0, 0, 200)),
             (right, color(100, 100, 200)),
             (left, color(200, 100, 100)),
             (back, color(0, 159, 0)),
             (front, color(175)),
             )
    hs = side / 2  # half side
    with push_matrix():
        translate(x * side, y * side, z * side)
        scale(hs)
        no_stroke()
        with begin_shape(QUADS):
            for pts, shade in faces:
                fill(shade)
                vertices(pts)

