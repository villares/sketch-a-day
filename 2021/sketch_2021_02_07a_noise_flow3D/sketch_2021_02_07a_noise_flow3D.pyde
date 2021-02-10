# based on code by solub ar
# https://discourse.processing.org/t/discrete-vectors/3942/22

add_library('peasycam')

n_line, n_point = 20, 300
factor = .04
offset, offset2  = 1, 200
da = [HALF_PI, QUARTER_PI, 0,  -QUARTER_PI, - HALF_PI]

def setup():
    size(600, 600, P3D)
    cam = PeasyCam(this, 1200)

def draw():
    background(255)    
    translate(-400, -200)
    paths = [[] for i in range(n_line)]
    offset, ofsset2 = mouseX / 100.0, mouseY / 100.0
    py = 0
    for y in range(n_line):
        px = 0
        pz = y * 25
        for x in range(n_point):
          n = int(round(map(noise(x * factor + offset, y * factor + offset), 0, 1, -1, 5)))
          d = PVector.fromAngle(da[n]).setMag(3)
          n2 = int(round(map(noise(x * factor + offset2, y * factor + offset2), 0, 1, -1, 5)))
          d2 = PVector.fromAngle(da[n]).setMag(3)
          px += d.x     
          py += d.y  
          pz += d2.y
          if py > 60 or py < 0: py -= d.y
          paths[y].append(PVector(px, pz, py,))
        py = 0
    
    noFill()  
    for w, pts in enumerate(paths):
        strokeWeight((len(paths) - w) / 4.0 + 1)
        beginShape()
        for x, y, z in pts:
            vertex(x, y, z)
        endShape()
    # for w, pts in enumerate(paths):
    #     for i, (x, y, z) in enumerate(pts[:-1]):
    #         nx, ny, nz = pts[i + 1]
    #         line(x, y, z, nx, ny, nz)
