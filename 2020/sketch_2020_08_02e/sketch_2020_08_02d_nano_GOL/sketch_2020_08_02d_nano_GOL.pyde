from itertools import chain,product
s=100;b,v,t={(0,0),(-1,0),(-2,0),(0,-1),(-1,-2)},lambda p:((p[0]+i,p[1]+j)for i,j in product((-1,0,1),repeat=2)if i+j*2!=0),lambda p:sum((o in b)for o in v(p))
def draw():global b;clear();[set(x,y,-1)for x,y in b];b={p for p in chain(*map(v,b))if t(p)==3 or(t(p)==2 and p in b)}




# b={(0,0),(-1,0),(-2,0),(0,-1),(-1,-2)}
# clear();stroke(-1)
# background(-1)

# def v(p):return((p[0]+i,p[1]+j)for i, j in((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)))

# from itertools import chain
# b = set([(0, 0), (-1, 0), (-2, 0), (0, -1), (-1, -2)])
# def setup():
#     size(500, 500)
# def draw():
#     global b
#     background(-1)
#     [point(x, y)for x, y in b]
#     n = set()
#     r = b | set(chain(*map(nbs, b)))
#     for p in r:
#         c = sum((nb in b)for nb in nbs(p))
#         if c == 3 or(c == 2 and p in b):
#             n.add(p)
#     b = n
# def nbs(p):
# return((p[0] + i, p[1] + j)for i, j in((-1, -1), (-1, 0), (-1, 1), (0,
# -1), (0, 1), (1, -1), (1, 0), (1, 1)))
