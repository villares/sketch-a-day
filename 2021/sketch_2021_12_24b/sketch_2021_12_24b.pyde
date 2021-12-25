

R,S,r=255,720,radians#つぶやきProcessing Python
def setup():size(S,S,P3D);colorMode(3);smooth(4)
def l(d):a=r(d/2.);s=R*sin(a);b=r(90*cos(a*9+frameCount*.03));z=s*cos(b);y=s*sin(b);x=R*cos(a);stroke(x%R,R,R);line(x*.5,y*.5,z*.5,x,y,z)
def draw():clear();translate(S/2,S/2);map(l,range(S))
