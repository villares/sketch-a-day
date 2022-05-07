import Part
from FreeCAD import Vector
from random import choice

Gui.runCommand('Std_SelectAll',0)
Gui.runCommand('Std_Delete')

dims = (40, 60, 80)
wall_thickness = 10
boxes, holes, frames = [], [], []
rotations = ((Vector(0, 0, 0), Vector(0, 1, 0), 90),
             (Vector(0, 0, 0), Vector(1, 0, 0), 90),   
             (Vector(0, 0, 0), Vector(0, 1, 0), 45),   
             (Vector(0, 0, 0), Vector(1, 0, 0), 45),   
             (Vector(0, 0, 0), Vector(0, 0, 1), 0),  # no Rotation!    
             (Vector(0, 0, 0), Vector(0, 0, 1), 0),  # no Rotation!
            ) 

def frame(w, h, d):
    box = Part.makeBox(w, h, d)
    hole = Part.makeBox(w - wall_thickness, h - wall_thickness, d)
    hole.translate(Vector(wall_thickness / 2, wall_thickness / 2, 0))
    tube = box.cut(hole)    
    hole2 = Part.makeBox(w, h - wall_thickness, d - wall_thickness)
    hole2.translate(Vector(0, wall_thickness / 2, wall_thickness / 2))
    almost = tube.cut(hole2)
    hole3 = Part.makeBox(w - wall_thickness, h, d - wall_thickness)
    hole3.translate(Vector(wall_thickness / 2, 0, wall_thickness / 2))
    return almost.cut(hole3).translated(Vector(-w / 2, -h / 2, -d / 2))      


for _ in range(5):
    w, h, d = choice(dims), choice(dims), choice(dims) # width, height, depth
    rot = choice(rotations)    

    box = Part.makeBox(w, h, d).translated(Vector(-w / 2, -h / 2, -d / 2))  
    boxes.append(box.rotated(*rot))

    frames.append(frame(w, h, d).rotated(*rot))
    
    hole = Part.makeBox(w - wall_thickness, h - wall_thickness, d)
    hole.translate(Vector(-w / 2, -h / 2, -d / 2))
    hole.translate(Vector(wall_thickness / 2, wall_thickness / 2))
    holes.append(hole.rotated(*rot) )

union_holes = holes.pop()   # Could try reduce...
for h in holes:
    union_holes = union_holes.fuse(h)

union_boxes = frames.pop()
for f in frames:
    union_boxes = union_boxes.fuse(f)
result = union_boxes.cut(union_holes)

Part.show(union_holes)  # manually changes to translucent
Part.show(result)

