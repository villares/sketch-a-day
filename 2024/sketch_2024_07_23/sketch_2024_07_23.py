def setup():
    size(1280, 720)
    img = load_image('garoa.jpg')
    mirror_half(img)
    image(img, 0, 0)

def mirror_half(picture):
    pxs = get_pixels_array(picture)
    target = len(pxs) - 1
    for index in range(0,len(pxs)//2):
        pxs[target] = pxs[index]
        target = target - 1
        
def get_pixels_array(picture):
    """
    Hidding object orientation, to mimic 
    Guzdia & Ericson's MediaComp textbook.
    """
    picture.load_pixels()
    return picture.pixels
