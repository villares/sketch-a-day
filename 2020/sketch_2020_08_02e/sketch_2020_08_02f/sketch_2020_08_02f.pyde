import itertools as t;s,m=100,-1;b,v,c={(1,1),(0,1),(m,1),(1,0),(0,m)},lambda p:((p[0]+i,p[1]+j)for i,j in t.product((m,0,1),(m,0,1))if i+j*2),"sum((o in b)for o in v(p))==%s"
def draw():global b;clear();b={set(p[0],p[1],m)or p for p in t.chain(*map(v,b))if eval(c%3)^(eval(c%2)and p in b)}



# -21
# import itertools as t;s=100;b,v,c={(i%s,i/s)for i in range(s*s)if random(2)>1},lambda p:((p[0]+i,p[1]+j)for i,j in t.product((-1,0,1),(-1,0,1))if i+j*2),lambda p:sum((o in b)for o in v(p))
# def draw():global b;clear();b={set(p[0],p[1],-1)or p for p in t.chain(*map(v,b))if c(p)==3^(c(p)==2 and p in b)}

# -10
# import itertools as t;s,m=100,-1;b,v,c={(1,1),(0,1),(m,1),(1,0),(0,m)},lambda p:((p[0]+i,p[1]+j)for i,j in t.product((m,0,1),(m,0,1))if i+j*2),lambda p:sum((o in b)for o in v(p))
# def draw():global b;clear();b={set(p[0],p[1],m)or p for p in t.chain(*map(v,b))if c(p)==3^(c(p)==2 and p in b)}

# -31
# import itertools as t;s,r=100,lambda:int(random(s));b,v,c={(r(),r())for i in range(s*s)},lambda p:((p[0]+i,p[1]+j)for i,j in t.product((-1,0,1),(-1,0,1))if i+j*2),lambda p:sum((o in b)for o in v(p))
# def draw():global b;clear();b={set(p[0],p[1],-1)or p for p in t.chain(*map(v,b))if c(p)==3^(c(p)==2 and p in b)}

# millis()%2
# (i%s,i/s)for i in range(s*s)if noise(i)>.5
# tuple(int(random(s))for n in (1,1))for i in range(s*s)

# doesnt work
# import itertools as t;s,b=100,set();v,c=lambda p:((p[0]+i,p[1]+j)for i,j in t.product((-1,0,1),(-1,0,1))if i+j*2),lambda p:sum((o in b)for o in v(p))
# def draw():global b;clear();b={set(p[0],p[1],-1)or p for p in t.chain(*map(v,b))if c(p)==3^(c(p)==2 and p in b)}
# def mouseDragged():b.add((mouseX,mouseY));print b
