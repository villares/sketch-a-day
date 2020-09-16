from java.lang import System 
System.setProperty("jogl.disable.openglcore", "false")


import collections as c;h=256;d=c.deque([PVector()],h);t=translate;R=lambda:int(random(-2,2))*9
def setup():size(h*2,h*2,P3D);colorMode(3)
def draw():clear();t(h,h);rotateY(millis()/1e3);[(t(*p.mult(.995)),fill(p.z%h,h,h),box(9),t(*p*-1))for p in d];d.append(d[-1]+(R(),R(),R()))

# spinning too fast! for lack of 1 char
# import collections as c;h=256;d=c.deque([PVector()],h);t=translate;R=lambda:int(random(-2,2))*9
# def setup():size(h*2,h*2,P3D);colorMode(3)
# def draw():clear();t(h,h);rotateY(millis()/9.);u=d[-1];[(t(*p.sub(u/9)),fill(p.z%h,h,h),box(9),t(*p*-1))for p in d];d.append(u+(R(),R(),R()))


# import collections as c;h=256;d=c.deque([PVector()],h);t=translate;R=lambda:int(random(-2,2))*9
# def setup():size(h*2,h*2,P3D)#つぶやきProcessing
# def draw():clear();t(h,h);rotateY(millis()/1e3);u=d[-1];[(t(*p.sub(u/9)),fill(p.z%h,p.x%h,p.y%h),box(9),t(*p*-1))for p in d];d.append(u+(R(),R(),R()))
