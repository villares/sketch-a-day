#*- coding: utf-8 -*-

from __future__ import division, print_function
from random import sample, choice


class Grid():

    def __init__(self, graph, cols, rows):
        self.cols = cols
        self.rows = rows
        self.graph = graph
        self.grid = self.generate_points()

    def generate_points(self):
        points = []
        for i in range(self.cols * self.rows):
            x = i % self.cols
            y = i // self.rows
            points.append([x, y])
        p_dist = lambda p: dist(p[0], p[1], self.cols / 2, self.rows / 2)
        points = sorted(points) #, key=p_dist)
        v_list = sorted(self.graph.vertices())
        return {v: p for v, p in zip(v_list, points)}

    def __getitem__(self, k):
        return self.grid[k]

    def __setitem__(self, k, v):
        if k not in self.graph:
            self.graph.add_vertex(k)
        self.grid[k] = v

    def __len__(self):
        return len(self.grid)

    def remove_vertex(self, v):
        if v in self.graph:
            self.graph.remove_vertex(v)
            del self.grid[v]
            return True
        else:
            return False


    def keys(self):
        return self.grid.keys()

    def values(self):
        return self.grid.values()

    def __iter__(self):
        return iter(self.grid)


    def edge_distances(self, ng=None):
        grid = ng or self.grid
        total = 0
        for edge in self.graph.edges():
            if len(edge) == 2:
                a, b = edge
                xa, ya = grid[a]
                xb, yb = grid[b]
                d = dist(xa, ya, xb, yb)
                total += d
        return total


    def edge_coords(self):
        coords = []
        for e in self.graph.edges():
            if len(e) == 2:
                a, b = tuple(e)
                xa, ya = self.grid[a]
                xb, yb  = self.grid[b]
                da = self.graph.vertex_degree(a)
                db = self.graph.vertex_degree(b)            
                coords.append((xa, ya, xb, yb, da, db))
        return coords
    
def dim_grid(n):
    a = int(sqrt(n))
    b = n // a
    if a * b < n:
        b += 1
    print(u'{}: {} × {} ({})'.format(n, a, b, a * b))
    return a, b
