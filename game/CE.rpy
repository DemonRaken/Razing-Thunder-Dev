default ce_mode = None
default ce_rep = 8
default ce_object = None


style ce_button_text:   
   color "#4fd2fa"
   selected_color "#f00"

screen ce_ui():

   tag ce
   zorder 1
   showif quick_menu:
      hbox:
         xalign 0.7
         yalign 0.75
         spacing 10
         textbutton "◀" action Rollback()
         textbutton _("Press"):
            action SetVariable("ce_mode", None if ce_mode == "press" else "press")
            selected ce_mode == "press" style "ce_button"
         textbutton _("Present"):
            style "ce_button"
            action Show("dossier_ui")
            #action SetVariable("ce_mode", None if ce_mode == "object" else "object") 
            #selected ce_mode == "object" style "ce_button"
         vbox:
            text _("Reputation") size 20 xalign 0.5
            bar value ce_rep range 10 xsize 200 ysize 20 yalign 0.5
         textbutton "▶" action Return()
              
screen game_over():
      tag game_over
      zorder 100
      frame:
         xalign 0.5
         yalign 0.5
         background "#000000"
         text "Game Over":
            font gui.name_text_font 
            size 272
            color "#ffffff"

label game_over:
      $ renpy.block_rollback()
      stop music fadeout 0.5
      scene black with dissolve # fade to black
      show screen game_over()          # show the text + decoration
      play music sad fadein 0.5
      pause 7.0                        # keep it on screen for 3 seconds
      hide screen game_over with dissolve
      $ MainMenu(confirm=False)()      # return to main menu
      return   

default seen_announce_interrogation = False

label CE_start:
   # Turn off Rollback for the CE only
   #$ config.rollback_enabled = False
   $ renpy.block_rollback()
   if not seen_announce_interrogation:
      $ seen_announce_interrogation = True
      call announce_interrogation
   play music ce fadein 2.5
   show screen ce_ui
   return

label CE_end:
   
   hide screen ce_ui
   hide screen status_indicator
   # Turn on RollBack again.
   #$ config.rollback_enabled = True
   $ seen_announce_interrogation = False
   $ renpy.block_rollback()
   stop music fadeout 2.5
   return

label testCataCE:
   show screen dossier_icon
   t "Hello, Cata, I've got you up a corner. Kabadon!"
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
   #$ ce_rep -= 1
   call ce_penalty(2)
   return
   

label cata_flawed_testimony_CE_right:
   $ ce_mode = None
   $ ce_rep += 2
   t "Actually, I do carry a mate with me. You are terribly wrong!"
   c "Seems like you do."
   call CE_end
   jump deleteme

label ce_penalty(amount, notLeo=False):
   $ ce_rep -= amount
   if ce_rep <= 0:
      call CE_end
      $ tlt = tt if notLeo else lt
      tlt "Ack... I made too many mistakes!"
      scene black with fade
      tlt "I can't concentrate, at this rate, I'll never find the truth...!"
      tlt "I can't give up...!"
      call game_over

label announce_interrogation:
   show text _("{size=150}{color=#FF0000}Interrogation{/color}{/size}") at truecenter, investigation_text_zoom
   pause 2.0
   hide text
   return

