# Inspired by https://twitter.com/ryotakob/status/1319998482283806720?s=20
#つぶやきProcessing
a=TWO_PI/6
r=rotate
t=translate
size(600,600)
clear()
stroke(-1)
s="A";d={"A":"B-A-B","B":"A+B+A"}
t(50,50)
for i in range(10):
 b=""
 for c in s:b+=d[c]if c in d else c
 s=b
for c in s:
 if c in"AB":line(0,0,2,0);t(2,0)       
 if c=="+":r(a)
 if c=="-":r(-a)
 
saveFrame("sketch_2020_10_24a.png")
