# -*- coding: utf-8 -*

import os

# Declare variables
fontfolder = 'testfonts'
fontformats = ['otf', 'ttf', 'woff2']
count = 0

# os.listdir(<path_to_folder>) lists all files in this folder
for f in os.listdir(fontfolder):
    # String.split(<char>) splits a string at given character. Returns a list of every part.
    # We need the last part of this list.
    extension = f.split('.')[-1]
    if extension in fontformats:
        print('... found fontfile:', f)
        count += 1

# Print result in formatted string
# (You can use " in a '-string withouth excaping it; and vice versa)
print(f'Fontfiles in "{fontfolder}": {count}')
