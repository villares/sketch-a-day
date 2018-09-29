i, table = 0, []

def setup():
    global printable_ascii
    size(100, 200)
    background(255)
    fill(0)
    noSmooth() # turns off antialiasing
    textAlign(CENTER, CENTER)
    printable_ascii = list(range(32, 127))# + list(range(161, 256))
    f = createFont("SourceCodePro-Bold", 24)
    textFont(f)
    
def draw():
    global i, gliphs    
    if i < len(printable_ascii):
        gliph = chr(printable_ascii[i])
        background(255)
        textSize(100)
        text(gliph, width/2, height/2)
        b, w, o = count_pixels()
        print("{}({}) black: {} white: {} other: {}".format(ord(gliph), gliph, b, w, o))
        table.append((gliph, b, w, o))
        i += 1
    elif i == len(printable_ascii):
        table.sort(key=lambda s: s[1])
        gliphs = "".join([gliph for gliph, b, w, o in table])
        print(gliphs)
        i += 1        
    else:
        present()

def count_pixels():
    black, white, other = 0, 0, 0
    for x in range(width):
        for y in range(height):
            pix = get(x, y)
            if pix == color(0):
                black += 1
            elif pix == color(255):
                white += 1
            else:
                other += 1
    return black, white, other
            
def present():
    background(255)
    i = int(map(mouseY, 0, height-1, 0, len(gliphs)-1))
    gliph, b, w, o = table[i]
    textSize(8)
    text("{} B:{}\nW:{}:\nO:{}".format(ord(gliph), b, w, o), width/2, 20)
    textSize(100)
    text(gliph, width/2, height/2)

# .`:,';-_*"~!i|/\rI^)+(l?{><=}tc[]sjvJL7f1xzTyYF5e23onuaV4$SkC#EPhZX96U0pqKdbGA%gH8wRBmODN&Q@WM SourceCodePro Bold
# .`:,';_-*"~!i|/\rI^+()l?}{<>=tc[]sjvJL7f1xzTyYF5e23nuoaV4$SkC#EPhZX906UKpqdbGA%gH8wR@BmODN&QWM Default    
# .`-',:_;~"!Ii\/r^><+=l|1?t()c*L}z{jvfJ7sx[]TYFnuCyo2kaeS54V3XhPEZUAK690bdqHp#$R8GDOwmNgBQ%&MW@ Open Sans
# `'.^"~,_-:\/;|*!+)(=<>71?il[]{}rtIjvJuznc3LYf4s%o2a&xVC5Uk9hywFZeT60PS$OD@gbKAXdm8GEHRq#NpWBMQ Courier
