SIN_60 = sqrt(3) * 0.5 # sin(radians(60))

class MockCell:
    state = 0
    gen = 0

class Cell():

    board = dict()
    EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))    
    ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))    
    W = 4
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
        if rnd:
            self.state = 1 if random(20000 / (1 + j)) < 1 else 0 
        else:
            self.state = 0
        self.next_state = self.state
        self.gen = 0
        self.nbs = 0
        
    def display(self):
        # with pushMatrix():
        #     translate(self.x, self.y)
            # noStroke()
            # live_nbs = self.calc_live_nbs()
            # fill((self.i * 2) % 128, (self.j * 2) % 128, 32 + 128 * self.state) 
            # fill(255 * self.state)
            # circle(0, 0, self.W * 2)
            if self.state:
                # strokeWeight(self.H * 2 * self.j / 100)
                # strokeWeight(4.5 - (abs(self.gen / 5.0) % 4))
                if not keyPressed:
                    moving_gen = (self.gen - frameCount / 2) % (3141 * 5)
                    sw = self.W + self.W / 2.0 * sin(moving_gen / 5.0)
                    strokeWeight(sw)
                else:
                    strokeWeight(self.W * 1.5)
                stroke(0, 0, 16 * self.nbs)
                point(self.x, self.y)
    
        
    def calc_live_nbs(self):
        nbs = self.EVN_NBS if self.i % 2 == 0 else self.ODD_NBS
        return sum(self.get_neighbour(i_offset, j_offset).state
                   for i_offset, j_offset in nbs)
   
    def get_neighbour(self, i_offset, j_offset):
        return self.board.get((self.i + i_offset,
                               self.j + j_offset),
                                MockCell())
        
    def get_live_nbs(self):
        nbs = self.EVN_NBS if self.i % 2 == 0 else self.ODD_NBS
        return [self.get_neighbour(i_offset, j_offset)
                for i_offset, j_offset in nbs
                if self.get_neighbour(i_offset, j_offset).state]
        

    def calc_next_state(self):
        self.nbs = nbs = self.calc_live_nbs()
        
        # if nbs == 1:
        #     self.next_state = 1      
        #     lnbs = self.get_live_nbs()
        #     if lnbs:
        #         self.gen = lnbs[0].gen + 1
        # elif nbs > 4:
        #     self.next_state = 0
        # else:
        #    self.next_state = self.state
        #    # self.gen -= 1
        
        # # muito bom com bordas 1 tb
        if nbs == 2 and self.state == 0:
            self.next_state = 1      
            lnbs = self.get_live_nbs()
            if lnbs:
                self.gen = lnbs[-1].gen + 1
        elif nbs > 4:
            self.next_state = 0
        else:
           self.next_state = self.state

        # dia 14
        # if nbs == 1 and self.state == 0:
        #     self.next_state = 1
        #     lnbs = self.get_live_nbs()
        #     if lnbs:
        #         self.gen = lnbs[0].gen + 1
        # elif nbs > 3:
        #     self.next_state = 0
        # else:
        #    self.next_state = self.state

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
    
