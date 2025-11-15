import py5   # biblioteca de desenho
import osmnx as ox  # para pegar dados do OSM em geopandas.GeoDatFrama
import shapely # biblioteca de geometria usada pelo geopandas

DIST = 7000

ox.settings.log_console = True
# Obter tupla (lat, long) de um endereço (geocoding)
ponto = ox.geocode('Brasília, DF, Brasil')
# Obter GeoDataFrame de um local (place)
predios = ox.features.features_from_point(
    ponto, # tupla de cooedenadas
    tags={'building': True},
    dist=DIST
    )
aguas = ox.features.features_from_point(
    ponto, # tupla de cooedenadas
    tags={'water': True},
    dist=DIST
    )
graph = ox.graph_from_point(
     ponto, network_type='all', dist=DIST
     )
gdf_nodes, caminhos = ox.graph_to_gdfs(
    graph,
    nodes=True, edges=True,
    node_geometry=True,
    fill_edge_geometry=False
    )

def setup():
    py5.size(800, 800)
    # começa a gravar um pdf
    py5.begin_record(py5.PDF, 'mapa-bsb.pdf')
    py5.background(0)  # preto
    #  Calculo para caber na tela usando .total_bounds do GDF
    x_min, y_min, x_max, y_max = predios.total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h
    # Aplicar tranformação nos GDFs (encolher pra caber na tela) inverte Y
    translate_and_scale_gdf(predios, -x_min, -y_min, x_scale, -y_scale)
    translate_and_scale_gdf(caminhos, -x_min, -y_min, x_scale, -y_scale)
    translate_and_scale_gdf(aguas, -x_min, -y_min, x_scale, -y_scale)
    # Desenhar aguas
    py5.no_stroke()
    py5.fill(200) # cinza 200
    geometria_aguas = shapely.GeometryCollection(list(aguas.geometry))
    py5.shape(geometria_aguas, 0, py5.height)  # desenhar começando na parte de baixo da tela
    # Desenhar na tela predios
    py5.stroke_weight(0.1)
    py5.stroke(0)  # cor do traço
    py5.color_mode(py5.HSB)  # Hue (Matiz), Saturation, Brightness
    grupo_predios = py5.create_shape(py5.GROUP)
    for geometria_predio in predios.geometry:
        py5.fill(py5.random(255), 255, 255)  # Matiz, Sat, Bri
        grupo_predios.add_child(py5.convert_shape(geometria_predio))
    py5.shape(grupo_predios, 0, py5.height)  # desenhar começando na parte de baixo da tela
    # Desenhar ruas
    py5.stroke(255)  # cor de traço das ruas
    py5.stroke_weight(0.5)
    py5.fill(240) # cinza claro
    geometria_caminhos = shapely.GeometryCollection(list(caminhos.geometry))
    py5.shape(geometria_caminhos, 0, py5.height)  # desenhar começando na parte de baixo da tela
    # termina de gravar o PDF
    py5.end_record()
   
def translate_and_scale_gdf(gdf, x, y, x_scale, y_scale):
    gdf['geometry'] = gdf.geometry.translate(x, y)
    gdf['geometry'] = gdf.geometry.scale(
        xfact=x_scale, yfact=y_scale, origin=(0, 0))

py5.run_sketch(block=False)  # remove block=False if on MacOS

