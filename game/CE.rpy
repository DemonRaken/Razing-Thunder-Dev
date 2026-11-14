default ce_mode = None
default ce_rep = 8
default ce_object = None


style ce_button_text:   
   color "#4fd2fa"
   selected_color "#f00"

screen ce_ui():

   tag ce
   zorder 1
   hbox:
      xalign 0.65
      yalign 0.75
      spacing 10
      textbutton "◀" action Rollback()
      textbutton "Press":
         action SetVariable("ce_mode", None if ce_mode == "press" else "press")
         selected ce_mode == "press" style "ce_button"
      textbutton "Object":
         style "ce_button"
         action Show("dossier_ui")
         #action SetVariable("ce_mode", None if ce_mode == "object" else "object") 
         #selected ce_mode == "object" style "ce_button"
      vbox:
         text "Reputation" size 20 xalign 0.5
         bar value ce_rep range 10 xsize 200 ysize 20 yalign 0.5
      textbutton "▶" action Return()
              


label CE_start:
   # Turn off Rollback for the CE only
   #$ config.rollback_enabled = False
   $ renpy.block_rollback()
   show screen ce_ui
   return

label CE_end:
   hide screen ce_ui
   # Turn on RollBack again.
   #$ config.rollback_enabled = True
   $ renpy.block_rollback()
   return

label testCataCE:
   show screen dossier_icon
   t "Hello, Cata, I've got up a corner. Kabadon!"
   c "Oh no!"
   t "oh yes!"
   jump cata_flawed_testimony_CE

label cata_flawed_testimony_CE:
   call CE_start

   c "This is my very flawed testimony"
   if ce_mode == "object":
      call cata_flawed_testimony_CE_wrong
   if ce_mode == "press":
      $ ce_mode = None
      t "You are not supposed to say it's flawed, are you?"
      c "I suppose not. May I continue?"
      t "O-Okay."


   c "This isn't a contradiction. You don't carry any mates."
   if ce_mode == "object":
      if ce_object in [de_mate, dp_leo]:
         call cata_flawed_testimony_CE_right
      else:
         call cata_flawed_testimony_CE_wrong
   if ce_mode:
      $ ce_mode = None
      t "Are you certain about that?"
      c "Dead certain."
      tt "There's something weird about what she just said."
   

   c "By the way, you look parched. Don't you want to go and get a drink?"
   if ce_mode == "object":
      if ce_object in [de_mate, dp_leo]:
         call cata_flawed_testimony_CE_right
      else:
         call cata_flawed_testimony_CE_wrong
   if ce_mode:
      $ ce_mode = None
      t "You are right, I am feeling a bit thirsty..."
      c "Yes, just go out and get yourself a drink."
      tt "There's something weird about what she just said. A drink... Do I have a drink?"
   

   c "This is the end of my testimony"
   if ce_mode == "object":
      call cata_flawed_testimony_CE_wrong
   if ce_mode:
      $ ce_mode = None
      t "It can't be over already!"
      c "I am afraid it is."


   hide screen ce_ui
   tt "This is tough. Where is the contradiction? I need a gaming guide!"
   jump cata_flawed_testimony_CE

label cata_flawed_testimony_CE_wrong:   
   $ ce_mode = None
   t "Your testimony contradicts the evidence!!"
   c "No."
   t "Fuck!"
   # Penalty Damage
   $ ce_rep -= 1
   return
   

label cata_flawed_testimony_CE_right:
   $ ce_mode = None
   $ ce_rep += 2
   t "Actually, I do carry a mate with me. You are terribly wrong!"
   c "Seems like you do."
   call CE_end
   jump deleteme
