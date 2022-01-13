boxes = []

def setup():
    size(500, 500, P3D)
    create_boxes()
    
def create_boxes():
    boxes[:] = []
    while len(boxes) < 1000:
        w = int(random(1, 20)) * 12
        h = int(random(1, 20)) * 12
        d = int(random(1, 20)) * 12
        hw, hh, hd = w / 2, h / 2, d / 2
        x = int(random(hw, width - hw) - width / 2)
        y = int(random(hh, height - hh) - height / 2)
        z = int(random(hd, height - hd) - height / 2)
        b = Box(x, y, z, w, h, d)
        if not box_boxes_intersection(b):
            boxes.append(b)

def draw():
    background(0)
    translate(width / 2, height / 2, -height)
    rotateY(frameCount / 100.0)
    for b in boxes:
        b.plot()    

def keyPressed():
    create_boxes()

def box_boxes_intersection(b):
    for other in boxes:
        if box_box_intersection(b, other):
            return True
    return False

def box_box_intersection(a, b):
    a_max_x, a_max_y, a_max_z = a.max
    a_min_x, a_min_y, a_min_z = a.min
    b_max_x, b_max_y, b_max_z = b.max
    b_min_x, b_min_y, b_min_z = b.min
    if a_max_x < b_min_x or b_max_x < a_min_x:
        return False
    if a_max_y < b_min_y or b_max_y < a_min_y:
        return False
    if a_max_z < b_min_z or b_max_z < a_min_z:
        return False
    return True

class Box():
    
    def __init__(self, x, y, z, w, h=None, d=None):        
        if not h: h = w
        if not d: d = h
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.d = d
        self.points = self.calc_points()
        self.min = self.points[0]
        self.max = self.points[-1]
        
    @property
    def color(self):
        return color(
            128 + self.w % 128,
            128 + self.h % 128,
            128 + self.d % 128,
        )
        
    def calc_points(self):
        hw, hh, hd =  self.w / 2.0,  self.h / 2.0,  self.d / 2.0
        return (
            (self.x - hw, self.y - hh, self.z - hd),    
            (self.x - hw, self.y + hh, self.z - hd),    
            (self.x + hw, self.y - hh, self.z - hd),    
            (self.x + hw, self.y + hh, self.z - hd), 
            (self.x - hw, self.y - hh, self.z + hd),    
            (self.x - hw, self.y + hh, self.z + hd),    
            (self.x + hw, self.y - hh, self.z + hd),    
            (self.x + hw, self.y + hh, self.z + hd),    
        )
        
        
    def plot(self):
        push()
        translate(self.x, self.y, self.z)
        fill(self.color)
        box(self.w, self.h, self.d)
        pop()
        
    def plot_points(self):
        for x, y, z in (self.min, self.max): #self.points:
            push()
            translate(x, y, z)
            fill(255)
            box(5)
            pop()
        
    def __repr__(self):
        return "Box({}, {}, {}, {}, {}, {}).color={}".format(
            self.x,
            self.y,
            self.z,
            self.w,
            self.h,
            self.d,
            self.color
        )
