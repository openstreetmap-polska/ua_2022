import json

from os import path, walk
from typing import Dict


DIR = path.join('Roboczy')


def rename_tag_addr_place_city(geojson: Dict) -> Dict:
    for feature in geojson['features']:
        addr_city = feature['properties'].get('addr:city', None)

        if not addr_city:
            continue

        if not feature['properties'].get('addr:street', ''):
            feature['properties']['addr:place'] = addr_city
            del feature['properties']['addr:city']

    return geojson


for root, subFolder, files in walk(DIR):
    for geojson_filename in files:
        filename = path.join(root, geojson_filename)

        with open(filename, 'r', encoding='utf8') as f:
            geojson = json.load(f)

        modified_geojson = rename_tag_addr_place_city(geojson)

        with open(filename, 'w', encoding='utf8') as f:
            json.dump(modified_geojson, f, ensure_ascii=False, indent=4)
