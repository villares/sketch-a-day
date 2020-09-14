from __future__ import print_function
from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")

# cabe, mas ainda não é o que eu queria...
V=PVector;t=translate;w=512;m=256;l=[V()];c=1e2
def setup():size(w,w,P3D)
def draw():u=l[-1];M=lambda r:[-5+5*(int(noise(m+b.magSq()/w)*c)%r)for m in range(3)];clear();t(*[m]*3);rotateX(len(l)/c);[(fill(*M(52)),t(*b),box(5),t(*b*-1),b.sub(u/9))for b in l];l[:]+=[u+M(3)]

# V=PVector;t=translate;w=512;m=256;l=[V()];c=1e2
# def setup():size(w,w,P3D)
# def draw():u=l[-1];N=lambda n:int(noise(n+b.mag()/c)*m);M=lambda m:5-5*(N(m+len(l))%3);clear();t(*[m]*3);rotateX(len(l)/c);[(t(*b),fill(N(1),N(2),N(3)),box(5),t(*b*-1),b.sub(u/9))for b in l];l[:]+=[u+V(M(1),M(2),M(3))]

# V=PVector;t=translate;w=512;m=256;l=[V()];c=1e2
# def setup():size(w,w,P3D)
# def draw():u=l[-1];N=lambda n:5*int(noise(n+i/c)*51);M=lambda m:5-5*(N(m)%3);clear();t(*[m]*3);rotateX(len(l)/c);[(t(*b),fill(N(1),N(2),N(3)),box(5),t(*b*-1),b.sub(u/9))for i,b in enumerate(l)];l[:]+=[u+V(M(1),M(2),M(3))]

# V=PVector;t=translate;w=512;m=256;l=[V()]
# def setup():size(w,w,P3D)
# def draw():u=l[-1];f=millis()/1e3;clear();t(*[m]*3);rotateX(f);[(t(*b),fill(b[0]%m,b[1]%m,b[2]%m),box(5),t(*b*-1),b.sub(u/9))for b in l];n=int(noise(f)*6);a=-5+(10*(n%2));l[:]+=[u+V(a*(n==3),a*(n==2),a*(n==1))]
