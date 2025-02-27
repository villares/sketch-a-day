import osmnx as ox

from pathlib import Path
data_path = Path('buildings.data')

ox.settings.requests_timeout = 1000

city_boundary = ox.geocode_to_gdf("São Paulo, Brazil")
buildings = ox.features_from_place(
            "São Paulo, Brazil", tags={
                'building': True,
                })
with open(data_path, 'wb') as f:
        pickle.dump((city_boundary,
                     buildings
                     ), f)