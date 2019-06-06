# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

from polys import poly, poly_filleted, poly_arc_augmented
from b_polys import b_poly_filleted, b_poly_arc_augmented

p_list = [(100, 100), (400, 200), (300, 400), (200, 100), (100, 300)]
rad_list = [80, 40, 20, 50, 10] 

def setup():
    size(500, 500)
    strokeWeight(4)

def draw():
    background(240)
    stroke(255)
    noFill()
    poly(p_list)
    stroke(0, 0, 0)
    noFill()
    if not keyPressed:
        # fill(0, 200, 0, 100) 
        b_poly_arc_augmented(p_list, rad_list)
        # fill(0, 0, 200, 100)
        b_poly_filleted(p_list, rad_list)
    elif key == " ":
        poly_arc_augmented(p_list, rad_list)
        poly_filleted(p_list, rad_list)
             
    if mousePressed:
        p_list[0] = (mouseX, mouseY)
    
