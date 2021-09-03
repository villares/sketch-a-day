# To run this, install shoebot.net
# thread https://twitter.com/juanplopes/status/1432049284015403011
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

elements = [(i, i) for i in range(1, 27)]

def setup():
    size(520, 660)
    colorrange(255)
    stroke(0)
    solutions = knapsack(26, elements)
    print(len(solutions))
    for i, s in enumerate(solutions):
        x = 0
        for c, w in s:
            fill(i * 9, 255 - i * 9, 255)
            rect(x, i * 4, w * 20, 4)
            x += w * 20
