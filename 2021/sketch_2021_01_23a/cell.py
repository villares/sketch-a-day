def hex_color(s):
    """
    This function allows you to create color from a string with hex notation in Python mode.
    
    On "standard" Processing (Java) we can use hexadecimal color notation #AABBCC
    On Python mode one can use this notation between quotes, as a string in fill(),
    stroke() and background(), but, unfortunately, not with color().
    """
    if s.startswith('#'):
        s = s[1:]
    return color(int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16))

class Cell():
    colors = (hex_color('#264653'),
              hex_color('#2a9d8f'), 
              hex_color('#9c46a'), 
              hex_color('#f4a261'),
              hex_color('#e76f51'))
    
    def __init__(self, index, cell_size):
        self.index = index
        self.state = False
        self.s = cell_size
        self.mouse_down = False
        i, j = index[0], index[1]
        self.pos = PVector(self.s/2 + i * self.s,
                           self.s/2 + j * self.s)
        self.ngbs = []
        NL = ((-1, -1), (+0, -1), (+1, -1),
              (-1, +0),           (+1, +0),
              (-1, +1), (+0, +1), (+1, +1))
        for ni, nj in NL:
            self.ngbs.append(
                    Cell.grid.get((i-ni, j-nj), None))   
        
    def play(self):
        # mouse_on = dist(self.pos.x, self.pos.y,
        #                 mouseX, mouseY) < self.s/2
        hs = self.s / 2
        px, py = self.pos.x, self.pos.y
        mouse_on = (px - hs < mouseX < px + hs and
                    py - hs < mouseY < py + hs)
        if mouse_on and mousePressed:
            self.mouse_down = True
        if self.mouse_down and not mousePressed:
            self.state = (self.state + 1) % len(Cell.colors)
            self.mouse_down = False

        # if mouse_on and mousePressed:
        #     self.mouse_down = True
        # elif self.mouse_down and mouse_on:
        #     self.state = not self.state
        #     self.mouse_down = False
        # else:
        #     self.mouse_down = False
        noStroke()
        fill(Cell.colors[self.state])   
        rect(self.pos.x, self.pos.y,
             self.s,
             self.s
             )
        if mouse_on:
             with pushStyle():
                stroke(255)
                noFill()
                rect(self.pos.x, self.pos.y,
                self.s-1,
                self.s-1
                )
 
        
