from random import choice

class Grid():
    
    def __init__(self, pos, **args):
        self.pos = PVector(*pos)
        self.vel = PVector(choice((-1, 1, .5, -.5)), choice((.25, -.25)))
        self.shapes = Grid.shapes((0, 0), **args)
        self.space = args['space']
        
    def update(self):
        for sh in self.shapes:
            shape(sh, self.pos.x, self.pos.y)
       
        self.pos += self.vel * self.space
        if self.pos.magSq() > width * height:
            self.pos = self.pos * -1
         
    @staticmethod                                           
    def shapes(pos, dims, space, elem):
        gx, gy = pos
        col_num, row_num = dims
        result = []
        half_w = col_num * space / 2.
        half_h = row_num * space / 2.
        for ix in range(col_num):
            x = gx + ix * space + space / 2. - half_w
            for iy in range(row_num):
                y = gy + iy * space + space / 2. - half_h
                noFill()
                result.append(Grid.create_element(x, y, ix, iy, *elem))
        return result

    
    @staticmethod                                           
    def create_element(x, y, ix, iy, *args):
        sh = args[0] # shape
        si = args[1] # size
        if int(si) % 3 == 0:
            si *= 0.25 + 0.25 * ((ix + iy) % 3)
        elif int(si) % 2 == 0:
            si *= 0.5 + 0.5 * ((ix + iy) % 2)            
        
        if args[0] in (RECT, ELLIPSE):
            return createShape(sh, x, y, si, si)
        elif sh == TRIANGLE:
            return createShape(TRIANGLE, x, y, x + si, y, x, y + si)
        elif sh == TRIANGLES:
            return createShape(TRIANGLE, x, y, x - si, y, x, y - si)
