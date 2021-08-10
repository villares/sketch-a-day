def setup():
    global img
    size(500, 500)
    img = loadImage("imagem.png")
    # a máscara tem que ter tamanho igual a da imagem que vai ser clipada 
    clip_mask = createGraphics(img.width, img.height) 
    clip_mask.beginDraw()   
    clip_mask.noFill()
    for i in range(256):
        clip_mask.stroke(255 - i)  # cor de traço vai de branco a preto
        clip_mask.circle(img.width / 2, img.height / 2, i * 2)    
    clip_mask.endDraw()
    img.mask(clip_mask) # esta operação modifica a imagem
    imageMode(CENTER)                         
                                                                                                            
def draw():
    pass  # é necessário ter draw(), mesmo que vazio, para a interação com o mouse!
    
def mousePressed():
    translate(mouseX, mouseY)
    rotate(random(PI))
    image(img, 0, 0)
    
