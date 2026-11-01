init python:
    def blip(event, interact=True, blipfile="", bliploop=False, **kwargs):
        if not interact:
            return
        if not blipfile:
            return
        if event == "show_done":
            renpy.sound.play(blipfile, loop=bliploop)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(fadeout=0.1)