from os import path, rename, walk


DIR = 'Roboczy'

filenames = {}

with open('scripts/robocze_all_file_rename.csv', 'r') as f:
    for line in f.readlines():
        old_name, new_name = line.strip().split(';')
        filenames[old_name] = new_name

for root, subFolder, files in walk(DIR):
    for geojson_filename in files:
        old_filename = path.join(root, geojson_filename)

        if geojson_filename in filenames:
            new_filename = path.join(root, filenames[geojson_filename])
            rename(old_filename, new_filename)
        else:
            print('Skipped: ' + old_filename)
