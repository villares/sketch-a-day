import py5   # biblioteca de desenho
import osmnx as ox  # para pegar dados do OSM em geopandas.GeoDatFrama
import shapely # biblioteca de geometria usada pelo geopandas
import geopandas as gpd
import pandas as pd

DIST = 500

ox.settings.log_console = True
# Obter tupla (lat, long) de um endereço (geocoding)
ponto = ox.geocode('Praça da República, São Paulo, SP, Brasil')

buildings = ox.features_from_point(
    ponto, dist=DIST, tags={'building': True}
    )
graphw = ox.graph_from_point(
     ponto, network_type='walk', dist=DIST
     )
gdf_nodes, g_walk = ox.graph_to_gdfs(
    graphw,
    nodes=True, edges=True,
    node_geometry=True,
    fill_edge_geometry=False
    )

grapha = ox.graph_from_point(
     ponto, network_type='all', dist=DIST
     )
gdf_nodes, g_all = ox.graph_to_gdfs(
    grapha,
    nodes=True, edges=True,
    node_geometry=True,
    fill_edge_geometry=False
    )

# # Testing some merging
# g_all  = gpd.GeoDataFrame(
#     pd.concat([g_all, g_walk], ignore_index=True),
#     crs=g_all.crs)

def setup():
    global shape_walk, shape_all
    py5.size(1200, 500)
    #  Calculo para caber na tela usando .total_bounds do GDF
    x_min, y_min, x_max, y_max = g_walk.total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h
    # Aplicar tranformação nos GDFs (encolher pra caber na tela) inverte Y
    translate_and_scale_gdf(g_walk, -x_min, -y_min, x_scale, -y_scale)
    translate_and_scale_gdf(g_all, -x_min, -y_min, x_scale, -y_scale)
    translate_and_scale_gdf(buildings, -x_min, -y_min, x_scale, -y_scale)
    shape_walk = g_walk.geometry.union_all()
    shape_all = g_all.geometry.union_all()
    shape_b = shapely.GeometryCollection(list(buildings.geometry))

#def draw():
    py5.background(0)  # preto
    py5.fill(255, 100)
    py5.stroke(255, 0, 0)  # red
    py5.shape(shape_all, 0, py5.height)  
    py5.stroke(0, 255, 0)  # green
    py5.shape(shape_walk, 0, py5.height)
    py5.stroke(0)
    py5.shape(shape_b,  0, py5.height)
    
    py5.translate(600,0)
    py5.stroke(0, 255, 0)  # cor de traço das ruas    
    py5.shape(shape_walk, 0, py5.height)  
    py5.stroke(255, 0, 0)  # cor de traço das ruas
    py5.shape(shape_all, 0, py5.height)  
    py5.stroke(0)
    py5.shape(shape_b,  0, py5.height)
    
    py5.save('out.png')

def translate_and_scale_gdf(gdf, x, y, x_scale, y_scale):
    gdf['geometry'] = gdf.geometry.translate(x, y)
    gdf['geometry'] = gdf.geometry.scale(
        xfact=x_scale, yfact=y_scale, origin=(0, 0))

py5.run_sketch(block=False)  # remove block=False if on MacOS

