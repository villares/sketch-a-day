def setup():
    size(650, 650)
    background(0)
    colorMode(HSB)
    for y in range(25, 601, 30):
        total = 0
        while total < 600:
            largura = random(32)
            fill(largura * 8, 200, 200)
            rect(25 + total, y, largura, 30)
            total += largura
            # note que nesta versão o valor total
            # pode passar de 600
