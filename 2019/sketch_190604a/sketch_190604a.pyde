# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

from polys import poly, poly_filleted, poly_arc_augmented
from b_polys import b_poly_filleted, b_poly_arc_augmented
from c_polys import c_poly_filleted, c_poly_arc_augmented

pts_list = [(100, 300), (400, 200), (300, 400),(100, 300), (100, 100)]
rad_list = [40, 80, 20, 50, 20] 

def setup():
    size(500, 500)
    # noFill()
    strokeWeight(4)

def draw():
    background(240)
    stroke(255)
    noFill()
    poly(pts_list)
    stroke(0, 0, 0)
    noFill()
    if not keyPressed or key == "b":
        fill(0, 200, 0, 100) 
        b_poly_arc_augmented(pts_list, rad_list)
        fill(0, 0, 200, 100)
        b_poly_filleted(pts_list, rad_list)
    elif key == " ":
        poly_arc_augmented(pts_list, rad_list)
        poly_filleted(pts_list, rad_list)
    elif key == "c":
        fill(0, 200, 0, 100) 
        c_poly_arc_augmented(pts_list, rad_list)
        fill(0, 0, 200, 100)
        c_poly_filleted(pts_list, rad_list)             
    if mousePressed:
        pts_list[0] = (mouseX, mouseY)
    
