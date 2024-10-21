import py5  # check out https://github.com/py5coding 

from villares.helpers import save_snapshot_and_code

walkers = []
STEP = 10
N = 2

def setup():
    global img
    py5.size(600, 600, py5.P2D)
    img = py5.create_graphics(py5.width, py5.height)
    with img.begin_draw():
        img.stroke_weight(10)
        img.fill(255, 0, 0)
        img.circle(300, 300, 550)
    #py5.image(img, 0, 0)
    #py5.stroke_weight(3)
    start()
    
def start():
    HALF_STEP = STEP // 2
    for _ in range(10):
        walkers.append(Walker(260 + py5.random_int(-N, N) * HALF_STEP,
                              260 + py5.random_int(-N, N) * HALF_STEP,))
    for _ in range(10000):
        for w in walkers.copy():
            #w.draw()
            w.move() 

def draw():
    py5.background(200)
           
    for w in walkers.copy():
            w.history.reverse()
            w.draw(py5.frame_count)
               
    #print(len(walkers))

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        walkers.clear()
        start()
     
class Walker():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = []
        self.history_set = set()
        self.stuck = 0
     
    def move(self):
        if self.stuck < 0:
            return
        elif self.stuck > 2:
            self.stuck = -1
#             walkers.append(Walker(
#                 self.x + py5.random_choice((-STEP * 2, STEP * 2)), 
#                 self.y + py5.random_choice((-STEP * 2, 0, STEP * 2))))
            return    
        xs = self.x + py5.random_choice((-STEP, 0, STEP))
        ys = self.y + py5.random_choice((-STEP, STEP))
#       for other in walkers:
#         #if other != self:
#              if (xs, ys) in other.history_set:
#                  self.stuck += 1
#                  break
#         else:  # !!! when for was not interrupted !!!
        if img.get_pixels(xs, ys) == py5.color(255, 0, 0):
            self.history.append((self.x, self.y))
            self.history_set.add((self.x, self.y))
            self.x = xs
            self.y = ys
        else:
            self.stuck += 1
                       
         
    def draw(self, n):
         for i, (x, y) in enumerate(self.history[1:n], 1):
             if n < len(self.history):
                 px, py = self.history[i - 1]
                 py5.line(px, py, x, y)
             
             
py5.run_sketch(block=False)