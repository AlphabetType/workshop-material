font = CurrentFont()
monospace = True
sample_glyph = font['space']
sample_width = sample_glyph.width

print("... checking font for sample width: ", sample_width)

if font.selection:
    glyphlist = font.selection
else:
    glyphlist = font.keys()


for glyphname in glyphlist:
    glyph = font[glyphname]

    if glyph.width != sample_width:
        monospace = False
        # glyph.mark = 1, 0, 0, 0.7
        print("Wrong width in glyph: {0} ({1})".format(glyph.name, glyph.width))

if monospace:
    print("Glyphs are monospaced!")