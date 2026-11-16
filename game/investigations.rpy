default aai_active = False
default aai_mode = None

style aai_button is button:
    background "#1a1a2e"
    hover_background "#16213e"
    xpadding 40
    ypadding 20

style aai_button_text is button_text:
    size 60
    bold True
    color "#ff5100"
    hover_color "#ff0000"
    outlines [
        (3, "#000000", 0, 0),
        (1, "#ffcc00", 0, 0)
    ]

screen aai_main_menu():
    hbox:
        xalign 0.5
        yalign 0.7
        spacing 50
        textbutton "Talk" style "aai_button":
            action [SetVariable("aai_mode", "talk"), Return()]
        textbutton "Examine"  style "aai_button":
            action [SetVariable("aai_mode", "examine"), Return()]
        textbutton "Present" style "aai_button":
            action [SetVariable("aai_mode", "present"), Return()]
        textbutton "Move" style "aai_button":
            action [SetVariable("aai_mode", "move"), Return()]

label debug_investigation:
    scene placeholder_granstands
    lt "I have an urge to investigate the breakroom."
    show text "{size=150}{color=#ff5100}Investigation{/color}{/size}"  at truecenter 
    pause 1.0
    hide text
    $ aai_active = True
    lt "I'll go immediately. No time to open my dossier to think!"
    call debug_investigate_breakroom
    n "This was the end."
    show text "{size=150}{color=#ff5100}Investigation END{/color}{/size}"  at truecenter 
    pause 1.0
    hide text
    $ aai_active = False

label debug_investigate_breakroom:
    scene placeholder_breakroom
    lt "Okay, I made it unseen to here. Now what should I do?"
    show cata angry
    c "Not so fast! What are you doing here? Did you plan to steal my lunch?"
    l "No... I came to investigate."
    c "Fine, let me help you"
    show cata angry at right
    show leo grin shine at left
    while aai_active:
        call screen aai_main_menu
        c "I sense that you want to [aai_mode] with me, let's do this!"
        while aai_mode == "talk":
            menu:
                "Ask Leo: What does he think of Tony?":
                    l neutral "I think Tony is a good boy. A bit too good."
                    l grin shine "He needs to go learn how to be a gaucho like me!"
                "Ask Catalina: What does she think of Tony?":
                    c "He is a nice, sweet boy. Nothing like this macho gaucho bastard near me."
                    l "Hey, who do you think you are calling a bas-- ahem. Yes."
                    c "Huh? You agreed with me?"
                    l "No. I don't have to say more to you."
                    c "Me too. Anything else to ask?"
                "Ask both: Who am I?":
                    c "Good Question."
                    l "I think you are someone I know..."
                    n "You are Leopardo from the future!"
                "Close":
                    $ aai_mode = None
        if aai_mode == "examine":
            n "There is nothing to do here."
        elif aai_mode == "present":
            $ dossier_tab_control = "present"
            call screen dossier_ui
            if ce_object in [dp_leo, de_mate]:
                l "Oh, I really love mate. Mate, oh my love."
                c "Stop it."
                l "Mateeee~!"
                c "Do you want to ask us something else?"
            elif ce_object == de_mask:
                c "Oh, I know this mask very well."
                l "Sweats."
                c "I know Leopardo's true identity"
                "Leopardo put his hand over Catalina's mouth"
                l "Please, be quiet. I'll let you drink from my Mate"
                c "Mphf?!"
            else:
                c "I don't know what to say about this. What about you?"
                l eh what "Nope, nothing here! Continue!"
            $ ce_object = None
            $ dossier_tab_control = "evidence"
        elif aai_mode == "move":
            $ dossier_tab_control = "map"
            #call screen dossier_ui
            n "You'd get softlocked here, so open dossier yourself, it should be on the map by default."
            $ dossier_tab_control = "map"
        c "Keep going until you are satisfied!"
            


# label debug_investigate_breakroom_end:
#     c "Did you find what you needed?"
#     l "Not yet, I need to investigate moreeee."
#     c "No. You are boring. Get out. "