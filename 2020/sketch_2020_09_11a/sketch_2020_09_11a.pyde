from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")

V = PVector
t = translate
w = 512
m = 256
l = [V()]
def setup():
    size(w, w, P3D)
def draw():
    u = l[-1]
    f = millis() / 1e3
    N = lambda o:int(noise(f+o) * 255)
    clear()
    t(*[m] * 3)
    rotateX(f)
    n = int(noise(f) * 6)
    [(t(*b), fill(N(i),N(i+100),N(200)), box(5), t(*b * -1), b.sub(u / 9))
     for i,b in enumerate(l)]
    a = -5 + (10 * (n % 2))
    l[:] += [u + V(a * (n == 3), a * (n == 2), a * (n == 1))]


# V=PVector;t=translate;w=512;m=256;l=[V()]
# def setup():size(w,w,P3D)
# def draw():u=l[-1];f=millis()/1e3;clear();t(*[m]*3);rotateX(f);[(t(*b),fill(b[0]%m,b[1]%m,b[2]%m),box(5),t(*b*-1),b.sub(u/9))for b in l];n=int(noise(f)*6);a=-5+(10*(n%2));l[:]+=[u+V(a*(n==3),a*(n==2),a*(n==1))]
