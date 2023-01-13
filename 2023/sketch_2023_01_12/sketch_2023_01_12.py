colors = []
    
def setup():
    size(600, 600)
    no_stroke()
    color_mode(HSB)
    colors.extend((
        color(96, 255, 150),
        color(128, 255, 150),
        color(160, 255, 150),
        color(32, 255, 150)))
        
def draw():
    background(0)
    s = 10
    for y in range(2 * s, height + 4 * s, 6 * s):
        for x in range(-2 * s, width + 2 * s, 12 * s):
            if (y // (6 * s)) % 2:
                module(x, y, s)
            else:
                module(x + 6 * s, y, s)
                
    if frame_count % 2 and frame_count <=360:
        save_frame('###.png')
                
def module(x, y, s=10):
    pentagon(x, y, s)
    pentagon(x + 6 * s, y, s, r=1)
    pentagon(x - 6 * s, y, s, r=-1)
    pentagon(x, y, s, r=2)
            
def pentagon(x, y, s=10, r=0):
    fill(colors[r])
    stroke(0)
    j =  4 * cos(radians(frame_count)) * sin(radians(frame_count))
    pts = ((-2, -j), (2, j), (3, 3), (j, 4), (-3, 3))
    s_pts = [(x * s, y * s) for x, y in pts]
    with push_matrix():
            translate(x, y)
            rotate(HALF_PI * r)
            with begin_closed_shape():
                vertices(s_pts)
            