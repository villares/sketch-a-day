from itertools import chain, product
s = 100
b, v, t = {(i % s, i / s)for i in range(s * s)if random(2) > 1}, lambda p: ((p[0] + i, p[
    1] + j)for i, j in product(range(-1, 2), repeat=2)if i + j * 2 != 0), lambda p: sum((o in b)for o in v(p))
def draw():
    global b
    clear()
    b = {set(p[0], p[1], -1)or p for p in chain(*map(v, b))
         if t(p) == 3 or(t(p) == 2 and p in b)}

# from itertools import chain,product
# s=100;b,v,t={(i%s,i/s)for i in range(s*s)if random(2)>1},lambda p:((p[0]+i,p[1]+j)for i,j in product(range(-1,2),repeat=2)if i+j*2!=0),lambda p:sum((o in b)for o in v(p))
# def draw():global b;clear();b={set(p[0],p[1],-1)or p for p in chain(*map(v,b))if t(p)==3 or(t(p)==2 and p in b)}


# b={(0,0),(-1,0),(-2,0),(0,-1),(-1,-2)}b
