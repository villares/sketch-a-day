#*- coding: utf-8 -*-


def setup_grid(graph, margin=None):
    margin = margin or width / 40
    cols, rows = dim_grid(len(graph))
    w, h = (width - margin * 2) / cols, (height - margin * 2) / rows
    points = []
    for i in range(cols * rows):
        c = i % cols
        r = i // rows
        x = margin + w * 0.5 + c * w - 20 * (r % 2) + 5 * r
        y = margin + h * 0.5 + r * h - 20 * (c % 2) + 5 * c
        z = 0
        points.append((x, y, z))
    points = sorted(
        points, key=lambda p: dist(p[0], p[1], width / 2, height / 2))
    v_list = reversed(sorted(graph.vertices(), key=graph.vertex_degree))
    # v_list = sorted(graph.vertices(), key=graph.vertex_degree)
    grid = {v: p for v, p in zip(v_list, points)}
    return grid

def dim_grid(n):
    a = int(sqrt(n))
    b = n / a
    if a * b < n:
        b += 1
    print(u'{}: {} × {} ({})'.format(n, a, b, a * b))
    return a, b

def measure_graph_grid(graph, grid):
    metric = 0
    for edge in graph.edges():
        if len(edge) == 2:
            a, b = edge
            d = PVector.dist(PVector(*grid[a]),
                             PVector(*grid[b]))
            metric += d
    return metric

def grid_swap(graph, grid):
    from random import sample
    fail = 0
    n = m = measure_graph_grid(graph, grid)
    while m <= n and fail < len(graph) ** 2:
        new_grid= dict(grid)
        a, b = sample(graph, 2)     
        new_grid[a], new_grid[b] = new_grid[b], new_grid[a] 
        n = measure_graph_grid(graph, new_grid)
        if m > n:
            print("at: {}".format(fail))
            return new_grid
        else:
            fail += 1
    print("no new grid")
    return grid
        
