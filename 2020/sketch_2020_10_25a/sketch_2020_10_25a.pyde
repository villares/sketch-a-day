# Inspired by https://twitter.com/ryotakob/status/1319998482283806720?s=20
#つぶやきProcessing
t=translate
s="A";d={"A":"B-A-B","B":"+ABA+"}
for i in range(6):
 b=""   
 for c in s:b+=d.get(c,c)
 s=b
def setup():size(500,500)
def draw():
 t(250,250);background(-1);a=mouseX/79.
 for c in s:(c in"AB"and(line(0,0,9,0),t(9,0)))or rotate(a if c=="+"else-a) 
 
 # #つぶやきProcessing
# r=rotate
# t=translate
# s="A";d={"A":"B-A-B","B":"C++B++C","C":"AFFCFFA"}
# for i in range(6):
#  b=""
#  for c in s:b+=d[c]if c in d else c
#  s=b
# def setup():size(600,600);frameRate(9)
# def draw():t(300,300);background(-1);a=frameCount/20.;[line(0,0,4,0)or t(4,0)for c in s if not(c=="+" and not r(a))and not(c=="-" and not r(-a))]
