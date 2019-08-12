from random import choice

class Grid():

    def __init__(self, pos, **args):
        self.pos = PVector(*pos)
        self.vel = PVector(choice((-1, 1, .5, -.5)), choice((.25, -.25)))
        self.shapes = Grid.create_shapes((0, 0), **args)
        self.space = args['space']

    def update(self):
        for sh in self.shapes:
            Grid.draw_element(sh, self.pos.x, self.pos.y)
        if dist(mouseX - width / 2, mouseY - width / 2,
                self.pos.x, self.pos.y) < self.space * 5:
            self.pos += self.vel * self.space
        if self.pos.mag() > width / 2: # * height:
            self.vel = self.vel * -1

    @staticmethod
    def create_shapes(pos, dims, space, elem):
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
        sh = args[0]  # shape
        si = args[1]  # size
        c = color(128)
        print ix, iy
        if int(si) % 3 == 0:
            si *= 0.25 + 0.25 * ((ix + iy) % 3)
        elif int(si) % 2 == 0:
            c = color(0, 0, 200)
            si *= 0.5 + 0.5 * ((ix + iy) % 2)
        
        if (ix + iy) % 3 ==0:
            c = color(200, 0, 0)
        elif (ix + iy) % 2 == 0:
            c = color(0, 0, 200)

            

        if args[0] in (RECT, ELLIPSE):
            return (sh, x, y, si, si, c)
        elif sh == TRIANGLE:
            return (TRIANGLE, x, y, x + si, y, x, y + si, c)
        elif sh == TRIANGLES:
            return (TRIANGLE, x, y, x - si, y, x, y - si, c)
        
    @staticmethod    
    def draw_element(el, sx, sy):
        fill(el[-1])
        sh, ex, ey = el[0], el[1], el[2]
        pushMatrix()
        translate(sx, sy)
        if sh == RECT:
            rect(ex, ey, el[3], el[4]) 
        if sh == ELLIPSE:
            rect(ex, ey, el[3], el[4]) 
        if sh == TRIANGLE:
            triangle(ex, ey, el[3], el[4], el[5], el[6]) 
        popMatrix()
