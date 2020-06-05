# D'aprés @ntsutae つぶやきProcessing 
# https://twitter.com/ntsutae/status/1268432505356513280?s=20

t = 0
w = 400  
a, b, c = 2, 1023, 512
def setup():
    size(w, w)
    strokeWeight(1.5)
    noSmooth()
def draw():
    global t
    t += 1
    # scale(2)
    background(-1)
    for y in range(400):
        for x in range(400):
            (t + abs((x + y - t) ^ (x - y + t)
                     ) ** a) % b < c and point(x, y)
def keyPressed():
    global a, b, c
    print(a, b, c)
    if key == 'a':
        a +=1
    if key == 'z' and a > 1:
        a -=1
    if key == 's':
        b +=1
    if key == 'x' and b > 1:
        b -=1
    if key == 'd':
        c +=1
    if key == 'c' and c > 1:
        c -=1

# First ported from @ntsutae code for a single tweet                
# t=0;w=720#つぶやきProcessing d'aprés @ntsutae
# def setup():size(w,w)
# def draw():
#  global t;t+=1;scale(3);background(-1)
#  for y in range(240):
#   for x in range(240):
#    (t+abs((x+y-t)^(x-y+t))**3)%1023<109 and point(x,y)
