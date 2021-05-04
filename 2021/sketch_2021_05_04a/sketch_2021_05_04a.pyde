# sketch_2021_05_04 #Processing #Python based on a conversation with a student that will present sin() cos() to the class next week (it could become a "for with continue" example, missing from my examples...)      

def setup():
    size(600, 600)
    background(0)
    x_centro, y_centro = 300, 300
    raio = 250
    for angulo_em_graus in range(360):
        angulo_em_radianos = radians(angulo_em_graus)
        x = x_centro + raio * cos(angulo_em_radianos)
        y = y_centro + raio * sin(angulo_em_radianos)
        if angulo_em_graus % 30 == 0: # divisível por 30
            fill(0, 0, 255)
            tam = 10
        elif angulo_em_graus % 6 == 0: # divisível por 6
            fill(0, 255, 0)
            tam = 5
        else:  # não é multiplo nem de 30 nem de 6
            continue # pula o for para a próxima volta
        circle(x, y, tam) 
        
 
