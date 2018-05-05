'''
Character Set Proofer

from 
https://doc.robofont.com/documentation/building-tools/toolspace/drawbot/proof-charset/
'''

f = CurrentFont()

# main variables
boxHeight = 70
boxPaddingX = 0
boxPaddingY = 20
margin = 30

# calculate scale
s = float(boxHeight) / f.info.unitsPerEm

# define page size
size('A3Landscape')
pageWidth, pageHeight = width(), height()

# calculate initial positions
x = margin
y = pageHeight - margin - boxHeight

# draw glyphs
xBox, yBox = x, y
for i, glyphName in enumerate(f.glyphOrder):

    g = f[glyphName]
    boxWidth = g.width*s

    # jump to next line
    if xBox + boxWidth >= pageWidth - margin:
        xBox = x
        yBox -= boxHeight + boxPaddingY
        # jump to next page
        if yBox < margin:
            yBox = y
            newPage(pageWidth, pageHeight)

    # draw glyph cell
    stroke(1, 0, 0)
    fill(None)
    #rect(xBox, yBox, boxWidth, boxHeight)

    # draw glyph
    xGlyph = xBox
    yGlyph = yBox - f.info.descender*s
    save()
    translate(xGlyph, yGlyph)
    fill(0)
    stroke(None)
    scale(s)
    drawGlyph(g)
    restore()

    # move to next glyph
    xBox += boxWidth + boxPaddingX
