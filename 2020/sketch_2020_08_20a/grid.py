#*- coding: utf-8 -*-

from __future__ import division, print_function
from random import sample, choice


class Grid():

    def __init__(self, graph, cols, rows, mode=0):
        """
        mode 0: heavy center
        mode 1: heavy perifery
        """
        self.cols = cols
        self.rows = rows
        self.graph = graph
        self.grid = self.generate_points(mode)
        self.other_grid = self.generate_points(mode)
        self.recalculate_d()

    def generate_points(self, mode):
        points = []
        for i in range(self.cols * self.rows):
            x = i % self.cols
            y = i // self.rows
            z = 0
            points.append([x, y, z])
        p_dist = lambda p: dist(p[0], p[1], self.cols / 2, self.rows / 2)
        points = sorted(points, key=p_dist)

        if mode == 0:
            v_list = reversed(sorted(self.graph.vertices(),
                                     key=self.graph.vertex_degree))
        elif mode == 1:
            v_list = sorted(self.graph.vertices(),
                            key=self.graph.vertex_degree)
        else:
            v_list = self.graph.vertices()
            print("random mode")

        return {v: p for v, p in zip(v_list, points)}

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
        n = m = self.edge_distances()
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
            n = self.edge_distances(new_grid)
            if m > n:
                t = "{:.2%} at: {} tries of {}v shuffle/swap" \
                    .format((n - m) / m, fail + 1, num)
                print("\n" + t, end="")
                self.grid = new_grid
                self.recalculate_d()
            else:
                fail += 1
        print(".", end='')

    def recalculate_d(self):
        for k in self.graph.vertices():
            d = self.graph.vertex_degree(k)
            self.other_grid[k][2] = d
            self.grid[k][2] = d

    def edge_distances(self, ng=None):
        grid = ng or self.grid
        total = 0
        for edge in self.graph.edges():
            if len(edge) == 2:
                a, b = edge
                xa, ya, _ = grid[a]
                xb, yb, _ = grid[b]
                d = dist(xa, ya, xb, yb)
                total += d
        return total

    def edges(self, t):
        z = zip(self.sorted_edges(self.grid),
                self.sorted_edges(self.other_grid))
        lerped_edges = []
        for za, zb in z:
            lerped_edges.append([lerp(ea, eb, t)
                                 for ea, eb in zip(za, zb)])
        return lerped_edges

    def sorted_edges(self, grid):
        edgs = []
        for e in self.graph.edges():
            if len(e) == 2:
                a, b = tuple(e)
                (xa, ya, za) = grid[a]
                (xb, yb, zb) = grid[b]
                deg = ((za + zb) / 2)  # r / (Grid.w / 10)
                edgs.append((xa, ya, xb, yb, za, zb, deg))
        return sorted(edgs, key=lambda e: e[6])

def dim_grid(n):
    a = int(sqrt(n))
    b = n // a
    if a * b < n:
        b += 1
    print(u'{}: {} × {} ({})'.format(n, a, b, a * b))
    return a, b
