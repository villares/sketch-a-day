def setup():
    size(500, 500, P3D)
    
def draw():
    translate(250, 250, 0)
    background(255)
    rotateY(mouseX / 4.0) # 22.5 graus
    for x in range(-100, 101, 50):
        for y in range(-100, 101, 50):
            for z in range(-100, 101, 50):
                fill(100 + x, 100 + y, 100 + z)
                my_box(x, y, z, 25 + 25 * sin(x + y + frameCount / 20.0))
        
def my_box(x, y, z, tamanho):
    pushMatrix()
    translate(x, y, z)
    box(tamanho)
    popMatrix()

    
