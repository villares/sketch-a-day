from pyp5js import *


t=0;m=255;s=sin
def setup():
 createCanvas(510,510)
 noStroke()
def draw():
 global t
 background(0)
 t+=.01
 r=0
 while r < TAU:
  x=y=m
  d=0
  while d < 1:
   a=r+bezierTangent(s(r),s(t),s(t-r),0,d)
   x+=cos(a)*2
   y+=s(a)*2
   fill(y%m,d*m,x%m)
   circle(x,y,d*9)
   d+=.01
  r+=PI / 8

