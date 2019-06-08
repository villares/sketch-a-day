"""
Welcome to the Silly Type Framework!
TODO:
    Edit Glyphs
    Draw word    
"""

import pickle
import silly

project = []

def setup():
    size(500, 500)
    strokeWeight(8)
    LAB = silly.Glyph("<",
                    ((2, 0, 1), (0, 2, 1), (2, 4, 1)),
                    (".012:"))
    project.append(LAB)
    a = silly.Glyph("a",
                    ((0, 4, 1), (2, 4, 1), (2, 0, 1),
                     (0, 0, 1), (0, 2, 1), (1.9, 2, 1), ),
                    (".012345:"))
    project.append(a)

    
def draw():
    background(240)
    x = silly.Glyph.m
    y = silly.Glyph.m * 8
    for g in project:
        pushMatrix()
        translate(x, y)
        g.plot()
        popMatrix()
        x += g.w * g.m
        if x > width - silly.Glyph.m * 2:
            x = silly.Glyph.m
            y += silly.Glyph.m * 8

def keyPressed():
    global project
    if key == "p":
        saveFrame("####.png")
    if key == "s":
        with open("data/project.data", "wb") as file_out:
            pickle.dump(project, file_out)
        println("project saved")

    if key == "r":
        with open("data/project.data", "rb") as file_in:
            saved_project = pickle.load(file_in)
            project += saved_project
        println("project loaded")
    print(project)
