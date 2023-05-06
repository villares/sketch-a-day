def setup():
    global us_map, michigan, ohio  
    size(640, 360)    
    us_map = load_shape("usa-wikipedia.svg")
    michigan = us_map.get_child("MI")
    ohio = us_map.get_child("OH")
    for child in us_map.get_children():
        print(child.get_name())

def draw():
    background(255)
    # Draw the full map
    shape(us_map, -600, -180)
    # Disable the colors found in the SVG file
    #michigan.disable_style()
    # Set our own coloring
    fill(0, 51, 102)
    no_stroke()
    # Draw a single state
    michigan.set_fill(color(0, 255, 0))  # não us_mapr disable_style()
    shape(michigan, -600, -180) # Wolverines!
    # Disable the colors found in the SVG file
    ohio.disable_style()
    # Set our own coloring
    fill(153, 0, 0)
    no_stroke()
    # Draw a single state
    shape(ohio, -600, -180)    # Buckeyes!
    for child in us_map.get_children():
        child.set_fill(color(random(200)))
