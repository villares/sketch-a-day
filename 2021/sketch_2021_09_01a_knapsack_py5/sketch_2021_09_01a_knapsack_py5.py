#!/bin/env python
# thread https://twitter.com/juanplopes/status/1432049284015403011
import py5

def knapsack(target_price, items):
    from functools import lru_cache
    
    @lru_cache(maxsize=(target_price + 1) * len(items))
    def inner(price, index):
        if price == 0:
            return [()]   # single valid solution with no items
        if index < 0:
            return []    # no valid solution
        return inner(price, index - 1) + [
            other + (items[index],)
            for other in inner(price - items[index][1], index - 1)
        ]
    return inner(target_price, len(items) - 1)

elements = [
    ('#0000FF', 1),
    ('#000080', 2),
    ('#00FF00', 3),
    ('#00FFFF', 4),
    ('#00FF80', 5),
    ('#008000', 6),
    ('#0080FF', 7),
    ('#008080', 8),
    ('#FF0000', 9),
    ('#FF00FF', 10),
    ('#FF0080', 11),
    ('#FFFF00', 12),
    ('#FFFFFF', 13),
    ('#FFFF80', 14),
    ('#FF8000', 15),
    ('#FF80FF', 16),
    ('#FF8080', 17),
    ('#800000', 18),
    ('#8000FF', 19),
    ('#800080', 20),
    ('#80FF00', 21),
    ('#80FFFF', 22),
    ('#80FF80', 23),
    ('#808000', 24),
    ('#8080FF', 25),
    ('#808080', 26),
]

def setup():
    py5.size(520, 660)
    solutions = knapsack(26, elements)
    print(len(solutions))
    for i, s in enumerate(solutions):
        x = 0
        for c, w in s:
            py5.fill(hex_color(c))
            py5.rect(x, i * 4, w * 20, 4)
            x += w * 20

def hex_color(s):
    if s.startswith('#'): s = s[1:]
    return py5.color(int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16))
    
py5.run_sketch()
