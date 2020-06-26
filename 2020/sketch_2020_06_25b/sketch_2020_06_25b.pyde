"""
Ported from code by Vamoss
https://vamoss.com.br https://twitter.com/vamoss https://github.com/vamoss
Original code link:
https://www.openprocessing.org/sketch/880000
"""

#as suggested by @bbfontes
#https://twitter.com/bbfontes/status/1252988672024154112

draggable = []

def setup():
    size(800, 600)
    size_ = min(width, height)
    initDrag((width - size_)/2, (height - size_)/2, size_, size_)


def draw():
    background(0)
    
    beginShape()
    for i in range(len(draggable)+3):
        curveVertex(draggable[i%len(draggable)].x, draggable[i%len(draggable)].y)
    endShape()
    
    # drawDrag()


def initDrag(x, y, w, h):
    border = 80
    draggable.append(PVector(x + border, y + border))#TOP LEFT
    draggable.append(PVector(x + w - border, y + border))#TOP RIGHT
    draggable.append(PVector(x + w - border, y + h - border))#BOTTOM LEFT
    draggable.append(PVector(x + border, y + h - border))#BOTTOM RIGHT

 
def mousePressed():
    # if not dragMousePressed():
        # simple solution
        # just create a point at the end of polygon
        #draggable.append(PVector(mouseX, mouseY))

        # complex solution
        # look for the closest average point between two points
        closest = 99999
        closestIndex = -1
        for i in range(len(draggable)):
            nextIndex = (i+1)%len(draggable)

            averageX = draggable[i].x + (draggable[nextIndex].x - draggable[i].x) / 2
            averageY = draggable[i].y + (draggable[nextIndex].y - draggable[i].y) / 2

            distX = averageX - mouseX
            distY = averageY - mouseY
            distance = distX * distX + distY * distY
            if(distance < closest):
                closest = distance
                closestIndex = i
            
        
        if(closestIndex>=0):
            draggable.append(PVector(mouseX, mouseY), closestIndex+1)
        
    

 
# def mouseReleased():
#     dragMouseReleased()

 
# def mouseDragged():
#     dragMouseDragged()
