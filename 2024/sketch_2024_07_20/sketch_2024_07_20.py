import prettymaps
import py5

place = "Sé, São Paulo, SP, Brasil"
plot = prettymaps.plot(place)
buildings = plot.geodataframes['building'].plot(ax=None)
#buildings.axes = []

message = 'data (c) OpenStreetMap contributors\n'\
          'https://www.openstreetmap.org/copyright\n'\
          'via github.com/marceloprates/prettymaps'

def setup():
    py5.size(800, 800)
    
    img = py5.convert_image(buildings.figure)
    py5.image(img, 0, 0, py5.width, py5.height)
    py5.fill(0)
    py5.text_font(py5.create_font('Inconsolata', 12))
    py5.text(message, 20, 20)
    py5.save_frame('out.png')
    
    
py5.run_sketch(block=False)