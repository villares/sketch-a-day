from java.lang import System 
System.setProperty("jogl.disable.openglcore", "false")

import collections as c;h=256;d=c.deque([PVector()],h);t=translate;R=lambda:int(random(-2,2))*9#つぶやきProcessing
def setup():size(h*2,h*2,P3D);colorMode(3)
def draw():clear();t(h,h);u=d[-1];[(t(*p.sub(u/9)),fill(p.z%h,h,h),box(9),t(*p*-1))for p in d];d.append(u+(R(),R(),R()))


# import collections as c;V=PVector;h=256;d=c.deque((V(),),h);t=translate;R=lambda:int(random(-2,2))*9
# def setup():size(h*2,h*2,P3D);colorMode(3)#つぶやきProcessing
# def draw():clear();t(h,h);u=d[-1];[(t(*p.sub(u/9)),fill(p.z%h,h,h),box(9),t(*p*-1))for p in d];d.append(u+(R(),R(),R()))

# import collections as c;V=PVector;h=256;d=c.deque((V(),),h);t=translate;R=lambda:int(random(-2,2))*9
# def setup():size(h*2,h*2,P3D);colorMode(3)#つぶやきProcessing
# def draw():clear();t(h,h);u=d[-1];[(t(*p),fill(p.z%h,h,h),box(9),t(*p*-1),p.sub(u/9))for p in d];d.append(u+V(R(),R(),R()))

# import collections as c;V=PVector;d=c.deque((V(),),maxlen=150);t=translate;w,h=512,256;R=lambda:int(random(-2,2))*5
# def setup():size(w,w,P3D)
# def draw():clear();t(h,h,h);u=d[-1];[(t(*p),fill(p.x%h,p.y%h,p.z%h),box(5),t(*p*-1),p.sub(u/9)) for p in d];d.append(u+V(R(),R(),R()))

# import collections as c;V=PVector;d=c.deque((V(),),maxlen=150);t=translate;w,h=512,256;R=lambda:int(random(-2,2))*5
# def setup():size(w,w,P3D)
# def draw():clear();t(h,h,h);rotateY(millis()/1e3);u=d[-1];[(t(*p),fill(p.x%h,p.y%h,p.z%h),box(5),t(*p*-1),p.sub(u/h)) for p in d];d.append(u+V(R(),R(),R()))

# import collections as c;V=PVector;d=c.deque((V(),),maxlen=150);t=translate;w,h=512,256
# R=lambda:int(random(-2,2))*5
# def setup():size(w,w,P3D)
# def draw():clear();t(h,h,h);rotateY(millis()/1e3);u=d[-1];[(t(*p),fill(i%h,h,h),box(5),t(*p*-1),p.sub(u/h)) for i,p in enumerate(d)];d.append(u+V(R(),R(),R()))

# import collections as c;V=PVector;d=c.deque((V(),),maxlen=150);t=translate;w,h=512,256.
# R=lambda:int(random(-2,2))*5
# def setup():size(w,w,P3D);colorMode(3)
# def draw():clear();t(h,h,h);f=frameCount;rotateY(f/h);u=d[-1];[(t(*p),fill((f+i)%h,h,h),box(5),t(*p*-1),p.sub(u/h)) for i,p in enumerate(d)];d.append(u+V(R(),R(),R()))

# -63
# import collections as c;d=c.deque(maxlen=150)
# t=lambda v:translate(*v);w,h=512,256.
# V=PVector;R=lambda:int(random(-2,2))*5
# def setup():size(w,w,P3D);colorMode(3);d.append(V())
# def draw():clear();t((h,h,h));f=frameCount;rotateY(f/h);u=d[-1];[(t(p),fill((f+i)%h,h,h),box(5),t(p*-1),p.sub(u/h)) for i,p in enumerate(d)];d.append(u+V(R(),R(),R()))
