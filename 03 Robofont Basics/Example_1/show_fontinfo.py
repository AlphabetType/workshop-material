font = CurrentFont()
sample_glyph = font['space']
sample_width = sample_glyph.width

if font.selection:
    glyphlist = font.selection
else:
    glyphlist = font.keys()


for glyphname in glyphlist:
    glyph = font[glyphname]

    if glyph.width != sample_width:
        print("Wrong width in glyph: {0} ({1})".format(glyph.name, glyph.width))
