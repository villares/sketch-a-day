# or get network by address, coordinates, bounding box, or any custom polygon
# ...useful when OSM just doesn't already have a polygon for the place you want
import osmnx as ox
import networkx as nx
import py5
import matplotlib as mpl

mpl.style.use(['ggplot', 'fast'])
mpl.use('agg')

# bml = (-23.54473, -46.64940)
# raio = 1200  # meters
# G = ox.graph_from_point(bml, dist=raio, network_type="walk")
# ox.save_graph_geopackage(G, 'BML.gpkg')
# ox.save_graphml(G, 'BML.graphml')

G = ox.load_graphml('BML.graphml')
fig, ax = ox.plot_graph(G, node_size=0, show=False)

# convert graph to line graph so edges become nodes and vice versa
#edge_centrality = nx.closeness_centrality(nx.line_graph(G))
#nx.set_edge_attributes(G, edge_centrality, "edge_centrality")
# color edges in original graph with closeness centralities from line graph
#ec = ox.plot.get_edge_colors_by_attr(G, "edge_centrality", cmap="inferno")
#ox.plot_graph(G, ax=ax, edge_color=ec, edge_linewidth=2, node_size=0)

#ox.plot_graph_route(G, route, route_color='r', ax=ax)
#s1 = py5.convert_shape(polygon1, flip_y_axis=True)


def setup():
    py5.size(800, 800)
    
    img = py5.convert_image(fig)
    py5.image(img, 0, 0)
    py5.save_frame('out.png')
    
    
py5.run_sketch()