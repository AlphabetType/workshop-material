# -*- coding: utf-8 -*

import os

# Declare variables
template_path = 'templates/html_template.html'

fontfolder = 'testfonts'
fontformats_dict = {
    'otf': 'url("{{fontpath}}") format("opentype")',
    'ttf': 'url("{{fontpath}}") format("truetype")',
    'woff2': 'url("{{fontpath}}") format("woff2")'
}

sample_fontsizes = [8, 12, 16, 24, 32, 48, 64, 72]
sample_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
sample_element_snippet = '''
<div class="sample_line">
    <div>{{fontsize}}px</div>
    <div style="font-size: {{fontsize}}px" class="testfont">
        {{sample_string}}
    </div>
</div>'''

# Use a methods, because it keeps your code clean and you do not repeat yourself
def get_ff_line(fontfile):
    extension = fontfile.split('.')[-1]
    new_statement = fontformats_dict[extension]
    new_statement = new_statement.replace('{{fontpath}}', fontfile)
    return new_statement

def get_sample_lines():
    content = ''
    for size in sample_fontsizes:
        size_as_string = str(size)
        content += sample_element_snippet.replace('{{fontsize}}', size_as_string).replace('{{sample_string}}', sample_string)

    return content

def get_html_content():
    with open(template_path, 'r') as html_file:
        html_content = html_file.read()

    return html_content

def createSamplepage(targetfolder, fontfile, html_content, sample_lines):
    print(f'Create sample in "{targetfolder}" for:\t {fontfile}')

    ff_line = get_ff_line(fontfile)
    content  = html_content.replace('{{fontfile}}', fontfile).replace('{{ff_line}}', ff_line).replace('{{samples}}', sample_lines)

    # Write file
    target_file = os.path.join(targetfolder, fontfile + '.html')
    with open(target_file, 'w+') as f:
        f.write(content)

# Variables to use for all fonts
html_content = get_html_content()
sample_lines = get_sample_lines()

# os.listdir(<path_to_folder>) lists all files in this folder
for f in os.listdir(fontfolder):
    # String.split(<char>) splits a string at given character. Returns a list of every part.
    # We need the last part of this list.
    extension = f.split('.')[-1]
    if extension in fontformats_dict.keys():
        createSamplepage(fontfolder, f, html_content, sample_lines)


