# This script helps to generate a simple proof doc

# Define the glyphs to test
glyphs = ['a', 'h', 'e', 'Euro']

# Define a format
format = "A3Landscape"

# Get all open fonts in Robofont, sorted by styleName
fonts = AllFonts('styleName')

# Define a margin(in this case for the buttom)
margin = 30

# Loop thorugh all glyphs of the previously defined list
for glyph in glyphs:
    
    # Create a new page for the glyph
    newPage(format)
    
    # Shift the origin point slightly to the left and up
    translate(margin/2, margin)
    
    # Scale the drawing so it will roughly fit on the page
    # yes, this could be done more elegantly
    scale(0.4)
    
    # Cycle through the fonts that we got in Line 8
    for font in fonts:
        # Define a color to fill the drawing
        fill(0,0,0)
        # Draw the glyph in the font we are currently at
        drawGlyph(font[glyph])
        
        # shift by the width of the glyph, otherwise glyphs would overlap
        translate(font[glyph].width, 0)
    
