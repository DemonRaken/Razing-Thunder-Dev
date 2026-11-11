# Character Definitions
define config.side_image_only_not_showing = True   # make side image not show when full body is shown.
define config.say_attribute_transition = Dissolve(0.2, alpha=True)   # Always add a dissolve when expression changes
default preferences.text_cps = 30   

define bb = Character(ctc="ctc_horse", ctc_pause="ctc_horse", ctc_position="fixed",
                      window_background="textbox5",
                      callback=blip, cb_blipfile="audio/tick.wav")


define x = Character("???", kind=bb)
define l = Character("El Leopardo", kind=bb, image="leo")
define lt = Character(kind=l, what_color="#4A86E8",  what_outlines=[(0,"#4A86E8", 0, 0)],
what_bold=False, window_background="textbox6")#, cb_blipfile=None)
define t = Character("Antonio Ortiz", kind=l, image="tony")
define tt = Character(kind=t, what_color="#4A86E8", what_outlines=[(1,"#ffd700")])#, cb_blipfile=None)
define c = Character("Catalina Moreno", kind=bb, image="cata")
define e = Character ("Esteban Rojas", kind=bb)
define tv = Character("TV Reporter", kind=bb)
define ch = Character("La Chispa", kind=bb)
define tg = Character("Thug", kind=bb)

# Change narrator to use the bb base
define narrator = Character(kind=bb, callback=blip, cb_blipfile="audio/type.wav", cb_bliploop=True)

# The time and location
define tl = Character(what_color="#38761D", what_bold=True, kind=narrator)