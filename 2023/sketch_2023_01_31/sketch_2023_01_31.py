# Kate Rose Morley's palette
# https://iamkate.com/data/12-bit-rainbow/
#Processing #Python #py5 imported mode
#genuary #genuary31 #トゥートProcessing 

palette = (
    '#817', '#a35', '#c66', '#e94',
    '#ed0', '#9d5', '#4d8', '#2cb',
    '#0bc', '#09c', '#36b', '#639'
    )

def setup():
    size(800, 800)
    no_stroke()
    background(0)

def draw():
    xc = yc = 400
    for i in range(6):
        m = 1 - abs(cos(radians(frame_count / 2))) ** 5
        r = 150 + 150 * m
        a = radians(frame_count / 2 + 60 * i)
        x = xc + r * cos(a)
        y = yc + r * sin(a)
        fill(palette[i])
        circle(x, y, 150)
        r = 300 - 150 * m
        a = a + radians(30)
        x = xc + r * cos(a)
        y = yc + r * sin(a)
        fill(palette[-1 -i])
        circle(x, y, 150)
        
#     if 360 < frame_count < 720 and frame_count % 2:
#         save_frame('###.png')