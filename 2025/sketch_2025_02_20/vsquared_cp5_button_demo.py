# Example by @vsquared from this discussion:
# https://github.com/py5coding/py5generator/discussions/606#discussioncomment-12267883

# Uses Imported mode for py5
from controlP5 import ControlP5

this = get_current_sketch()
print(this)

def settings():
  size(400,200)

def setup():
  global btn1
  
  window_title("Button cp5 Demo")  
  cp5 = ControlP5(this)
  btn1 = cp5.addButton("btn1").setValue(0).setPosition(100,40).setSize(100,20)

# Never called
def btn1(value):
  print("a button event from btn1: " + value);

# Never called
def controlEvent(e):
  print(e.getController().getName())

# This works
def mouse_pressed(e):
  if(btn1.isPressed()):
    print("btn1 was pressed.")