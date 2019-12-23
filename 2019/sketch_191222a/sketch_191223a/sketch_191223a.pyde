add_library('Picking')  # import picking.*
from cube import Cube


# Picker picker
cubes = []
pickedCube = None

def setup():
    global picker
    size(300, 300, P3D)
    picker = Picker(this)

    smooth()

    cubes.append(
        Cube(0, 50, width * 0.50, height * 0.50, color(200, 100, 100)))
    cubes.append(
        Cube(1, 30, width * 0.80, height * 0.50, color(100, 200, 100)))
    cubes.append(
        Cube(2, 30, width * 0.20, height * 0.50, color(100, 200, 200)))


def mousePressed():
    global pickedCube
    id = picker.get(mouseX, mouseY)
    if id >= 0:
        pickedCube = cubes[id]


def mouseReleased():
    global pickedCube
    pickedCube = None


def draw():
    if mousePressed and pickedCube != None:
        pickedCube.rotate(
            radians((pmouseX - mouseX) % 360),
            radians((pmouseY - mouseY) % 360)
        )

    background(255)
    fill(200, 100, 100)

    for cube in cubes:
        picker.start(cube.id)
        cube.draw()

    picker.stop()
