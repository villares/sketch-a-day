from functools import cache

from shapely import Polygon
import trimesh

def setup():
    size(800, 800, P3D)
    
def draw():
    no_stroke()
    translate(width / 2, height / 2)
    rotate_x(radians(45))
    translate(-width / 2, -height / 2)
    
    background(0)
    lights()
    for c in Element.element_list:
        c.draw()
        
def key_pressed():
    if key == 'c':
        Element.element_list.clear()
    elif key == ' ':
        p = len(Element.element_list)
        Element.add_element()
        while p != len(Element.element_list):
            Element.add_element()
            p = len(Element.element_list)
            print(p)
        
        #save_frame(f'{frame_count:0>5}.png')
    elif key == 's':
        save_snapshot_and_code()
    elif key == 'p':
        save_frame('s###.png')
           

class Element():
    
    NUM_ANGLES = 5
    element_list = []
    
    def __init__(self, x, y, d,
                 angle_origin=0,
                 generation=0,
                 parent_pos=None):
        self.x = x
        self.y = y
        self.d = d
        self.ao = angle_origin
        self.gen = generation
        if parent_pos:
            self.px, self.py = parent_pos
        else:
            self.px, self.py = x, y
        self.geometry = self.calc_geometry()
        self.sly = Polygon(self.geometry)
        self.tsh = trimesh.creation.extrude_polygon(
            self.sly,
            10 + self.gen * 10)
        color_mode(HSB)
        c = color(
            remap(self.y, 0, height, 0 , 255),
             (2 + self.gen) * 25,
             255)
        self.p5s = tsh_to_py5(self.tsh, c, c)
        
        
    def calc_geometry(self):
        vers = []
        n = Element.NUM_ANGLES
        ang = TWO_PI / n
        a_off = ang / 2
        r = self.d / 2
        for i in range(n):
            x = self.x + r * cos(a_off + ang * i + self.ao)
            y = self.y + r * sin(a_off + ang * i + self.ao) 
            vers.append((x, y))
        return vers
     
    def draw(self):
        shape(self.p5s)
#         with begin_closed_shape():
#             vertices(self.geometry)
         #circle(self.x, self.y, self.d)
        
        #stroke_weight(2)
        #line(self.x, self.y, self.px, self.py)
#         fill(0)
#         no_stroke()
#         r = self.d / 2
#         xao = self.x + r * cos(self.ao) 
#         yao = self.y + r * sin(self.ao)
#         element(xao, yao, 10)
#        

    @classmethod
    def d_choice(cls):
        return random_choice((30 / sqrt(2),  30, 30 * sqrt(2)))

    def create_element(self):
        a = random_choice(range(self.NUM_ANGLES)) # 3, 4))
        ang = (TWO_PI / self.NUM_ANGLES) * a
        d = self.d_choice()
        r = self.d / 2 + d / 2
        x = self.x + cos(self.ao + ang) * r   # + self.ao + PI
        y = self.y + sin(self.ao + ang) * r 
        new_element = Element(x, y, d,
                            self.ao + ang + PI,
                            (self.gen + 1) % 10,
                            (self.x, self.y))
        if new_element.good_element():
            self.element_list.append(new_element)
    
    
    def good_element(self):
        if not (50 < self.x < width - 50 and
                50 < self.y < height - 50):
            return False
        for other in self.element_list:
            if self.over_other(other):
                return False
        return True

    def over_other(self, other):    
        distance = dist(self.x, self.y, other.x, other.y)
        return distance < (self.d / 2 + other.d / 2)


    @classmethod
    def add_element(cls):
        if not cls.element_list:
            x, y = width / 2, height / 2
            d = cls.d_choice()
            cls.element_list.append(Element(x, y, d))
        else:
            for c in cls.element_list.copy():
                c.create_element()
        #print(len(elements))

@cache
def tsh_to_py5(tsh, f, s):
    fill(f)
    no_stroke() #stroke(s)
    return convert_shape(tsh)

def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    save(p / stamp / (stamp + '.png')) 
    shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(p / stamp / (stamp + '.png'))
