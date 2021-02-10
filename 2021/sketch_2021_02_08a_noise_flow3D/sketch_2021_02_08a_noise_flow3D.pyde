# based on code by solub at
# https://discourse.processing.org/t/discrete-vectors/3942/22

add_library('peasycam')

n_line, n_point = 10, 100
factor = .005
offset, offset2  = 1, 200
da = [HALF_PI, QUARTER_PI, 0,  -QUARTER_PI, - HALF_PI]
# da = [QUARTER_PI, HALF_PI + QUARTER_PI, PI, PI + QUARTER_PI, PI + HALF_PI]

def setup():
    size(600, 600, P3D)
    colorMode(HSB)
    cam = PeasyCam(this, 900)

def draw():
    background(0)    
    paths = [[] for i in range(n_line)]
    offset, offset2 = mouseX / 100.0, mouseY / 100.0
    for y in range(n_line):
        for x in range(n_line):
            py =  map(y, 0, n_line -1, -200, 200)
            px =  map(x, 0, n_line -1, -200, 200)
            pz = 0
            path = []
            stroke(255)
            circle(px, py, 5)
            for p in range(n_point):
                a2 = da[int(round(map(noise(px * factor + offset,
                                    py * factor + offset2,
                                    pz * factor), 0, 1, -1, 5)))]
                a1 = da[int(round(map(noise(px * factor + offset,
                                    py * factor + offset2,
                                    pz * factor), 0, 1, -1, 5)))]
                xd = cos(a2) * sin(a1)
                yd = cos(a2) * cos(a1)
                zd = sin(a2)
                d = PVector(xd, yd, zd).setMag(3)
                px += d.x     
                py += d.y  
                pz += d.z #if (pz + d.z) > 0 else -d.z
                path.append(PVector(px, py, pz,))
            paths.append(path)
    
    noFill()  
    for w, pts in enumerate(paths):
        strokeWeight(2)
        beginShape()
        for x, y, z in pts:
            stroke(z % 255, 255, 255)

            vertex(x, y, z)
        endShape()
    # for w, pts in enumerate(paths):
    #     for i, (x, y, z) in enumerate(pts[:-1]):
    #         nx, ny, nz = pts[i + 1]
    #         line(x, y, z, nx, ny, nz)
