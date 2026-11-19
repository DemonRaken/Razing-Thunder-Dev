init python:
    renpy.music.register_channel("blips", mixer="sfx", loop=False)
    def blip(event, interact=True, blipfile="", bliploop=False, **kwargs):
        if not interact:
            return
        if not blipfile:
            return
        if event == "show_done":
            renpy.music.play(blipfile, channel="blips", loop=bliploop)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips", fadeout=0.1)   