# This version is for pyp5js
# Try it in your browser! https://tinyurl.com/bolas-pcdbr2022
    

bolas = []

def setup():
    createCanvas(600, 600) # pode usar size(600, 600)
    colorMode(HSB, 255)
    noStroke()

def draw():
    #background(0)
    fill(0, random(10, 30))
    rect(0, 0, width, height)
    for b in bolas[:]:   # para cada bola "b" da lista bolas
        b.atualizar()
        if b.tamanho < 1:
            bolas.remove(b)
    print(len(bolas))

class Bola:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random(-3, 3)
        self.vy = random(-3, 3)
        self.tamanho = random(10, 32)
        
    def atualizar(self):
        self.desenhar()
        self.andar()
        self.quicar()    
        self.tamanho = self.tamanho * 0.97
        
    def desenhar(self):
        fill(self.tamanho * 8, 200, 200)
        circle(self.x, self.y, self.tamanho) # x, y, diâmetro
        
    def andar(self):
        # self.x = self.x + self.vx
        self.x += self.vx   # aumenta o self.x
        self.y += self.vy 
        self.vy += 0.1
    
    def quicar(self):
        if self.x > width or self.x < 0:
           self.vx = -self.vx
        if self.y > height or self.y < 0:
            self.vy = -self.vy
        
def mouseDragged(e):
     b = Bola(mouseX, mouseY)
     bolas.append(b)
     
     
        
    