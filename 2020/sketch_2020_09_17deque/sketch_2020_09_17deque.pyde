
import collections as c;s=255;h=c.deque([(0,0)],s)
def setup():size(s*2,s*2);noStroke();colorMode(3)
def draw():background(51);[(fill(i,s,s,s/2),circle(x,y,i/5))for i, (x, y) in enumerate(h)];h.append(h.popleft())
def mouseDragged():h.append((mouseX,mouseY))#つぶやきProcessing

def mouseReleased():print(len(h))
