# Sigle tweet variation on 22a

# add_library('VideoExport') 
# def setup():size(720,720)
 # global videoExport
 # videoExport = VideoExport(this)
 # videoExport.startMovie()
 # videoExport.setFrameRate(30)
 # frameRate(30)
 # noiseSeed(20200122)
def setup():size(720,720)
def draw():
 clear();noStroke();m=360;v=.002;s=sin
 for n in range(m*2,1,-9):
  f=radians(frameCount-n/3);fill(255,5);beginShape()
  for i in range(m):
   a=i*TAU/m;r=n*noise(m*s(f-a)*v+m,m*s(f+a)*v+m,m*s(f)*v);vertex(r*s(a)+m,r*cos(a)+m)
  endShape(2)
  
 # videoExport.saveFrame()
 if frameCount == 360:
  # videoExport.endMovie()
  exit()
