from itertools import chain
s=50;b={(i%s,i/s)for i in range(s*s)if random(10)<5}
v=lambda p:((p[0]+i,p[1]+j)for i,j in((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)))
t=lambda p:sum((o in b)for o in v(p))
def draw():global b;scale(2);background(-1);[point(x,y)for x,y in b];r=set(chain(*map(v,b)));b={p for p in r if t(p)==3 or(t(p)==2 and p in b)}


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
#     return((p[0] + i, p[1] + j)for i, j in((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)))
