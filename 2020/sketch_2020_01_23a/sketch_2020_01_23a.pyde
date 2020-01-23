# Sigle tweet variation on 22a

# add_library('VideoExport') 
def setup():size(800,800)
 # global videoExport
 # videoExport = VideoExport(this)
 # videoExport.startMovie()
 # videoExport.setFrameRate(30)
 # frameRate(30)
 # noiseSeed(20200122)
def draw():
 clear();m=360;translate(m,m);v=.002;s=sin
 for n in range(m,1,-9):
  f=radians(frameCount+n/3);fill(255,16);beginShape()
  for i in range(m):
   a=i*TAU/m;r=n*2*noise(m*s(f+a)*v+m,m*s(f-a)*v+m,m*s(f)*v);vertex(r*s(a),r*cos(a))
  endShape(2)
  
 # videoExport.saveFrame()
 if frameCount == 360:
  # videoExport.endMovie()
  exit()
