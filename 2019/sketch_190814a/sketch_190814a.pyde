
size(500, 500)
margin = 12.5

for num in range(20):
    v = margin + num * 25
    for other_num in range(20):
        tam = random(10, 25)
        fill(random(128), random(256), random(128, 256))
        h = margin + other_num * 25
        ellipse(h, v, tam, tam)
