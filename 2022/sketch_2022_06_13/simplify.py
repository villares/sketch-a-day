from math import dist

def simplify_pts(pts_list, min_dist):
        reference_point = pts_list[0]
        pts_simplified = [reference_point]
        for x, y in pts_list[1:]:
            if dist((x, y), reference_point) >= min_dist: 
                pts_simplified.append((x, y))
                reference_point = x, y
        return pts_simplified
    
def simplify_pts3(pts_list, min_dist):
        previous_point = (float('inf'), float('inf'))
        return [previous_point := (x, y) for x, y in pts_list
                if dist((x, y), previous_point) >= min_dist]
        
def simplified_points(pts_list, min_dist):
        reference_point = pts_list[0]
        yield reference_point
        for x, y in pts_list[1:]:
            if dist((x, y), reference_point) >= min_dist: 
                reference_point = x, y
                yield x, y