import py5   # biblioteca de desenho
import osmnx as ox  # para pegar dados do OSM em geopandas.GeoDatFrama
import shapely # biblioteca de geometria usada pelo geopandas

DIST = 1000

ox.settings.log_console = True
# Obter tupla (lat, long) de um endereço (geocoding)
ponto = ox.geocode('São Paulo, SP, Brasil')

graph = ox.graph_from_point(
     ponto, network_type='drive', dist=DIST
     )
gdf_nodes, g_walk = ox.graph_to_gdfs(
    graph,
    nodes=True, edges=True,
    node_geometry=True,
    fill_edge_geometry=False
    )

graph = ox.graph_from_point(
     ponto, network_type='all', dist=DIST
     )
gdf_nodes, g_all = ox.graph_to_gdfs(
    graph,
    nodes=True, edges=True,
    node_geometry=True,
    fill_edge_geometry=False
    )


def setup():
    py5.size(1200, 600)
    #  Calculo para caber na tela usando .total_bounds do GDF
    x_min, y_min, x_max, y_max = g_walk.total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h
    # Aplicar tranformação nos GDFs (encolher pra caber na tela) inverte Y
    translate_and_scale_gdf(g_walk, -x_min, -y_min, x_scale, -y_scale)
    translate_and_scale_gdf(g_all, -x_min, -y_min, x_scale, -y_scale)
    # Desenhar ruas
    py5.stroke_weight(1)
    global shape_walk, shape_all
    py5.stroke(255, 0, 0)  # cor de traço das ruas
    shape_walk = py5.convert_shape(
        shapely.GeometryCollection(list(g_walk.geometry)))
    py5.stroke(0, 255, 0)  # cor de traço das ruas
    shape_all = py5.convert_shape(
        shapely.GeometryCollection(list(g_all.geometry)))
    
#def draw():
    py5.background(0)  # preto
    py5.shape(shape_all, 0, py5.height)  # desenhar começando na parte de baixo da tela
    py5.shape(shape_walk, 0, py5.height)  # desenhar começando na parte de baixo da tela
    py5.translate(py5.height, 0)
    py5.shape(shape_walk, 0, py5.height)  # desenhar começando na parte de baixo da tela
    py5.shape(shape_all, 0, py5.height)  # desenhar começando na parte de baixo da tela
    
    py5.save('out.png')

def translate_and_scale_gdf(gdf, x, y, x_scale, y_scale):
    gdf['geometry'] = gdf.geometry.translate(x, y)
    gdf['geometry'] = gdf.geometry.scale(
        xfact=x_scale, yfact=y_scale, origin=(0, 0))

py5.run_sketch(block=False)  # remove block=False if on MacOS

