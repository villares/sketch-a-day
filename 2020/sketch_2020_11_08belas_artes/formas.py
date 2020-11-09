class Quadrado():
    
    def __init__(self, x, y, lado):
        self.x = x
        self.y = y
        self.vx = random(-5, 5)
        self.vy = random(-5, 5)        
        self.lado = lado
        self.cor = color(random(256), random(256), random(256))
        
    def mouse_over(self):
        return (self.x < mouseX < self.x + self.lado
                and self.y < mouseY < self.y + self.lado)
        
    def desenha(self):
        if self.mouse_over():
            fill(255)
        else:
            fill(self.cor)
        rect(self.x, self.y, self.lado, self.lado)
       
    def corra(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > width:
            self.x = 0
        elif self.x < 0 :
            self.x = width
        if self.y > height:
            self.y = 0
        elif self.y < 0:
            self.y = height
            
          
    def mova(self, dx, dy):
        # self.x = self.x + dx
        self.x += dx
        self.y += dy
        self.lado = lado
        self.cor = color(random(256), random(256), random(256))
        
    def mouse_over(self):
        return (self.x < mouseX < self.x + self.lado
                and self.y < mouseY < self.y + self.lado)
        
    def desenha(self):
        if self.mouse_over():
            fill(255)
        else:
            fill(self.cor)
        rect(self.x, self.y, self.lado, self.lado)
        
    def mova(self, dx, dy):
        # self.x = self.x + dx
        self.x += dx
        self.y += dy
