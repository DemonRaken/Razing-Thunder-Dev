default persistent.chose_lang = False

screen language_select:
    vbox:
        xalign 0.5
        yalign 0.5
        text "Elige tu idioma\nChoose your language"
        textbutton "Español" action [Language("spanish"), Return()]
        textbutton "English" action [Language(None), Return()]
        


label splashscreen:
    image white = Solid("#ffffff")   
    scene white
    with Pause(1)

    play sound "tick.ogg"

    show unq-splash with dissolve
    with Pause(2)

    scene white with dissolve
    with Pause(1)

    show text "{color=#000000}Raken Presents...{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    # ON BOOT
    # LANGUAGE SELECTION ONCE

    if not persistent.chose_lang:
        $ persistent.chose_lang = True
        call screen language_select
    return   