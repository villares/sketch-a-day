B_RADIUS = 0

class Button():
    
    button_list = []

    def __init__(self, x, y, w, h, txt, func):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.txt = txt
        self.txt_color = color(0)
        self.pressed = False
        self.func = func
        self.active = False
        self.active_on = color(200, 200, 240)
        self.active_off = color(100)
        self.button_list.append(self)

    def mouse_over(self):
        return (self.x < mouseX < self.x + self.w and
                self.y < mouseY < self.y + self.h)

    def display(self, mp):
        pushStyle()
        mouse_over = self.mouse_over()
        fill(self.calc_fill(mouse_over))
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h, B_RADIUS)
        fill(0)
        textAlign(CENTER, CENTER)
        text(self.txt,
             self.x + self.w / 2,
             self.y + self.h / 2)
        if self.check(mouse_over, mp):
            self.func(self)
        popStyle()
                
    def check(self, mouse_over, mp):
        result = False
        if mouse_over and self.pressed and not mp:
            result = True
        if mouse_over and mp:
            self.pressed = True
        else:
            self.pressed = False
        return result
    
    def toggle(self):
        self.active = not self.active
        
    def exclusive_on(self):    
        for b in self.button_list:
            b.active = False
        self.active = True
   
    def calc_fill(self, mouse_over):
        if self.active and mouse_over:
            return self.darken_color(self.active_on)
        elif self.active:
            return self.active_on
        elif mouse_over:
            return self.darken_color(self.active_off)
        else:
            return self.active_off
     
    @staticmethod       
    def darken_color(c):
        r, g, b = red(c), green(c), blue(c)
        return color(r / 2, g / 2, b / 2)        

    @classmethod
    def display_all(cls, mp):
        for b in cls.button_list:
            b.display(mp)
            
