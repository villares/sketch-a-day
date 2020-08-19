#*- coding: utf-8 -*-

from __future__ import division, print_function
from random import sample, choice


class Grid():

    def __init__(self, graph, cols, rows, mode=0):
        """
        mode 0: heavy center
        mode 1: heavy perifery
        """
        points = []
        for i in range(cols * rows):
            c = i % cols
            r = i // rows
            z = 0
            points.append([r, c, z])
        points = sorted(
            points, key=lambda p: dist(p[0], p[1], width / 2, height / 2))
        if mode == 0:
            v_list = reversed(
                sorted(graph.vertices(), key=graph.vertex_degree))
        elif mode == 1:
            v_list = sorted(graph.vertices(), key=graph.vertex_degree)
        else:
            v_list = graph.vertices()
            print("random mode")
        self.graph = graph
        self.grid = {v: p for v, p in zip(v_list, points)}
        recalculate_sizes_from_v_deg(self.graph, self)

    def __getitem__(self, k):
        return self.grid[k]

    def __setitem__(self, k, v):
        self.grid[k] = v

    def __len__(self):
        return len(self.grid)
    
    def keys(self):
        return self.grid.keys()

    def values(self):
        return self.grid.values()

    def __iter__(self):
        return iter(self.grid)

    def swap(self, num=2):
        grid = self.grid
        graph = self.graph
        fail = 0
        n = m = edge_distances(graph, grid)
        while m <= n and fail < len(graph) ** 2:
            new_grid = dict(grid)
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
                t = "{:.2%} at: {} tries of {}v shuffle/swap" \
                    .format((n - m) / m, fail + 1, num)
                print("\n" + t, end="")
                recalculate_sizes_from_v_deg(graph, new_grid)
                self.grid = new_grid
            else:
                fail += 1
        print(".", end='')
    
    

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


def recalculate_sizes_from_v_deg(graph, grid):
    u = Grid.w / 10
    for k in grid.keys():
        grid[k][2] = u * graph.vertex_degree(k)
    return u

def v_dist(a, b):
    xa, ya, _ = a
    xb, yb, _ = b
    return dist(xa, ya, xb, yb)
