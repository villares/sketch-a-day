pa = [(100, 100), (300, 50), (300, 300)]
pb = [(150, 150), (250, 100), (250, 250), (100, 250)]


def setup():
    size(400, 400)
    strokeWeight(5)
    
def draw():
    
    pc = clip_poly(pa, pb)
    
    noFill()
    stroke(200, 0, 0)
    draw_poly(pa)
    stroke(0, 200, 0)
    draw_poly(pb)
    if keyPressed:
        stroke(0, 0, 200)
        draw_poly(pc)

    
            
def draw_poly(poly, closed=True):
    beginShape()
    for p in poly:
        vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()
    

def clip_poly(subjectPolygon, clipPolygon):
   def inside(p):
      return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
 
   def computeIntersection():
      dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
      dp = [ s[0] - e[0], s[1] - e[1] ]
      n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
      n2 = s[0] * e[1] - s[1] * e[0] 
      n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
      return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
 
   outputList = subjectPolygon
   cp1 = clipPolygon[-1]
 
   for clipVertex in clipPolygon:
      cp2 = clipVertex
      inputList = outputList
      outputList = []
      s = inputList[-1]
 
      for subjectVertex in inputList:
         e = subjectVertex
         if inside(e):
            if not inside(s):
               outputList.append(computeIntersection())
            outputList.append(e)
         elif inside(s):
            outputList.append(computeIntersection())
         s = e
      cp1 = cp2
   return(outputList)
