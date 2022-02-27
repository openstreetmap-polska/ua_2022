import json

from os import path, walk
from typing import Dict


DIR = path.join('Roboczy', 'szpitale')


KEYS = {
    'nazwa': 'name',
    'telefon': 'phone',
    'e-mail': 'email',
    'www': 'website'
}


def clear_name(name: str) -> str:
    name = name.replace('  ', ' ').strip()
    name = name.lower()

    if name == 'szpital':
        return ''

    return name.title()


def convert_properties_to_osm(geojson: Dict) -> Dict:
    for feature in geojson['features']:
        properties = {}

        # filter and rename keys
        for k, v in feature['properties'].items():
            if k not in KEYS or v is None:
                continue

            properties[KEYS[k]] = v

        if 'name' in properties:
            cleared_name = clear_name(properties['name'])
            if cleared_name:
                properties['name'] = cleared_name
            else:
                del properties['name']

        # add osm tags
        properties['amenity'] = 'hospital'
        properties['emergency'] = 'yes'
        properties['healthcare'] = 'hospital'

        feature['properties'] = properties

    return geojson


for root, subFolder, files in walk(DIR):
    for geojson_filename in files:
        filename = path.join(root, geojson_filename)

        with open(filename, 'r', encoding='utf8') as f:
            geojson = json.load(f)

        modified_geojson = convert_properties_to_osm(geojson)

        with open(filename, 'w', encoding='utf8') as f:
            json.dump(modified_geojson, f, ensure_ascii=False, indent=4)
