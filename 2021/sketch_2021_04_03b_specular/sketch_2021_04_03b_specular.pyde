def setup():
    size(400, 400, P3D) 
    noStroke()
    background(0) 

def draw():
    background(0)
    fill(10, 51, 102) 
    ambientLight(255, 102, 255)
    lightSpecular(255, 204, 204)
    specular(255, 100, 100)
    translate(200, 200, 0)
    rotateY(frameCount / 50.0)
    directionalLight(255, 102, 102, 0, 0, -1)

    shininess(150)
    sphere(70)  # Left sphere
    translate(110, 0, 0) 
    shininess(150) 
    sphere(70)  # Right sphere
