SIN_60 = sqrt(3) * 0.5 # sin(radians(60))

class MockCell:
    state = 0

class Cell():

    board = dict()
    EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))    
    ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))    
    W = 10
    H = SIN_60 * W
    last_clicked = None
    
    def __init__(self, i, j, rnd=False):
        self.board[(i, j)] = self
        self.i = i
        self.j = j
        self.x = i * self.W * 1.5 + self.W
        if i % 2 == 0:
            self.y = j * self.H * 2 + self.H
        else:
            self.y = j * self.H * 2 + self.H * 2
        self.state = int(random(2)) if rnd else 0
        self.next_state = self.state
        
    def display(self):
        with pushMatrix():
            translate(self.x, self.y)
            noStroke()
            live_nbs = self.calc_live_nbs()
            # fill((self.i * 2) % 128, (self.j * 2) % 128, 32 + 128 * self.state) 
            fill(255 * self.state)
            self.hexagon(self.W)
            
            fill(16 + live_nbs * 32)
            circle(0, 0, self.W * 0.5)
            fill(0)
            textSize(14)
            textAlign(CENTER, CENTER)
            # text("{}".format(live_nbs), -1, -1)
            # text("{}, {}".format(self.i, self.j), 0, 0)
            # circle(0, 0, 10)
            noFill()
        
    def calc_live_nbs(self):
        nbs = self.EVN_NBS if self.i % 2 == 0 else self.ODD_NBS
        return sum(self.get_neighbour(i_offset, j_offset).state
                   for i_offset, j_offset in nbs)
   
    def get_neighbour(self, i_offset, j_offset):
        return self.board.get((self.i + i_offset,
                               self.j + j_offset),
                                MockCell())

    def calc_next_state(self):
        nbs = self.calc_live_nbs()
        if nbs == 1:
            self.next_state = 1
        # elif nbs > 4:
        #     self.next_state = 0
        else:
            self.next_state = self.state

    def check_click(self):
        if (self.mouse_over() and
            self.__class__.last_clicked != self):
                self.state ^= 1
                self.__class__.last_clicked = self
                
    def mouse_over(self):
        return dist(self.x, self.y, mouseX, mouseY) < self.H    
                                                                          
    @staticmethod
    def hexagon(w):
        h = SIN_60 * w
        with beginShape():
                vertex(-w, 0)
                vertex(-w / 2, -h)
                vertex(w / 2, -h)
                vertex(w, 0)
                vertex(w - w / 2, h)
                vertex(-w / 2, h)
                vertex(-w, 0)
    
