from bienal import BienalClient, get_deep_ai_caption_position
from random import choice

img = None
analysis = None

def settings():
    global img, analysis, bienal
    
    bienal = BienalClient()
    print("### GET IMAGE")    
    # analysis = bienal.get_collection_image(col_id=16, image_id=911)  
    
def setup():
    size(500, 500)
    strokeWeight(2)
    
def draw():
    
    passado01 = bienal.get_collection(col_id=2)
    
    racy_imgs = []
    for img in passado01.images[:20]:
        racy = [nota for nota in img.clarifai.nsfw['concepts'] if nota['name'] == 'nsfw']
        if racy[0]['value'] > 0.1:
            racy_imgs.append(img)
    print(len(racy_imgs))
    print(racy_imgs[0])
    url = racy_imgs[0]['yolo_image']
    img = loadImage(url)
    image(img, 0, 0)    
    noLoop()
