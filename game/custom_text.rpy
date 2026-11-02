## Fonts
# Place your font files in the 'game' folder
define gui.text_font = "EBGaramond-Regular.ttf"  # Font for dialogue
define gui.name_text_font = "Cinzel-Regular.ttf"  # Font for character names

## Text Colors
define gui.text_color = "#FFFFFF"       # White dialogue text
define gui.name_text_color = "#FFD700"  # Gold character names

## Text Outline (for readability)
define gui.text_outlines = [(2, "#000000", 0, 0)] # 2px black outline
define gui.name_text_outlines = [(2, "#000000", 0, 0)]

## Font Sizes
define gui.text_size = 34  # Adjust for readability
define gui.name_text_size = 40 # Names slightly larger



## Name box customizations
define gui.name_xpos = 360 + 50
define gui.name_ypos = 25


define gui.dialogue_xpos = 0.24

## Center Test

#define gui.name_xpos = 0.5
#define gui.name_xalign = 0.5

#define gui.dialogue_xpos = 0.5
#define gui.dialogue_text_xalign = 0.5




# Floating Back History Skip Controls
#style window:

    #xalign 0.5
    #xfill True
    #yalign gui.textbox_yalign    
    #ysize gui.textbox_height + 23 

#    background Frame("images/textbox/textbox2.png", 150, 150)   



# Text box
# define gui.textbox_height  = 277
