from vpython import *
#GlowScript 3.0 VPython
# https://www.glowscript.org/#/user/villares/folder/MyPrograms/program/boxes
from random import choice
N = 10
scene.title =  """TweetVPython"""

boxes = []
L, s  = 6, 1/6
sizes = (s, s*2, s*3)

def rv():
    return vector(choice(sizes),choice(sizes),choice(sizes))

for x in range(N):
  for y in range(N):
    for z in range(N):
      b = box(color=vector(x/N,y/N,z/N),
            pos=vector(L*(x/(N-1)-.5),L*(y/(N-1)-.5),L*(z/(N-1)-.5)),
            size=rv())
      boxes.append(b)
      
while True:
  rate(1)
  for b in boxes:
      b.size=rv()