class Cell():
    W = 30
    H = sin(radians(60)) * W

    def __init__(self, i, j):
        self.i = i
        self.j = j

        self.state = int(random(2))
 
        if j % 2 == 0:
            self.x = i * self.W * 3 + self.W
        else:
            self.x = i * self.W * 3 + self.W * 2.5
        self.y = j * self.H + self.H

    def display(self):

        fill(self.state * 255)
        stroke(0)
        fill((self.i * 24) % 256, (self.j * 8) % 256, 128 + 128 * self.state)
        with pushMatrix():
            translate(self.x, self.y)
            with beginShape():
                vertex(-self.W, 0)
                vertex(-self.W / 2, -self.H)
                vertex(self.W / 2, -self.H)
                vertex(self.W, 0)
                vertex(self.W - self.W / 2, self.H)
                vertex(-self.W / 2, self.H)
                vertex(-self.W, 0)
                # circle(self.W, self.H, 10)   
            fill(0)
            textAlign(CENTER, CENTER)
            text("{}, {}".format(self.i, self.j), 0, 0)
            # circle(0, 0, 10)
            noFill()
