from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")


V=PVector;t=translate;w=512;l=[V()]#つぶやきProcessing
def setup():size(w,w,P3D)
def draw():u=l[-1];f=millis()/1e3;clear();t(*[w/2]*3);rotateX(f);[(t(*b),fill(*V(*b).setMag(w)),box(5),t(*b*-1),b.sub(u/9)) for b in l];n=int(noise(f)*6);a=random(-50,50);l.append(u+V(a*(n==3),a*(n==2),a*(n==1)))


# V=PVector;w=255;l=[V()]#つぶやきProcessing
# def t(v):translate(*v)
# def setup():size(w,w,P3D)
# def draw():u=l[-1];f=millis()/1e3;clear();t([w/2]*3);rotateX(f);[(t(b),fill(*V(*b).setMag(w)),box(5),t(b*-1),b.sub(u/9)) for b in l];n=int(noise(f)*6);a=random(-6,6);l.append(u+V(a*(n==3),a*(n==2),a*(n==1)))


# V=PVector;w=900;l=[V()];t=lambda v:translate(*v)#つぶやきProcessing 
# def setup():size(w, w, P3D)
# def draw():f=frameCount/50.;background(-1);t([w/2]*3);rotateX(f);[(t(b),box(5),t(b*-1),b.sub(l[-1]/10)) for b in l];n=int(noise(f)*6);v=V.random3D()*9;l.append(l[-1]+V(v.x*(n==3),v.y*(n==2),v.z*(n==1)))



# V=PVector;w=900;l=[V()];t=lambda v:translate(*v)
# def setup():size(w, w, P3D)
# def draw():f=frameCount/50.;clear();t([w/2]*3);rotateX(f);[(t(b),box(5),t(b*-1),b.sub(l[-1]/10)) for b in l];n=noise(f)*5;v=V.random3D()*9;l.append(l[-1]+V(v.x*int(1<n<6),v.y*int(2<n<7),v.z*int(3<n<9)))
