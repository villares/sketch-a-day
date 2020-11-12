size(1200,1200) 
strokeWeight(3)
a=PI/1.5
s="A"
d={"A":"B--FAF--B","B":"B+FCF+B","C":"AFCFAF"}
clear();stroke(-1)
for i in range(8):
 b=""
 for c in s:b+=d.get(c, c)
 s=b
for c in s:
 if c=="+":rotate(a)
 elif c=="-":rotate(-a)
 else:line(0,0,9*3,0);translate(9 *3,0)
#つぶやきProcessing
saveFrame("LS_002.png")

# size(400,400) 
# a=PI/3
# s="A";r=rotate
# d={"A":"B--FAFF--B","B":"C+FFBF+C","C":"AFCFAF"}
# clear();stroke(-1)
# for i in range(7):
#  b=""
#  for c in s:b+=d.get(c, c)
#  s=b
# for c in s:
#  if c=="+":r(a)
#  elif c=="-":r(-a)
#  else:line(0,0,9,0);translate(9,0)
# #つぶやきProcessing
