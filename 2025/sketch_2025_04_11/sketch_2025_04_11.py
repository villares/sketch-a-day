import os
import leafmap.maplibregl as leafmap

#from villares.token_helpers import get_token
#os.environ["MAPTILER_KEY"] = get_token('maptiler', 'MAPTILER_KEY')

m = leafmap.Map(center=[-43, 23], zoom=3, style="liberty")
m.add_globe_control()

m.to_html('out.html')