import osmnx as ox
import networkx as nx
import py5
import taxicab as tc

import matplotlib as mpl
#mpl.style.use(['ggplot', 'fast'])
#mpl.use('agg')

bml = (-23.54473, -46.64940)
# raio = 1200  # meters
# G = ox.graph_from_point(bml, dist=raio, network_type="walk")
# ox.save_graph_geopackage(G, 'BML.gpkg')
# ox.save_graphml(G, 'BML.graphml')
#G = ox.load_graphml('BML.graphml')
#fig, ax = ox.plot_graph(G, node_size=0, show=False)

# broken
# route = tc.distance.shortest_path(G, bml, (-23.54, -46.64))
#route =  ox.routing.shortest_path(G, bml, bml, weight='length', cpus=1)
#ox.plot_graph_route(G, route, route_color='r', ax=ax)

place = "Sé, São Paulo, SP, Brasil"
gdf = ox.geocode_to_gdf(place)

# get the street network, with retain_all=True to retain all the disconnected islands' networks
G = ox.graph_from_place(place, network_type="walk", retain_all=True)

# plot the network, but do not show it or close it yet
fig, ax = ox.plot_graph(
    G,
    show=False,
    close=False,
    bgcolor="#333333",
    edge_color="w",
    edge_linewidth=0.3,
    node_size=0,
)

# to this matplotlib axis, add the place shape(s)
gdf.plot(ax=ax, fc="k", ec="#FFFFFF", lw=1, alpha=1, zorder=-1)

# optionally set up the axes extents
margin = 0.1
west, south, east, north = gdf.unary_union.bounds
margin_ns = (north - south) * margin
margin_ew = (east - west) * margin
ax.set_ylim((south - margin_ns, north + margin_ns))
ax.set_xlim((west - margin_ew, east + margin_ew))
#mpl.pyplot.show()

def setup():
    py5.size(800, 800)
    
    img = py5.convert_image(fig)
    py5.image(img, 0, 0)
    py5.save_frame('out.png')
    
    
py5.run_sketch(block=False)