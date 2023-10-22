
"""
Based on https://gist.github.com/Shaptic/6297978
"""
def ccw(tri):
    assert len(tri) == 3, 'must be a triangle'
    a, b, c = tri
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])

def in_poly(p, points):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    inside = False
    if len(points[0]) == 3:
        for i, (xi, yi, _) in enumerate(points):
            xj, yj, _= points[i - 1]  
            if ((yi > p[1]) != (yj > p[1])) and (p[0] < (xj - xi) * (p[1] - yi)
                                                / (yj - yi) + xi):
                inside = not inside  # an intersection was found
        return inside
    else:   
        for i, (xi, yi) in enumerate(points):
            xj, yj = points[i - 1]  
            if ((yi > p[1]) != (yj > p[1])) and (p[0] < (xj - xi) * (p[1] - yi)
                                                / (yj - yi) + xi):
                inside = not inside  # an intersection was found
        return inside
    
def get_ear(shape, ear):
    return (shape[ear - 1], shape[ear], shape[(ear+1) % len(shape)])

def triangulate(original_shape):
    # Use orientation of the top-left-most vertex.
    shape = list(original_shape[:])
    left, starting_index = shape[0], 0
    for i, v in enumerate(shape):
        if v[0] < left[0] or (v[0] == left[0] and v[1] < left[1]):
            left = v
            starting_index = i
    orientation = ccw(get_ear(shape, starting_index))
    triangles = []
    while len(shape) >= 3:
        reflex_vertices = []
        eartip = -1
        for i, v in enumerate(shape):  # For each vertex in the shape
            if eartip >= 0:
                break
            triangle = get_ear(shape, i)  # A triangle from vertex to adjacents.
            # If polygon's orientation doesn't match that of the triangle,
            # it's definitely a reflex and not an ear.
            if ccw(triangle) != orientation:
                reflex_vertices.append(v)
                continue  # Test reflex vertices first.
            for rv in reflex_vertices:
                if rv in triangle:
                    continue  # If we are testing ourselves, skip.
                elif in_poly(rv, triangle):
                    break  # If any reflex vertex in triangle, not ear.
            else:  # No reflexes, so we test all past current vertex.
                for past_current_v in shape[i + 2:]:
                    if past_current_v in triangle:
                        continue
                    elif in_poly(past_current_v, triangle):
                        break  # No vertices in the triangle, we are an ear.
                else:
                    eartip = i
        if eartip == -1:
            break
        triangles.append(get_ear(shape, eartip))
        del shape[eartip] 
    return triangles
