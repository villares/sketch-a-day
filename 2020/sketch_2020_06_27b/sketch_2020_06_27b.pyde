#  (t+abs((x+y-t)^(x-y+t))**3)%1023<109
n = 16

t = 0
def setup():
    global s
    noStroke()
    frameRate(2)
    size(640, 640)
    textFont(loadFont('UbuntuMono-Bold-48.vlw'))
    
def draw():
    s = width / n
    textAlign(CENTER, CENTER)
    textSize(14)
    colorMode(HSB)
    a = frameCount
    b = frameCount * 2
    c = a ^ b 
    vv = [a, b, c]
    for x in range (n):
        for y in range(3):
          v = vv[y]
          bv = left_padded_bin(v, n)  
          if bv[x] == '0':
              fill(0)
          else:
              fill(255)
          rect(x * s, y * s, s, s)
          
          
def left_padded_bin(v, n):
    bv = bin(v)[2:]
    if len(bv) < n:
        bv = '0'*(n-len(bv)) + bv
    return bv
