  
from itertools import product
from random import sample
from helpers import line_intersect, is_poly_self_intersecting

def setup():
    global grid
    size(650, 650)
    strokeJoin(ROUND)
    noLoop()
    grid = list(product(range(125, width - 99, 200), repeat=2))
    
def keyPressed():
    redraw()

def draw():
    background(230)   
    strokeWeight(10)
    stroke(255)
    for x, y in grid:
        point(x, y) 
    path = arrow = None
    while not path or not is_poly_self_intersecting(arrow):
        path = sample(grid, 6)
        arrow = offset_path(path, 40)
    # noStroke()
    fill(100)
    stroke(230)
    beginShape()
    for x, y in arrow:
        vertex(x, y) 
    endShape(CLOSE)
    
def offset_path(path, offset):
    a = calc_offset(path, offset, True)
    # a = remove_loops(a)
    b = calc_offset(path[::-1], offset)
    # b = remove_loops(b)
    return a + b
  
def remove_loops(path):
    path = list(path)
    crossings = []
    for i, (pa, pb) in enumerate(zip(path, path[1:]), 2):
        for pc, pd in zip(path[2:], path[3:]):
            if pb == pc or pd == pa or pa == pc or pb == pd:
                continue
            ip = line_intersect(pa, pb, pc, pd)
            if ip:
                crossings.append((i, ip))
    if len(crossings) >= 2:
        (ia, ip), (ib, _) = crossings[-2:]
        path = path[:ia - 1] + [ip] + path[ib - 1:] 
        #crossings = crossings[:-2]        
    # for i, (x, y) in crossings:
    #     print(i, x, y)
    #     circle(x, y, 20 - i * 2)
    return tuple(path)
                                  
                                                                                                                                                                                                
def calc_offset(path, offset, inside=False):
    first_seg = path[:2]  # first segment
    first_angle = PI + seg_angle(first_seg) if inside else seg_angle(first_seg)
    first_point = point_offset(first_seg[0], offset, first_angle)
    first_offset = seg_offset(first_seg, offset)
    # draw_seg(first_offset)
    new_path = [first_point, first_offset[0]]
    for p in path[2:]:
        second_seg = (first_seg[1], p)
        second_offset = seg_offset(second_seg, offset)
        # if dist(first_seg[1][0], first_seg[1][1], p[0], p[1]) < offset:
        #     first_seg = second_seg
        #     first_offset = second_offset
        #     continue
        half_angle = (seg_angle(first_seg) + seg_angle(second_seg)) / 2 - HALF_PI
        ip = line_intersect(first_offset, second_offset, in_segment=True)
        if not ip:
            new_path.append(first_offset[1])
            new_path.append(second_offset[0])
        else:
            new_path.append(ip)
        # prepare for next loop    
        first_seg = second_seg
        first_offset = second_offset
    new_path.append(second_offset[1]) # final offset point
    return new_path 
   
def draw_seg(seg):
    (xa, ya), (xb, yb) = seg
    line(xa, ya, xb, yb)
        
def seg_offset(seg, offset):
    angle = seg_angle(seg) + HALF_PI  # angle perpendiculat to seg
    return point_offset(seg[0], offset, angle), point_offset(seg[1], offset, angle)    
    
def point_offset(p, offset, angle):
    return p[0] + offset * cos(angle), p[1] + offset * sin(angle)    
                
def seg_angle(seg):
    (xa, ya), (xb, yb) = seg
    return atan2(yb - ya, xb - xa) + PI
 
