#*- coding: utf-8 -*-

from __future__ import division, print_function

def setup_grid(graph, width, height, margin=None):
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

def edge_distances(graph, grid):
    total = 0
    for edge in graph.edges():
        if len(edge) == 2:
            a, b = edge
            d = PVector.dist(PVector(*grid[a]),
                             PVector(*grid[b]))
            total += d
    return total

def grid_swap(graph, grid, num=2):
    from random import sample
    fail = 0
    n = m = edge_distances(graph, grid)
    while m <= n and fail < len(graph) ** 2:
        new_grid= dict(grid)
        if num == 2:
            a, b = sample(graph.vertices(), 2)  
            new_grid[a], new_grid[b] = new_grid[b], new_grid[a]
        else: 
            ks = sample(graph.vertices(), num) 
            vs = [grid[k] for k in sample(ks, num)]
            for k, v in zip(ks, vs):
                new_grid[k] = v          
        n = edge_distances(graph, new_grid)
        if m > n:
            t = "\n{:.2%} at: {} tries of {}v shuffle/swap" 
            print(t.format((n - m) / m, fail + 1, num), end="")
            return new_grid
        else:
            fail += 1
    print(".", end='')
    return grid
