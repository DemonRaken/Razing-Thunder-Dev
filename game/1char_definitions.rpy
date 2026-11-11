# Character Definitions
define config.side_image_only_not_showing = True   # make side image not show when full body is shown.
define config.say_attribute_transition = Dissolve(0.2, alpha=True)   # Always add a dissolve when expression changes
default preferences.text_cps = 30   

define bb = Character(ctc="ctc_horse", ctc_pause="ctc_horse", ctc_position="fixed",
                      window_background="textbox5",
                      callback=blip, cb_blipfile="audio/tick.wav")


define x = Character("???", kind=bb)
#Leopardo
define l = Character("El Leopardo", kind=bb, image="leo")
define lt = Character(kind=l, what_color="#4A86E8",  what_outlines=[(2,"#000000", 1, 1)],
window_background="textbox6")#, cb_blipfile=None)

#Tony
define t = Character("Antonio Ortiz", kind=l, image="tony")
define tt = Character(kind=t, what_color="#4A86E8", what_outlines=[(2,"#000000", 1, 1)],
window_background="textbox6")#, cb_blipfile=None)

define c = Character("Catalina Moreno", kind=bb, image="cata")
define r = Character ("Renata Vargas", kind=bb, image="rena")
define lu = Character ("Lucas Mendoza", kind=bb, image = "luc")

define e = Character ("Esteban Rojas", kind=bb, image="est")
define v = Character ("Vicente Ruiz", kind=bb, image="vi")

#NPCs
define tv = Character("TV Reporter", kind=bb)
define ch = Character("La Chispa", kind=bb)
define tg = Character("Thug", kind=bb)

# Change narrator to use the bb base
define narrator = Character(kind=bb, callback=blip, cb_blipfile="audio/type.wav", cb_bliploop=True)

# The time and location
define tl = Character(what_color="#38761D",  
what_outlines=[(2,"#000000", 1, 1)],
kind=narrator,
window_background="textbox6", 
what_text_align=0.5, 
what_xalign=0.5)