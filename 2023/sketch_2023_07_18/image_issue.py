
def setup():
    img = create_image(100, 100, ARGB)
    print(type(img))
    new_img = img.copy()
    print(type(new_img))
    
    img_from_file = load_image('a.png')
    print(type(img_from_file))
    new_iff = img_from_file.copy()
    print(type(new_iff))
    