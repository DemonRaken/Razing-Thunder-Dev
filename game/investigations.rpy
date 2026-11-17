default aai_active = False
default aai_mode = None
default aai_travel = None
default aai_travel_done = []
default aai_travel_left = []
default who_did_it_choice = None

init python:
    def aai_investigated(areaname):
        if areaname in aai_travel_left:
            aai_travel_left.remove(areaname)
            aai_travel_done.append(areaname)

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

transform investigation_text_zoom:
    alpha 0
    xzoom 1.5
    linear 0.5 alpha 1.0
    ease 0.5 xzoom 1.0


transform char_entrance(i):
    alpha 0
    yoffset 40
    pause (i * 0.08)
    linear 0.4 alpha 1.0
    linear 0.4 yoffset 0   

screen who_did_it():
    frame:
        yalign 0.5
        background None
        vbox:
            yalign 0.5

            frame:
                xysize (config.screen_width, 150)
                text "{size=100}{color=#ff5100}Who did it?!{/color}{/size}" at investigation_text_zoom:
                    xalign 0.5
                    yalign 0.5
                    kerning 2
            frame:
                xalign 0.5
                hbox:
                    for i, c in enumerate([c, r, lu, e, s, me, en]):
                        imagebutton:
                                at char_entrance(i)
                                idle Transform(c.image_tag + " neutral", xysize=(200, 250), crop=(50, 0, 600, 500))
                                #selected Transform(c.image_tag + " neutral", xysize=(250, 350), xzoom=1.08, yzoom=1.08)
                                idle_foreground VBox(Text(c.name, size=22, color="#ffffff"), xalign=0.5, yalign=0.9, ypadding=8, background=Solid("#000000cc"))
                                hover_foreground VBox(Text(c.name, size=22, color="#ff0000"), xalign=0.5, yalign=0.9, ypadding=8, background=Solid("#ff510099"))
                                action [SetVariable("who_did_it_choice", c), Return()]
                                xysize (200, 250)

            frame:
                xysize (config.screen_width, 350)
                add "leo point":
                    xalign 0.5
                    crop (0, 250, 600, 50)
                    fit "cover"

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
    jump debug_investigation_start

label debug_investigation_start:
    scene placeholder_granstands
    lt "Why is this happening? Who could possible have don-- Gah?! My head!! Hurts!!!"
    call screen who_did_it
    lt "I think [who_did_it_choice.name] is the culprit. I must investigate to prove this!"
    lt "I suddenly have an uncontrollable urge to investigate the breakroom."
    lt "Ahh, that urge subsided. Now I can think with the dossier. So let's open it!"
    show text "{size=150}{color=#ff5100}Investigation{/color}{/size}" at truecenter, investigation_text_zoom
    pause 2.0
    hide text
    $ aai_active = True
    $ aai_travel_left = [mp_breakroom]
    jump debug_investigation_maptravel

label debug_investigation_end:
    n "This was the end."
    show text "{size=150}{color=#ff5100}Investigation END{/color}{/size}"  at truecenter, investigation_text_zoom
    pause 2.0
    hide text
    $ aai_active = False
    lt "Now I can continue with my business, like jumping back at the start."
    jump start

label debug_investigation_maptravel:
    if len(aai_travel_left) == 0: # done all investigations
        lt "Huh, it seems I investigated everything. I am ready!"
        jump debug_investigation_end
        
    $ dossier_tab_control = "map"
    call screen dossier_ui
    if aai_travel in aai_travel_done:
        lt "I actually already went to [aai_travel.name]."
        jump debug_investigation_maptravel
    if aai_travel not in aai_travel_left:
        lt "I don't have to do anything at [aai_travel.name]"
        jump debug_investigation_maptravel
    lt "I know! I'll visit [aai_travel.name] next!"
    $ dossier_tab_control = "evidence"

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
            if mp_breakroom in aai_travel_left:
                n "There is nothing to do here. However, you investigated everything in here!"
                $ aai_investigated(mp_breakroom)
            else:
                lt "I've already investigated every nook and cranny in here."
                lt "I better MOVE somewhere else instead."
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
            jump debug_investigation_maptravel
        c "Keep going until you are satisfied!"
            


# label debug_investigate_breakroom_end:
#     c "Did you find what you needed?"
#     l "Not yet, I need to investigate moreeee."
#     c "No. You are boring. Get out. "