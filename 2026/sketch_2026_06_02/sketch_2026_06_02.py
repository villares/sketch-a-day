"""
Exemplo de geopandas.GeoDataFrame + Folium 
!pip install geopandas folium branca mapclassify
"""

import geopandas as gpd

#### para baixar arquivos do Google Drive
#import gdown
## https://drive.google.com/file/d/1i15KSXMikIKVILnkE5cyjIFnmgUxWzs_/view?usp=sharing
#file_id = "1i15KSXMikIKVILnkE5cyjIFnmgUxWzs_" # "ID_GOOGLE_DRIVE"
#output  = "indice_vuln_soc.gpkg" 
#gdown.download(id=file_id, output=output, quiet=False)
####

gdf = gpd.read_file('indice_vuln_soc.gpkg') # no Colab usar /content/...
print(gdf.columns)

mapa = gdf.explore("cd_indice_vulnerabilidade_social", tiles="CartoDB positron")
mapa.save("mapa.html")