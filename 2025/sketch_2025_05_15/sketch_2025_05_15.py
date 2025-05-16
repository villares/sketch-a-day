    
    

def setup():
    size(600, 600)
    no_loop()    
    
def draw():
#     begin_record(PDF, '####.pdf')
    background(0, 100, 200)
    stroke(255)
    galho(300, 500, 50, 45) # x, y, tamanho, angulo
    stroke(0)
    galho(200, 300, 50, 30)
#     end_record()

def galho(x, y, tamanho, angulo):
    redutor = 0.80
    push_matrix()
    translate(x, y)
    line(0, 0, 0, -tamanho)
    translate(0, -tamanho)
    if tamanho > 5:
        rotate(radians(angulo))  
        galho(0, 0, tamanho * redutor, angulo)
        rotate(radians(-angulo * 2))
        galho(0, 0, tamanho * redutor, angulo)        
    pop_matrix()
    
def key_pressed():
    save_frame('###.png')