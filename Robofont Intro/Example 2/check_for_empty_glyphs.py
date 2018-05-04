font = CurrentFont()

if font.selection:
    glyphlist = font.selection
else:
    glyphlist = font.keys()

for glyphname in glyphlist:
    glyph = font[glyphname]

    if len(glyph.contours) == 0 and len(glyph.components) == 0:
        print(glyph.name, 'is empty')

