def setup():
    size(650, 650)
    background(0, 0, 200)
    
    total = 0
    while total < 600:
        largura = random(32)
        fill(largura * 8)
        rect(25 + total, 25, largura, 600)
        total += largura
        # note que nesta versão o valor total
        # pode passar de 600
