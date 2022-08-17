# https://stackoverflow.com/a/13851341/19771
size(900, 900)
scale(60)
stroke_weight(0.01)
rectangles = (
    [[1.2, 2.2], [3, 1]], [[1, 4], [2, 2]], [[1, 6], [2, 4]], [[2, 6], [3, 5]],
    [[3, 8], [4, 4]], [[2, 8], [3, 7]], [[3, 10], [5, 8]], [[3, 4], [9, 3]],
    [[4, 5], [7, 4]], [[6, 8], [7, 5]], [[6, 9], [8, 8]], [[8, 9], [10, 6]],
    [[9, 6], [10, 3]]
    )
rect_mode(CORNERS)
for a, b in rectangles:
    rect(*a, *b)

pts = set()
for (x1, y1), (x2, y2) in rectangles:
    for pt in ((x1, y1), (x2, y1), (x2, y2), (x1, y2)):
        if pt in pts: # Shared vertice, remove it.
            pts.remove(pt)
        else:
            pts.add(pt)
pts = list(pts)

sort_x = sorted(pts)
sort_y = sorted(pts, key=lambda p: (p[1], p[0]))

with push():
    stroke_weight(0.05)
    points(pts)
    for i, p in enumerate(sort_x):
        fill(0, 100, 0)
        push()
        translate(*p)
        scale(0.1)
        text_size(2)
        text(i, 1, 1)
        pop()
edges_h = {}
edges_v = {}

i = 0
while i < len(pts):
    curr_y = sort_y[i][1]
    while i < len(pts) and sort_y[i][1] == curr_y: 
        edges_h[sort_y[i]] = sort_y[i + 1]
        edges_h[sort_y[i + 1]] = sort_y[i]
        i += 2
i = 0
while i < len(pts):
    curr_x = sort_x[i][0]
    while i < len(pts) and sort_x[i][0] == curr_x:
        edges_v[sort_x[i]] = sort_x[i + 1]
        edges_v[sort_x[i + 1]] = sort_x[i]
        i += 2

# Get all the polygons.
polygons = []
while edges_h:
    # We can start with any point.
    polygon = [(edges_h.popitem()[0], 0)]
    while True:
        curr, e = polygon[-1]
        if e == 0:
            next_v = edges_v.pop(curr)
            polygon.append((next_v, 1))
        else:
            next_v = edges_h.pop(curr)
            polygon.append((next_v, 0))
        if polygon[-1] == polygon[0]:
            # Closed polygon
            polygon.pop()
            break
    # Remove implementation-markers from the polygon.
    poly = [pt for pt, _ in polygon]
    for v in poly:
        if v in edges_h: edges_h.pop(v)
        if v in edges_v: edges_v.pop(v)

    polygons.append(poly)
    translate(0.1, 0.1)    
    fill(100, 0, 0, 100)
    print(poly)
    with begin_closed_shape():
        vertices(poly)
