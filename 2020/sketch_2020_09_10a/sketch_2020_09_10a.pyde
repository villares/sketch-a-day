from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")

V=PVector;t=translate;w=512;m=256;l=[V()]
def setup():size(w,w,P3D)
def draw():u=l[-1];f=millis()/1e3;clear();t(*[m]*3);rotateX(f);[(t(*b),fill(b[0]%m,b[1]%m,b[2]%m),box(5),t(*b*-1),b.sub(u/9))for b in l];n=int(noise(f)*6);a=-5+(10*(n%2));l[:]+=[u+V(a*(n==3),a*(n==2),a*(n==1))]



# V=PVector;t=translate;w=512;m=256;l=[V()]
# def setup():size(w,w,P3D);stroke(-1)
# def draw():u=l[-1];f=millis()/1e3;clear();t(*[m]*3);rotateX(f);[(t(*b), fill(b[0]%m,b[1]%m,b[2]%m),box(5),t(*b*-1),b.sub(u /9))for b in l];n=int(noise(f)*6);a=-5+(10*(n%2));l.append(u+V(a*(n==3),a*(n==2),a*(n==1)))

# def setup():
#     size(w, w, P3D); strokeWeight(3)
# def draw():
#     u = l[-1]
#     f = millis() / 1e4
#     clear()
#     t(*[w / 2] * 3)
#     rotateX(f);stroke(-1)  #(stroke(*V(*b).setMag(w))
#     [(line(b[0],b[1],b[2],p[0],p[1],p[2]), b.sub(u / 9))
#      for b,p  in zip(l[3:],l[2:])]
#     n = int(noise(f) * 6)
#     a = random(-10, 10)
#     l.append(u + V(a * (n == 3), a * (n == 2), a * (n == 1)))
