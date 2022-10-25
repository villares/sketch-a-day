def setup():
 size(800,800)
 color_mode(HSB);no_stroke();clear();t(400,500,120,-PI/2)
def t(X,Y,L,D):
 x,y,a,s,m=X+L*cos(D),Y+L*sin(D),radians(L),.8,255
 if L>5:triangle(*t(x,y,L*s,D+a),*t(x,y,L*s,D-a),x,fill((32*D)%m,m,m,2*(120-L))or y)
 return x,y #つぶやきProcessing #py5