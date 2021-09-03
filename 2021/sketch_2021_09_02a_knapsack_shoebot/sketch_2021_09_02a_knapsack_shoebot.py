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

elements = [(n, n) for n in range(1, 27)]

def setup():
    size(520, 990)
    colorrange(255)
    stroke(0)
    solutions = knapsack(26, elements)
    print(len(solutions))
    for i, s in enumerate(solutions):
        x = 0
        for n, w in s:
            fill(128 * (w  % 3), w * 24 % 256, 64 * (w % 5))
            # fill(random(255), random(255), random(255))
            rect(x, i * 6, w * 20, 6)
            x += w * 20
