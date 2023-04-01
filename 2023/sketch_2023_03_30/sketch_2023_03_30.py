size(600, 600)
for j in range(10):
    x = 50 + 50 * j
    for i in range(10):
        y = 50 + 50 * i
        fill(20 + i * 25,   # red
             20 + j * 25,   # green
             255 - i * 25)  # blue
        square(x, y, 50)
