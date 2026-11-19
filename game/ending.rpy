## ending.rpy — Character roll-call followed by a credits roll.
## Drop into game/. Call `ending_sequence` when the story is done.
## Requires: the ctc_horse image (already defined elsewhere in your project).

## ------------------------------------------------------------------ config ---

## Who appears, in what order, with which sprite and how they're credited.
define ENDING_CAST = [
    ("cata neutral",  "Catalina Moreno"),
    ("leo neutral",   "El Leopardo"),
    ("tony neutral",  "Antonio Ortiz"),
    ("rena neutral",  "Renata Vargas"),
    ("lu neutral",    "Lucas Mendoza"),
    ("est neutral",   "Esteban Rojas"),
    ("seb neutral",   "Sebastian Castillo"),
    ("en neutral",    "Lorenzo Villareal"),
    ("me neutral",    "Sofía Medina"),
]

## Per-card timings (seconds). Total per card = SLIDE_IN + HOLD + SLIDE_OUT.
define ENDING_SLIDE_IN  = 0.6
define ENDING_HOLD      = 3.0
define ENDING_SLIDE_OUT = 0.6

## Background behind the cards.
define ENDING_BG = "placeholder_park"

## Horse decoration: 0 hides it; 1.0 = default size; try 1.5–2.0 for ending.
define ENDING_HORSE_SCALE = 3

## --------------------------------------------------------------- credits ---

## Edit freely. `{b}...{/b}` is bold, `{size=+N}` grows text, `{color=#...}`
## tints. Blank lines separate sections.
define CREDITS_TEXT = """
{size=+14}{b}Razing Thunder{/b}{/size}

{size=-6}This needs translating too ugh{/size}

{color=#888888}· · ·{/color}

{b}Written and Directed by{/b}
Raken

{b}Character Art{/b}
Raken

{b}Backgrounds{/b}
The Internetz

{b}Music{/b}
The Internets

{b}Engine{/b}
Ren'Py

{b}Special Thanks{/b}
Everyone who read it

{color=#888888}· · ·{/color}

{size=+6}Thank you for playing.{/size}
"""

## Scroll tuning:
##   - If the credits get cut off before the pause ends, make
##     CREDITS_SCROLL_END more negative (e.g. -3000).
##   - If they linger on empty black at the end, make it less negative.
##   - CREDITS_DURATION controls scroll speed.
define CREDITS_TEXT_WIDTH   = 900
define CREDITS_TEXT_SIZE    = 26
define CREDITS_SCROLL_START = 1080    # starting ypos (bottom of screen)
define CREDITS_SCROLL_END   = -2200   # ending ypos (above the top)
define CREDITS_DURATION     = 45.0    # total scroll time (seconds)

## --------------------------------------------------------------- transforms ---

## One card: slide in from the right, hold, slide out to the left, fade.
transform ending_card:
    xalign 1.3
    yalign 1.0
    alpha 0.0
    ease ENDING_SLIDE_IN xalign 0.5 alpha 1.0
    pause ENDING_HOLD
    ease ENDING_SLIDE_OUT xalign -0.3 alpha 0.0

## Name label fades in a beat after the portrait arrives.
transform ending_name_fade:
    xpos 0.72
    ypos 0.865
    alpha 0.0
    pause 0.4
    linear 0.4 alpha 1.0

## Re-anchors the horse bottom-right and applies the configured scale.
transform ending_horse:
    xpos 0.82
    ypos 0.865
    xanchor 1.0
    yanchor 1.0
    zoom ENDING_HORSE_SCALE

## Scrolls the credits vbox from below the screen to above it.
transform credits_scroll:
    xalign 0.5
    ypos CREDITS_SCROLL_START
    linear CREDITS_DURATION ypos CREDITS_SCROLL_END

## ------------------------------------------------------------------ screens ---

screen ending_name(name):
    zorder 50
    frame:
        at ending_name_fade
        xalign 0.5
        yalign 0.15
        background "#000000aa"
        padding (30, 15)
        text name:
            size 42
            color "#ffffff"
            outlines [(2, "#000000", 1, 1)]
            xalign 0.5

screen credits_screen():
    zorder 50
    add Solid("#000000")

    vbox:
        at credits_scroll
        xsize CREDITS_TEXT_WIDTH
        spacing 8
        text CREDITS_TEXT:
            text_align 0.5
            color "#ffffff"
            size CREDITS_TEXT_SIZE

    textbutton _("Skip"):
        action Return()
        xalign 0.98
        yalign 0.96
        text_size 18
        text_color "#ffffff88"
        text_hover_color "#ffffffff"

## ------------------------------------------------------------------ labels ---

label ending_roll_call:
    scene expression (ENDING_BG or "black") with Dissolve(0.5)

    if ENDING_HORSE_SCALE > 0:
        show ctc_horse at ending_horse

    python:
        total = ENDING_SLIDE_IN + ENDING_HOLD + ENDING_SLIDE_OUT
        for sprite, name in ENDING_CAST:
            renpy.show(sprite, at_list=[ending_card])
            renpy.show_screen("ending_name", name=name)
            renpy.pause(total, hard=True)
            renpy.hide(sprite)
            renpy.hide_screen("ending_name")

    if ENDING_HORSE_SCALE > 0:
        hide ctc_horse

    scene black with Dissolve(0.8)
    return

label credits_roll:
    scene black with Dissolve(0.5)
    show screen credits_screen
    ## hard=True: clicks/keys won't dismiss it; only the Skip button will.
    ## If you'd rather allow click-to-skip, change to hard=False.
    $ renpy.pause(CREDITS_DURATION, hard=True)
    hide screen credits_screen
    pause 0.8
    return

## One entry point: roll call, then credits. Call this from your end label.
label ending_sequence:
    call ending_roll_call
    call credits_roll
    return