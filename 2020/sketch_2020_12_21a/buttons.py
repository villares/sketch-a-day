B_RADIUS = 0

class Button():
    
    button_list = []

    def __init__(self, x, y, w, h, txt, func):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.t = txt
        self.pressed = False
        self.func = func
        self.button_list.append(self)

    def mouse_over(self):
        return (self.x < mouseX < self.x + self.w and
                self.y < mouseY < self.y + self.h)

    def display(self, mp):
        mouse_over = self.mouse_over()
        if mouse_over:
            fill(140)
        else:
            fill(240)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h, B_RADIUS)
        fill(0)
        textAlign(CENTER, CENTER)
        text(self.t,
             self.x + self.w / 2,
             self.y + self.h / 2)
        
        if self.check(mouse_over, mp):
            self.func()
        
    def check(self, mouse_over, mp):
        if mouse_over and self.pressed and not mp:
            self.pressed = False
            return True

        if mouse_over and mp:
            self.pressed = True
        else:
            self.pressed = False

        return False
    
    @classmethod
    def display_all(cls, mp):
        for b in cls.button_list:
            b.display(mp)
