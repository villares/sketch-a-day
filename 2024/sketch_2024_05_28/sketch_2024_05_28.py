def setup():
    size(800, 800)
    
def draw():
    background(240)
    for c in Circle.circle_list:
        c.draw()
        
def key_pressed():
    if key == 'c':
        Circle.circle_list.clear()
    elif key == ' ':
        Circle.add_circle()
        #save_frame(f'{frame_count:0>5}.png')
    elif key == 's':
        save_snapshot_and_code()
    elif key == 'p':
        save_frame('s###.png')
           

class Circle():
    
    NUM_ANGLES = 5  
    circle_list = []
    
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
     
    def draw(self):
        no_stroke() 
        fill(255 - self.d * 3, self.gen % 255, self.d * 3)
        circle(self.x, self.y, self.d)
        stroke(0)
        stroke_weight(2)
        line(self.x, self.y, self.px, self.py)
#         fill(0)
#         no_stroke()
#         r = self.d / 2
#         xao = self.x + r * cos(self.ao) 
#         yao = self.y + r * sin(self.ao)
#         circle(xao, yao, 10)
#        

    @classmethod
    def d_choice(cls):
        return random_choice((30 / sqrt(2),  30, 30 * sqrt(2)))

    def create_circle(self):
        a = random_choice(range(self.NUM_ANGLES)) # 3, 4))
        ang = (TWO_PI / self.NUM_ANGLES) * a
        d = self.d_choice()
        r = self.d / 2 + d / 2
        x = self.x + cos(self.ao + ang) * r   # + self.ao + PI
        y = self.y + sin(self.ao + ang) * r 
        new_circle = Circle(x, y, d,
                            self.ao + ang + PI,
                            self.gen + 10,
                            (self.x, self.y))
        if new_circle.good_circle():
            self.circle_list.append(new_circle)
    
    
    def good_circle(self):
        if not (50 < self.x < width - 50 and
                50 < self.y < height - 50):
            return False
        for other in self.circle_list:
            if self.over_other(other):
                return False
        return True

    def over_other(self, other):    
        distance = dist(self.x, self.y, other.x, other.y)
        return distance < (self.d / 2 + other.d / 2)


    @classmethod
    def add_circle(cls):
        if not cls.circle_list:
            x, y = width / 2, height / 2
            d = cls.d_choice()
            cls.circle_list.append(Circle(x, y, d))
        else:
            for c in cls.circle_list.copy():
                c.create_circle()
        #print(len(circles))


def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    save(p / stamp / (stamp + '.png')) 
    shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(p / stamp / (stamp + '.png'))
