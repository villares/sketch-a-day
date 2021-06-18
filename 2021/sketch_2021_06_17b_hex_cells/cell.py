class MockCell:
    state = 0

class Cell():

    board = dict()
    EVEN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))    
    ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1))    
    W = 15
    H = sin(radians(60)) * W
    last_clicked = None
    
    def __init__(self, i, j, rnd=False):
        self.board[(i, j)] = self
        self.i = i
        self.j = j
        self.state = int(random(2)) if rnd else 0
        self.x = i * self.W * 1.5 + self.W
        if i % 2 == 0:
            self.y = j * self.H * 2 + self.H
        else:
            self.y = j * self.H * 2 + self.H * 2

    def display(self):
        with pushMatrix():
            translate(self.x, self.y)
            noStroke()
            live_nbs = self.calc_live_nbs()
            fill(live_nbs * 32)
            self.hexagon(self.W, self.H)
            
            fill((self.i * 4) % 256, (self.j * 4) % 256, 128 + 128 * self.state)
            self.hexagon(self.W / 3, self.H / 3)
            fill(255)
            textAlign(CENTER, CENTER)
            # text("{}".format(live_nbs), 0, 0)
            # text("{}, {}".format(self.i, self.j), 0, 0)
            # circle(0, 0, 10)
            noFill()
        
    def calc_live_nbs(self):
        nbs = self.EVEN_NBS if self.i % 2 == 0 else self.ODD_NBS
        return sum(self.get_neighbour(i_offset, j_offset).state
                   for i_offset, j_offset in nbs)
   
    def get_neighbour(self, i_offset, j_offset):
        return self.board.get((self.i + i_offset, self.j + j_offset),
                              MockCell())

    def check_click(self):
        if self.mouse_over() and self.__class__.last_clicked != self:
            self.state ^= 1
            self.__class__.last_clicked = self
                
    def  mouse_over(self):
        return dist(self.x, self.y, mouseX, mouseY) < self.H    
                                                                          
    @staticmethod
    def hexagon(w, h):
        # h expected to be sin(radians(60)) * w 
        with beginShape():
                vertex(-w, 0)
                vertex(-w / 2, -h)
                vertex(w / 2, -h)
                vertex(w, 0)
                vertex(w - w / 2, h)
                vertex(-w / 2, h)
                vertex(-w, 0)
    
