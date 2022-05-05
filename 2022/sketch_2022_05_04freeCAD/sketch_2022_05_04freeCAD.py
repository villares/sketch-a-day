import Part
from FreeCAD import Vector
from random import choice

Gui.runCommand('Std_SelectAll',0)
Gui.runCommand('Std_Delete')

dims = (40, 60, 80, 100)
wall_thickness = 10
boxes, holes = [], []
rotations = ((Vector(0, 0, 0), Vector(0, 1, 0), 90),
             (Vector(0, 0, 0), Vector(1, 0, 0), 90),   
             (Vector(0, 0, 0), Vector(0, 0, 1), 0),  # no Rotation!
            ) 
for _ in range(10):
    w, h, d = choice(dims), choice(dims), choice(dims) # width, height, depth
    rot = choice(rotations)    

    box = Part.makeBox(w, h, d)
    box.translate(Vector(-w / 2, -h / 2, -d / 2))    
    box.rotate(*rot)
    boxes.append(box)

    hole = Part.makeBox(w - wall_thickness, h - wall_thickness, d)
    hole.translate(Vector(-w / 2, -h / 2, -d / 2))
    hole.translate(Vector(wall_thickness / 2, wall_thickness / 2))
    hole.rotate(*rot)  # same as box/boxes    
    holes.append(hole)

union_holes = holes.pop()   # Could try reduce...
for f in holes:
    union_holes = union_holes.fuse(f)
union_boxes = boxes.pop()
for p in boxes:
    union_boxes = union_boxes.fuse(p)

result = union_boxes.cut(union_holes)
Part.show(result)


