def setup():
    global offscreen
    size(800, 500)
    # vamos usar uma área de desenho fora da tela "offscreen buffer"
    offscreen = createGraphics(400, height) 
    offscreen.beginDraw()  # necessário antes de desenhar na área
    offscreen.background(0, 200, 0)
    offscreen.fill(255)  
    for _ in range(100):
        offscreen.rect(random(400), random(height), 50, 50)
    offscreen.endDraw() # também é preciso encerrar o desenho
    cursor(CROSS)  # cursor em cruz
                                         
def draw():
    background(150, 150, 200)
    # Uma outra área de desenho que vai ser uma máscara de recorte:  Regiões
    # brancas na máscara indicam posiçoes da imagem final que são mostradas,
    # regiões pretas serão ocultadas e as cinzas intermediárias mostradas translúcidas
    clip_mask = createGraphics(400, height)
    clip_mask.beginDraw()   
    clip_mask.noFill()  # usaremos círculos vazados
    for i in range(128):
        clip_mask.stroke(255 - i * 2)  # cor de traço variável
        clip_mask.circle(mouseX, mouseY, i)    
    clip_mask.endDraw() 
 
    result = offscreen.copy()  # uma cópia da imagem original
    result.mask(clip_mask)     # esta operação modifica a imagem
    image(result, 0, 0)        # mostra a imagem modificada
    image(offscreen, 400, 0)   # mostra a imagem original
    
