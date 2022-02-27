from os import path, rename, walk


DIR = 'Roboczy'

for root, subFolder, files in walk(DIR):
    for geojson_filename in files:
        current_dir = root.split('/')[-1]
        old_filename = path.join(root, geojson_filename)

        new_filename = old_filename.replace('JPT', f'{current_dir}_JPT')
        rename(old_filename, new_filename)
