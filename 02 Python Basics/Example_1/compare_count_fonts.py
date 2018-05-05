# -*- coding: utf-8 -*

import os

# Declare variables
fontfolder = 'testfonts'
fontformats_dict = {
    'otf': 0,
    'ttf': 0,
    'woff2': 0
}

# os.listdir(<path_to_folder>) lists all files in this folder
for f in os.listdir(fontfolder):
    # String.split(<char>) splits a string at given character. Returns a list of every part.
    # We need the last part of this list.
    extension = f.split('.')[-1]
    if extension in fontformats_dict.keys():
        print('... found fontfile:', f)
        fontformats_dict[extension] += 1

# Loop through dict to show result
for ext, count in fontformats_dict.items():
    print(f'{ext}\t -> {count}')

# Print a message if the count differs per format
if not fontformats_dict['otf'] == fontformats_dict['ttf'] == fontformats_dict['woff2']:
    print('WARNING: Count of font formats is not the same!')

