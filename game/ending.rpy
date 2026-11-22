## ending.rpy — Character roll-call followed by a credits roll.
## Drop into game/. Call `ending_sequence` when the story is done.
## Requires: the ctc_horse image (already defined elsewhere in your project).

## ------------------------------------------------------------------ config ---

define ENDING_CAST = [
    ("tony smile",  "Antonio Ortiz"),
    ("cata neutral",  "Catalina Moreno"),
    ("rena smile",  "Renata Vargas"),
    ("lu neutral",    "Lucas Mendoza"),
    ("vi smile",    "Vicente Ruiz"),
    ("en grin",    "Lorenzo Villareal"),
    ("me smile",    "Sofía Medina"),
    ("seb smile3",   "Sebastian Castillo"),
    ("est smile",   "Esteban Rojas"),
    ("leo point",   "El Leopardo"),
]

define ENDING_SLIDE_IN  = 0.6
#define ENDING_HOLD      = 3.0

define ENDING_SLIDE_OUT = 0.6

define ENDING_BG = ""
define ENDING_HORSE_SCALE = 3

## Layout knobs for the split view.
##   CREDITS_XPOS — horizontal center of the credits column (0=left, 1=right).
##   CAST_XPOS    — horizontal resting spot for characters.
define CREDITS_XPOS = 0.27
define CAST_XPOS    = 0.78

## --------------------------------------------------------------- credits ---

define CREDITS_TEXT_WIDTH   = 900
define CREDITS_TEXT_SIZE    = 26
define CREDITS_SCROLL_START = 1080
define CREDITS_SCROLL_END   = -2200
define CREDITS_DURATION     = 28

define ENDING_HOLD      = CREDITS_DURATION/(len(ENDING_CAST)*2)

define track_list = """
Backstreet Swing
Black Crystal
Cerebral Maze
Echoed Art
Last Embrace (vocals)
Oceanfront
Rituale Machina
Secret Corridor
Silent Shadows
Silent Witness
Sunlit Cafe
Tender Gaze (vocals)
The City Breathes Your Name
Wacky Witness
Material Creep
"""

define CREDITS_TEXT = """
{size=+14}{b}Razing Thunder{/b}{/size}

{size=-6}...{/size}

{color=#888888}· · ·{/color}

{b}Created by{/b}
[author]

{b}Writing and Direction{/b}
[author]

{b}Editing and Proofreading{/b}
[author]

{b}Character Art{/b}
[author]

{b}Additional Art{/b}
[author]

{b}Music{/b}
PeriTune (peritune.com)
{i}[track_list]{/i}

{b}Sound Effects{/b}
Joseph SARDIN - BigSoundBank.com

{b}Engine{/b}
Ren’Py by PyTom and contributors

{b}Beta Testers{/b}
TBA

{b}Special Thanks{/b}
Everyone who read it to the end.

{color=#888888}· · ·{/color}

{size=+6}Thank you for playing.{/size}

{size=-4}© 2026 [author]. All rights reserved.
Version [_version]
https://demonraken.itch.io/razing-thunder{/size}
"""


## --------------------------------------------------------------- transforms ---

## Slide in from the right, rest on the right side, slide back out right.
transform ending_card:
    xalign 1.3
    yalign 1.0
    alpha 0.0
    ease ENDING_SLIDE_IN xalign CAST_XPOS alpha 1.0
    pause ENDING_HOLD
    ease ENDING_SLIDE_OUT xalign 1.3 alpha 0.0

## Name label sits above the character, top-right.
transform ending_name_fade:
    xalign CAST_XPOS
    #ypos 0.06
    ypos 0.69
    xpos 0.69
    alpha 0.0
    pause 0.4
    linear 0.4 alpha 1.0

## Bottom-right corner decoration.
transform ending_horse:
    xpos 0.59
    ypos 0.59
    xanchor 1.0
    yanchor 1.0
    zoom ENDING_HORSE_SCALE

## Scrolls up the left-hand column.
transform credits_scroll:
    xpos CREDITS_XPOS
    xanchor 0.2
    ypos CREDITS_SCROLL_START
    linear CREDITS_DURATION ypos CREDITS_SCROLL_END

## ------------------------------------------------------------------ screens ---

screen ending_name(name):
    zorder 50
    frame:
        at ending_name_fade
        background "#000000aa"
        padding (30, 15)
        text name:
            size 42
            color "#ffffff"
            outlines [(2, "#000000", 1, 1)]
            xalign 0.5
            font gui.name_text_font

screen credits_screen():
    zorder 50
    ## No Solid here — the `scene black` behind provides the background so
    ## the characters on the right remain visible.
    vbox:
        at credits_scroll
        xsize CREDITS_TEXT_WIDTH
        spacing 8
        text CREDITS_TEXT:
            text_align 0.5
            color "#ffffff"
            size CREDITS_TEXT_SIZE
            font gui.text_font

    textbutton _("Skip"):
        action [SetVariable("ending_skipped", True), Return()]
        xalign 0.98
        yalign 0.96
        text_size 18
        text_color "#ffffff88"
        text_hover_color "#ffffffff"

## ------------------------------------------------------------------ labels ---

default ending_skipped = False

## Roll call and credits play simultaneously.
label ending_sequence:
    scene expression (ENDING_BG or "black") with Dissolve(0.5)
    $ dossier_enabled = False
    $ ending_skipped = False
    $ quick_menu = False

    play music ending

    if ENDING_HORSE_SCALE > 0:
        show ctc_horse at ending_horse

    show screen credits_screen

    python:
        card_total = ENDING_SLIDE_IN + ENDING_HOLD + ENDING_SLIDE_OUT
        total_roll = card_total * len(ENDING_CAST)

        for sprite, name in ENDING_CAST:
            if ending_skipped:
                break
            renpy.show(sprite, at_list=[ending_card], zorder=10)
            renpy.show_screen("ending_name", name=name)
            renpy.pause(card_total, hard=True)
            renpy.hide(sprite)
            renpy.hide_screen("ending_name")

        ## If credits scroll longer than the roll call, wait out the rest.
        if not ending_skipped:
            remaining = CREDITS_DURATION - total_roll
            if remaining > 0:
                renpy.pause(remaining, hard=True)

    if not ending_skipped:
        pause 0.8
        show text "Thank you for playing!":
            xalign 0.5
            yalign 0.6
            alpha 0.0
            linear 0.8 alpha 1.0
        pause 2.0
        scene black with fade
        pause 0.2
        stop music fadeout 1.5
        pause 1.5
    
    hide screen credits_screen
    hide ctc_horse
    scene black
    stop music
    $ quick_menu = True
    $ config.main_menu_music = audio.embrace_offvo
    return