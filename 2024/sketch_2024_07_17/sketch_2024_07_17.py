# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch
from itertools import product

vs = []
faces = []
W = 50

def setup():
    size(600, 600)
    stroke_weight(3)
    stroke_join(ROUND)
    stroke(255)
    no_fill()
    
    vs_dict = {}
    for i, (x, y) in enumerate(product(range(100, 501, W), repeat=2)):
        vs.append((x, y))
        vs_dict[x, y] = i
    for x, y in product(range(100, 500, W), repeat=2):        
        face = []
        for ox, oy in ((0, 0), (1, 0), (1, 1), (0, 1)):
            v = x + ox * W, y + oy * W
            face.append(vs_dict[v])            
        faces.append(face)

    c = Py5Vector(width / 3, height / 3)
    for i, (x, y) in enumerate(vs):        
        v = Py5Vector(x, y)
        ov = (v - c) 
        ov.mag = sqrt(ov.mag) * 3
        vs[i] = tuple(v - ov)
        

def draw():
    background(0)
    for face in faces:
        with begin_shape(QUADS):
            vertices(vs[v] for v in face)
            

def key_pressed():
    save_snapshot_and_code()
    
def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    #save(p / stamp / (stamp + '.png')) 
    #shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(stamp + '.png')