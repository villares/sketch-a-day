from PIL import Image
import py5

def setup():
    py5.size(400, 400)
    
    img = Image.open('piscina.jpg')
    print(img)
    py5.image(img, 0, 0)
    
py5.run_sketch()
