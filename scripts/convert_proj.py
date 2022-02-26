from pyproj import Transformer

import json

from os import path, walk
from typing import Dict


DIR = 'Roboczy'


transformer = Transformer.from_crs('EPSG:2180', 'EPSG:4326')



def epsg2180_to_epsg_4326(geojson: Dict) -> Dict:
    geojson['crs']['properties']['name'] = 'urn:ogc:def:crs:EPSG::4326'
    
    for feature in geojson['features']:
        x, y = feature['geometry']['coordinates']
        lat, lon = transformer.transform(y, x)
        feature['geometry']['coordinates'] = [lon, lat]

    return geojson


for root, subFolder, files in walk(DIR):
    for geojson_filename in files:
        filename = path.join(root, geojson_filename)
        
        try:
            with open(filename, 'r', encoding='utf8') as f:
                geojson = json.load(f)
    
            modified_geojson = epsg2180_to_epsg_4326(geojson)

            with open(filename, 'w', encoding='utf8') as f:
                json.dump(modified_geojson, f, ensure_ascii=False, indent=4)
        
        except Exception as e:
            print(e)

