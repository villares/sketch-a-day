#つぶやきshoebotpython
from random import choice
#from math import pi
w=500

def setup():
 size(w,w)
 speed(5)
 stroke(0)
 print('a')
    
def draw():
 transform(CORNER)
 translate(w/2,w/2)
 for i in range(100):
  #rotate(radians=pi/2*choice((-1,1)))
  rotate(90*choice((-1,1))) # degrees are default in shoebot
  line(0,0,i,0)
  translate(i,0)
  



