from __future__ import unicode_literals, print_function
import csv
from codecs import open

# Define data
data = [
    (1, "maçã,", 1.0),
    (42, "manga, uva", 2.0),
    (1337, "jaca", -1),
    (0, "kiwi", 123),
    (-2, "Nada.", 3),
]
def setup():
    size(600, 600)
    background(0, 100, 0)
    # textSize(24)
    textFont(createFont('Source Code Pro', 24))
    # Write CSV file
    with open("test.csv", "wt", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        # writer.writerow(["your", "header", "foo"])  # write header
        writer.writerows(data)
    
    # Read CSV file
    with open("test.csv", encoding="utf-8") as fp:
        reader = csv.reader(fp)
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]
        x, y = 20, 20
        for row in data_read:
            for item in row:
                print(item.ljust(12), end='')
                text(item.ljust(12), x, y)
                x += textWidth(item.ljust(12))
            y += 32
            x = 20
            print()
    
