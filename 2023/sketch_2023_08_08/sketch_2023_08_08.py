def setup():
    size(400, 400)   # largura, altura
    background(0, 0, 200)
    fill(255)
    no_stroke()
    ellipse(200, 200, 20, 200) # nariz
    ellipse(100, 100, 100, 100)
    ellipse(300, 100, 100, 100)
    fill(0)
    ellipse(100, 100, 100, 50)
    ellipse(300, 100, 100, 50)
    fill(200, 0, 0)
    ellipse(100, 100, 50, 50)
    ellipse(300, 100, 50, 50)
    save('rosto_ale.png')
    