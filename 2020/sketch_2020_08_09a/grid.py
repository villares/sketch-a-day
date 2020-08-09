#*- coding: utf-8 -*-

from __future__ import division

def setup_grid(graph, margin=None):
    margin = margin or width / 40
    cols, rows = dim_grid(len(graph))
    w, h = (width - margin * 2) / cols, (height - margin * 2) / rows
    points = []
    for i in range(cols * rows):
        c = i % cols
        r = i // rows
        x = margin + w * 0.5 + c * w - 14 * (r % 2) + 7
        y = margin + h * 0.5 + r * h - 14 * (c % 2) + 7
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
    b = n // a
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
        a, b = sample(graph.vertices(), 2)  
        new_grid[a], new_grid[b] = new_grid[b], new_grid[a] 
        n = measure_graph_grid(graph, new_grid)
        if m > n:
            t = "{:.1%} at: {} tries of 2 vertex swaps"
            print(t.format((n - m) / m, fail + 1))
            return new_grid
        else:
            fail += 1
    print("no new grid")
    return grid
        
def grid_shuffle(graph, grid):
    from random import sample
    fail = 0
    n = m = measure_graph_grid(graph, grid)
    while m <= n and fail < len(graph) ** 2:
        new_grid= dict(zip(grid.keys(), sample(grid.values(), len(grid))))
        n = measure_graph_grid(graph, new_grid)
        if m > n:
            t = "{:.1%} at: {} tries of complete shuffle"
            print(t.format((n - m) / m, fail + 1))

            return new_grid
        else:
            fail += 1
    print("no new grid")
    return grid

def grid_swap_mult(graph, grid, num=3):
    from random import sample
    fail = 0
    n = m = measure_graph_grid(graph, grid)
    while m <= n and fail < len(graph) ** 2:
        new_grid= dict(grid)
        ks = sample(graph.vertices(), num) 
        vs = [grid[k] for k in sample(ks, num)]
        for k, v in zip(ks, vs):
            new_grid[k] = v          
        n = measure_graph_grid(graph, new_grid)
        if m > n:
            t = "{:.1%} at: {} tries of {}v swaps" 
            print(t.format((n - m) / m, fail + 1, num))
            return new_grid
        else:
            fail += 1
    print("no new grid")
    return grid
