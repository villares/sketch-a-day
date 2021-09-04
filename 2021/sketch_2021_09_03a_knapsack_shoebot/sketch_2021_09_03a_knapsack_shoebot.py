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

def setup():
    from random import shuffle
    
    elements = [(str(n), n) for n in range(1, 13)]\
    #+ [(str(n) + 'bis', n) for n in range(1, 7)] 

    shuffle(elements)

    W, H = 40, 8
    target = 12
    colorrange(255)
    colormode(HSB)
    stroke(0)
    solutions = knapsack(target, elements)
    print(len(solutions))
#     shuffle(solutions)
#     solutions.sort()
    
    size(target * W * 2, len(solutions) * H)

    for i, s in enumerate(solutions):
        x = 0
        for n, w in s:
            fill(w * 8 if 'bis' in n else w * 32, 255, 255)
#             fill(128 * (w  % 3), w * 24 % 256, 64 * (w % 5))
            # fill(random(255), random(255), random(255))
            rect(x, i * H, w * W, H)
            x += w * W
