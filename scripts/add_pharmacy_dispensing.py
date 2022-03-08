import json

from os import path, walk
from typing import Dict


DIR = path.join('Roboczy', 'apteki')


def rename_tag_addr_place_city(geojson: Dict) -> Dict:
    for feature in geojson['features']:
        feature['properties']['dispensing'] = 'yes'

    return geojson


for root, subFolder, files in walk(DIR):
    for geojson_filename in files:
        filename = path.join(root, geojson_filename)

        with open(filename, 'r', encoding='utf8') as f:
            geojson = json.load(f)

        modified_geojson = rename_tag_addr_place_city(geojson)

        with open(filename, 'w', encoding='utf8') as f:
            json.dump(modified_geojson, f, ensure_ascii=False, indent=4)
