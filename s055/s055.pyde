CEL_SIZE = 25
HALF_CEL = CEL_SIZE / 2
ANG = 0

def setup():
    global ROWS, COLS # filas e colunas
    size(400, 400)
    ROWS, COLS = int(height / CEL_SIZE), int(width / CEL_SIZE)
    noFill()
    strokeWeight(3)
    frameRate(10)
    

def draw():
    global ANG
    background(100)
    for r in range(ROWS):
        for c in range(COLS):
            with pushMatrix():
                translate(HALF_CEL + c * CEL_SIZE,
                          HALF_CEL + r * CEL_SIZE)
                rotate(ANG*c*r/10)    
                stroke(ANG*100 % 255, r * 15 % 255, c * 17 % 255)
                arrow(0, 0, 50 * sin(ANG/5), 50* cos(ANG/5),
                      tail_func=ellipse, tail_size=20 )
                ANG += 0.0001
                
def arrow(x1, y1, x2, y2, shorter=0, head=None,
    tail_func=None, tail_size=None):
    """
    O código para fazer as setas, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    """
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 10, 10)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        strokeCap(ROUND)
        line(0, L - offset, -head / 3, L - offset - head)
        line(0, L - offset, head / 3, L - offset - head)
        strokeCap(SQUARE)
        line(0, offset, 0, L - offset)
        
        if tail_func:
            if not tail_size: tail_size = head
            tail_func(0, 0, tail_size, tail_size)