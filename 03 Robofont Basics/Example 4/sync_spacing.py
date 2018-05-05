# The script will be executed on the foremost font open in Robofont
font = CurrentFont()

# A sample glyph inside the font to get margin data from is defined
sample_glyph = font['o']

# The glyphs which should share margins with the sample glyph are grouped in 2 lists
o_left_glyphs = ['c', 'd', 'q', 'e']
o_right_glyphs = ['b', 'p']

# The script cycles through the list of similar glyphs
# The left margin of the sample glyph is applied to every glyph in the list
for glyph in o_left_glyphs:
    font[glyph].leftMargin = sample_glyph.leftMargin

# And the same for the right margin    
for glyph in o_right_glyphs:
    font[glyph].rightMargin = sample_glyph.rightMargin
    
print('='*5 + 'done' + '='*5 )
