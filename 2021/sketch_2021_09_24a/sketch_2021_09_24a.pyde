import os


def setup():
    size(900, 900)
    background(0)
    scale(0.5)
    x = y = 0
    for root, dirs, files in os.walk("/home/villares/GitHub/sketch-a-day/"):
        path = root.split(os.sep)
        pl = len(path) - 5
        stroke(0, 0, 200)
        line(x, y, x + pl * 50, y)        
        print((pl - 1) * '-' + os.path.basename(root))
        for file in files:
            stroke(255)
            line(x, y, x + pl * 50, y)       
            print(pl * '-' + file)
            y += 1
            if y > 900 * 2:
                y = 0
                x = x + 300
