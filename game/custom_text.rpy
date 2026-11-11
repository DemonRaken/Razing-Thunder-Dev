## Fonts
# Place your font files in the 'game' folder
define gui.text_font = "LibreBaskerville-Regular.ttf"  # Font for dialogue
define gui.name_text_font = "Cinzel-Regular.ttf"  # Font for character names

## Text Colors
define gui.text_color = "#FFFFFF"       # White dialogue text
define gui.name_text_color = "#FFD700"  # Gold character names

## Text Outline (for readability)
define gui.text_outlines = [(1, "#000000", 1, 1)] # 1px saddle brown outline
define gui.name_text_outlines = [(1, "#8C4704", 0, 0)]

## Font Sizes
define gui.text_size = 37  # Adjust for readability
define gui.name_text_size = 48 # Names slightly larger

## Name box customizations
define gui.name_xpos = 0.005
define gui.name_ypos = 5

## Dialogue customization
define gui.dialogue_xpos = 0.12
define gui.dialogue_ypos = 0.33
define gui.dialogue_width = 0.72 #0.76

# Textbox fine tweaking
style window:    
    xalign 0.9
    xsize 1536
    ysize 301
    yalign 0.97
    #xfill False
    #ysize 0.9
    #ysize 200
    #ysize gui.textbox_height + 23
    #xsize 400
    #text_size 200

#    background Frame("images/textbox/textbox2.png", 150, 150)   

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
