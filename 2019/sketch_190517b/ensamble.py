from random import choice
from polys import poly, poly_arc_augmented


class Ensamble:
    

    def __init__(self, points, radius):
        self.p_list = points
        self.rad_list = radius
        
    def __eq__(self, other):
        return self.p_list == other.p_list

    def plot(self):
        rad_list = self.rad_list
        noFill()
        strokeWeight(10)
        for _ in range(len(rad_list)):
            poly_arc_augmented(self.p_list, rad_list)
            rad_list[:] = [rad_list[-1]] + rad_list[:-1]
 
