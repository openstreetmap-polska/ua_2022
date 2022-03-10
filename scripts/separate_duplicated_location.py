import json

from os import path, walk
from typing import Dict


DIR = 'Roboczy'
OFFSET = 0.00003

coordinates = set()


def fix_coordinates(geojson: Dict) -> Dict:

    for feature in geojson['features']:
        lon, lat = feature['geometry']['coordinates']
        while (lon, lat) in coordinates:
            lat -= OFFSET
        coordinates.add((lon, lat))

        feature['geometry']['coordinates'] = [lon, lat]

    return geojson


for root, subFolder, files in walk(DIR):
    for geojson_filename in files:
        filename = path.join(root, geojson_filename)

        with open(filename, 'r', encoding='utf8') as f:
            geojson = json.load(f)

        modified_geojson = fix_coordinates(geojson)

        with open(filename, 'w', encoding='utf8') as f:
            json.dump(modified_geojson, f, ensure_ascii=False, indent=4)
