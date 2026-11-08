default persistent.chose_lang = False

screen language_select:
    vbox:
        xalign 0.5
        yalign 0.5
        text "{color=#FF0000}Elige tu idioma/Choose your language{/color}"
        textbutton "{color=#FF0000}Español{/color}" action [Language("spanish"), Return()]
        textbutton "{color=#FF0000}English{/color}" action [Language(None), Return()]


label splashscreen:
    image white = Solid("#ffffff")   
    scene white
    with Pause(1)

    play sound "tick.ogg"

    show unq-splash with dissolve
    with Pause(2)

    scene white with dissolve
    with Pause(1)

    #show text "{color=#FF0000}Una producción de Bravo Jeremias{/color}" with dissolve
    show text "{color=#FF0000}Una producción de Raken...{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    # ON BOOT
    # LANGUAGE SELECTION ONCE

    if not persistent.chose_lang:
        $ persistent.chose_lang = True
        call screen language_select
    return   